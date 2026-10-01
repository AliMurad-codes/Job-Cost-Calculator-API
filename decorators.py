import time
from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Finished {func.__name__}")

        return result

    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(
            f"[TIME] {func.__name__} "
            f"took {execution_time:.6f} seconds"
        )

        return result

    return wrapper