from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum


if __name__ == "__main__":
    # array = [1, 2, 3, 4, 5]

    t1 = time.time()
    pool = Pool()
    result = pool.map(f, range(100000))
    pool.close()
    pool.join()
    print("pool took: ", time.time()-t1)

    t2 = time.time()
    result = []
    for n in range(100000):
        result.append(f(n))

    print("serial processing took: ", time.time()-t2)

