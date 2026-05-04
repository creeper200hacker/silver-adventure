from multiprocessing import Pool

def heavy_operation(number):
    return sum(i * i for i in range(number))

if __name__ == "__main__":
    numbers = [1_000_000, 1_000_000, 1_000_000, 1_000_000]
    with Pool(processes=4) as pool:
        results = pool.map(heavy_operation, numbers)
    print(results)
