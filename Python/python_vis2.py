import multiprocessing
def sq(numbers):
    for n in numbers:
        print(f"Square of {n}: {n * n}", flush=True)

def cu(numbers):
    for n in numbers:
        print(f"Cube of {n}: {n * n * n}", flush=True)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = sq ,args = ([1,2,3,4],))
    p2 = multiprocessing.Process(target = cu ,args = ([1,2,3,4],))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("process")
    