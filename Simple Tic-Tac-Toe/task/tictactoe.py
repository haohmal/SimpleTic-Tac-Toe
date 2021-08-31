in_string = input()

print("-" * 8)
for i in range(3):
    print("| {0} {1} {2} |".format(in_string[i * 3], in_string[i * 3 + 1], in_string[i * 3 + 2]))
print("-" * 8)