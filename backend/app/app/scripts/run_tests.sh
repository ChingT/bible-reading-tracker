#!/usr/bin/env bash

set -e
set -x

python -m pytest app/tests --cov --cov-report=html:coverage_re
