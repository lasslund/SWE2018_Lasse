from fuzzing.fuzzer import FuzzExecutor

# Files to use as initial input seed.
file_list = ["./test_string.txt"]


# List of applications to test.
apps_under_test = ["python RLE_RLD.py -e".replace(" ","&")]

number_of_runs = 30

def test():
    print("start test")
    fuzz_executor = FuzzExecutor(apps_under_test, file_list)
    fuzz_executor.run_test(number_of_runs)
    print("Tests finished")
    return fuzz_executor.stats

def main():
    print("Hello")
    stats = test()
    print(stats)

if __name__ == "__main__":
	main()
