d = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

frequency = {}
for v in d.values():
    if v in frequency:
        frequency[v] += 1
    else:
        frequency[v] = 1

print("Frequency of values:")
for key, val in frequency.items():
    print(f"{key} appears {val} times")
