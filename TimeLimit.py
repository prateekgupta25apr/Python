from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time


def my_task():
    print("Execution starts")
    time.sleep(2)
    print("Execution stops")


executor = ThreadPoolExecutor(max_workers=1)
future = executor.submit(my_task)

try:
    future.result(timeout=3)
except TimeoutError:
    print("Execution timed out!")
finally:
    executor.shutdown()
