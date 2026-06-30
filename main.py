def main():
    number = 10
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    fibonacci_series = [0, 1]

    while len(fibonacci_series) < 10:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])

    print(f"Factorial of {number} is {factorial}")
    print("First 10 Fibonacci numbers:")
    print(fibonacci_series)


if __name__ == "__main__":
    main()
