import re

RE_EMAIL = RE_EMAIL = re.compile(r'^[a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*@(([a-zA-Z0-9]+)(-[a-zA-Z0-9]+)*)(\.([a-zA-Z0-9]+)(-[a-zA-Z0-9]+)*)+$')

if RE_EMAIL.match("simon@gamil.com") is None:
    print("Invalid email address")

