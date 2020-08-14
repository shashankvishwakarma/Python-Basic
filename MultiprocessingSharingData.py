import multiprocessing


def calc_square(numbers, result, v):
    print("calculate square of numbers")
    v.value = 5.05
    for idx, n in enumerate(numbers):
        result[idx] = n * n
    print("within the process square result: ", result[:])


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    result = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))

    p1.start()
    p1.join()

    print("outside the process square result using array: ", result[:])
    print("outside the process square result using value: ", v.value)
    print("Done!")
