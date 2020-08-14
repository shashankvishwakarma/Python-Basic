import time
import threading


def calc_square(number):
    print("calculate square of numbers")
    for n in number:
        time.sleep(0.2)
        print('Square: ', n * n)


def calc_cube(number):
    print("calculate cube of numbers")
    for n in number:
        time.sleep(0.2)
        print('Cube: ', n * n * n)


arr = [2, 3, 8, 9]
t = time.time()
thread1 = threading.Thread(target=calc_square, args=(arr,))
thread2 = threading.Thread(target=calc_cube, args=(arr,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("done in : ", time.time() - t)
print("Ha... I am done with all my work now!")
