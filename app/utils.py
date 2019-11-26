from datetime import date


def str2date(date_str: str) -> date:
    return date.fromisoformat(date_str)
