
def main():
    nums = list(map(int, open('day01.txt').read().splitlines()))

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            for k, num3 in enumerate(nums):
                if i == j or j == k:
                    continue
                if num1 + num2 + num3 == 2020:
                    print(num1 * num2 * num3)
                    quit()


if __name__ == "__main__":
    main()
