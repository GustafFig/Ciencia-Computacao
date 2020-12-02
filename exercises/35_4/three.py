import re

EMAIL_REGEX = re.compile(r"^[A-z][-\w_]*@\w+\.\w{1,3}$")


def verify_email(email):
    if not email.startswith("_") and EMAIL_REGEX.match(email) is not None:
        return True
    raise ValueError(f"{email} inváilo")
