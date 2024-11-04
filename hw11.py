def process_numbers(numbers):
    result = []
    
    calc = lambda x: x**2 if x % 2 == 0 else (x**3 if x % 3 == 0 else x + (x+1) + (x+2))
    
    for num in numbers:
        result.append(calc(num))
    
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
processed_numbers = process_numbers(numbers)
print(processed_numbers)