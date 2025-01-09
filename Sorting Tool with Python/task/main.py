all_numbers = []

while True:
    try:
        data = input()
        items = data.split()
        for item in items:
            all_numbers.append(int(item))
    except EOFError:
        break

total = len(all_numbers)
greatest = max(all_numbers)
greatest_count = all_numbers.count(greatest)

print(f"Total numbers: {total}.")
print(f"The greatest number: {greatest} ({greatest_count} time(s)).")
