import secrets
import string


def code_generator(length=8, characters=string.ascii_letters):
    """Generate a random code."""
    return "".join(secrets.choice(characters) for _ in range(length))
