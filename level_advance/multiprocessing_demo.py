"""
Multiprocessing example (good for image processing)
"""

import multiprocessing
from pil_demo import process_image
import time


def run():
    start_time = time.time()

    threads = []
    for index in range(1, 5):
        process = multiprocessing.Process(target=process_image, args=(f"{index}.jpg",))
        process.start()
        threads.append(process)

    for process in threads:
        process.join()

    end_time = time.time()

    print(f"All images processed in {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    # test the process 10 times
    for _ in range(10):
        run()
