from threading import Thread, Lock
from time import time

mutex = Lock()


def add_range_no_sync(num_range):
    global num
    for i in num_range:
        num += i


def add_range_sync_naive(num_range):
    global num
    for i in num_range:
        mutex.acquire()
        num += i
        mutex.release()


def add_range_smart_sync(num_range):
    global num

    local_acc = int()
    for i in num_range:
        local_acc += i
    mutex.acquire()
    num += local_acc
    mutex.release()


def sum_ranges(range1, range2, implementation):
    stamp = time()

    t1 = Thread(target=implementation, args=[range1])
    t2 = Thread(target=implementation, args=[range2])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return time() - stamp


if __name__ == "__main__":
    range1 = range(0, 1000000)
    range2 = range(1000000, 2000001)

    # No Sync Implementation
    num = int()
    took = sum_ranges(range1, range2, add_range_no_sync)
    print("sum (no sync): {}\n duration: {}".format(num, took))

    # Naive Sync Implementation
    num = int()
    took = sum_ranges(range1, range2, add_range_sync_naive)
    print("sum (naive sync): {}\n duration: {}".format(num, took))

    # Smart Sync Implementation
    num = int()
    took = sum_ranges(range1, range2, add_range_smart_sync)
    print("sum (smart sync): {}\n duration: {}".format(num, took))
