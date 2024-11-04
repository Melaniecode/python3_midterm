def computation(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x ** 2
        elif x % 3 == 0:
            yield x ** 3
        else:
            yield x + (x + 1) + (x + 2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(computation(numbers))
print(result)