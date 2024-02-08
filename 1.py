
numbers = ["2340", "1r"]
numbers = [int(s) for s in numbers if s.isdigit()]
print(numbers)