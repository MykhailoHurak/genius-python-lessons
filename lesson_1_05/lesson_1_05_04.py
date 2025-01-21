def print_numbers(start, stop):
    for number in range(start, stop):
        print(f"Current number is: {number}")
    print("-------")

ranges = [(1, 10), (5, 12), (50, 70)]

for start, stop in ranges:
    print(print_numbers(start, stop))
