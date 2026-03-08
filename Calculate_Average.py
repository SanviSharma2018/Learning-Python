data = {'sunita': 100, 'sanvi': 40, 'vikas': 130, 'aarav': 20}

total = 0

for key, val in data.items():
    total += val

print(f"Average: {total / len(data)}")
