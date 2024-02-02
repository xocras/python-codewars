# Human readable duration format

# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    duration = {
        "year": 31_536_000,
        "day": 86_400,
        "hour": 3_600,
        "minute": 60,
    }

    duration["year"], seconds = divmod(seconds, duration["year"])

    duration["day"], seconds = divmod(seconds, duration["day"])

    duration["hour"], seconds = divmod(seconds, duration["hour"])

    duration["minute"], seconds = divmod(seconds, duration["minute"])

    duration["second"] = seconds

    message = ""

    for key, value in duration.items():
        if not value:
            continue

        message += ', ' if message else ''
        message += f"{value} {key}{'s' if value != 1 else ''}"

    message = ' and '.join(message.rsplit(', ', 1))

    return message if message else 'now'