numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sorted(map(lambda x: x**2 if x % 2 == 0 else (x**3 if x % 3 == 0 else x + (x+1) + (x+2)), numbers))

print(result)