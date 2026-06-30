def main():
    number = 10
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"Factorial of {number} is {factorial}")


if __name__ == "__main__":
    main()
