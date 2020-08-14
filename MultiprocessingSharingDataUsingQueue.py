import multiprocessing


def calc_square(numbers, queue):
    print("calculate square of numbers")
    for n in numbers:
        queue.put(n * n)


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(arr, queue))

    p.start()
    p.join()

    while queue.empty() is False:
        print(queue.get())

    print("Done!")
