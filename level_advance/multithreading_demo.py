"""
Multithreading example (bad for image processing)
"""

import threading
import time
from pil_demo import process_image


def run():
    start_time = time.time()

    threads = []
    for index in range(1, 5):
        thread = threading.Thread(target=process_image, args=(f"{index}.jpg",))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"All images processed in {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    # test the process 10 times
    for _ in range(10):
        run()
