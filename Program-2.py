def generate_odd_series(a):
    result = []
    for i in range(1, a + 1):
        odd = 2 * i - 1
        result.append(odd)
    return result
a = int(input("Enter value of a: "))
print("Output:", generate_odd_series(a))
