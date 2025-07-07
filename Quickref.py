steps = 10
# Left-aligned staircase
for i in range(1, steps + 1):
    print("*" * i)

print()  # Blank line between the two staircases

# Right-aligned staircase
for i in range(1, steps + 1):
    print(" " * (steps - i) + "*" * i)
