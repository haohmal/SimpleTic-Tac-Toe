prime_numbers = []
numbers = []
for i in range(2, 1001):
    if not any([i % n == 0 for n in numbers]):
        prime_numbers.append(i)
    numbers.append(i)