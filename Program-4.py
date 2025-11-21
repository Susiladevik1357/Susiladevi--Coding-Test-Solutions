def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = 0
        for n in numbers:
            if n % i == 0:
                count += 1
        result[i] = count
    return result
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Output:", count_multiples(numbers))
