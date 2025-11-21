def conditional_odd_series(a):
    # If 'a' is even use a-1, if odd use a
    length = a if a % 2 != 0 else a - 1

    result = []
    for i in range(1, length + 1):
        odd = 2 * i - 1
        result.append(odd)
    return result
a = int(input("Enter value of a: "))
print("Output:", conditional_odd_series(a))
