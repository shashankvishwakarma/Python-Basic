import multiprocessing

square_result = []
cube_result = []


def calc_square(number):
    print("calculate square of numbers")
    for n in number:
        square_result.append(n * n)
    print("within the process square result: ", str(square_result))


def calc_cube(number):
    print("calculate cube of numbers")
    for n in number:
        cube_result.append(n * n * n)
    print("within the process cube result: ", str(cube_result))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
