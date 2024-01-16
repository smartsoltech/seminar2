import logging
from functools import wraps

def log_function_call(logger):
    def decorator_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Вызов функции: {func.__name__} с аргументами: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Функция {func.__name__} завершилась успешно с результатом: {result}")
                return result
            except Exception as e:
                logger.exception(f"Ошибка в функции {func.__name__}: {e}")
                raise
        return wrapper
    return decorator_log