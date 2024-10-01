def decorator(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(iters):
                start = time.time()
                func(*args, **kwargs)
                total_time += time.time() - start
            print(f"Function {func.__name__} completed in {total_time}")

        return wrapper

    return actual_decorator


@decorator(2)
def wait_time():
    time.sleep(1)

decorator(iters=2)(wait_time)()


