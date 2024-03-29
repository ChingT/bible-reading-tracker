"""Main FastAPI app instance declaration."""

import logging
import time
from pathlib import Path

from celery.signals import after_setup_logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.api import api_router
from app.core.celery_app import create_celery
from app.core.config import settings

logger = logging.getLogger("app")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
)
app.include_router(api_router, prefix=settings.API_V1_STR)

# Sets all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Guards against HTTP Host Header attacks
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)


@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:0.4f} sec"
    logger.info(
        "Processed request %s in %s s", request.url, response.headers["X-Process-Time"]
    )
    return response


celery = create_celery()


@after_setup_logger.connect
def setup_celery_logger(logger, *args, **kwargs):
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("tasks")
    fh = logging.FileHandler("logs/tasks.log")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("logging file path: %s", fh.baseFilename)


def set_logger():
    logs_folder = Path("logs")
    logs_folder.mkdir(parents=True, exist_ok=True)
    log_path = logs_folder / "app.log"
    logger = logging.getLogger("app")

    fmt = "%(asctime)s [%(levelname)s]\t%(message)s"
    datefmt = "%Y/%m/%d %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


set_logger()
