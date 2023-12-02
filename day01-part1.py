
# Brute force for simplicity. Could alternatively sort and work inward from opposite ends.
def main():
    nums = list(map(int, open('day01.txt').read().splitlines()))

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i == j:
                continue
            if num1 + num2 == 2020:
                print(num1 * num2)
                quit()


if __name__ == "__main__":
    main()
