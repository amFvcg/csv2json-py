from functools import wraps


def nullable(func):
    wraps(func)

    def wrapper(val):
        if len(val) is None or\
           val == 'null':
            return None
        return func(val)
    return wrapper


def bool(val):
    return True if val in ['y', 'Y', '1']\
        else False if val in ['n', 'N', '0']\
        else None
