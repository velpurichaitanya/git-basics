def main():
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < 10:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])

    print("First 10 Fibonacci numbers:")
    print(fibonacci_series)


if __name__ == "__main__":
    main()
