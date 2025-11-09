"""A generator for up to 999 random numbers.
    Also sorts numbers in ascending/descending order."""

import random

# --- Constants ---
MIN_RANDOM = 1
MAX_RANDOM = 999
INVALID_INPUT_MESSAGE = "Invalid Input"


def bubble_sort(lst, ascending=True):
    """Used to sort the lists numerically"""
    n = len(lst)
    if n < 2:
        return
    while True:
        swapped = False
        for i in range(n - 1):
            a = lst[i]
            b = lst[i + 1]
            if ascending:   # Check which order to sort
                if a > b:
                    tmp = lst[i]    # swap with a temp
                    lst[i] = lst[i + 1]
                    lst[i + 1] = tmp
                    swapped = True
            else:
                if a < b:
                    tmp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = tmp
                    swapped = True
        if not swapped:
            break


def main():
    """Runs the actual generator and prints the result."""
    user_input = input(f"How many random numbers in the range {MIN_RANDOM} - {MAX_RANDOM} are desired? ")
    try:
        count = int(user_input)     # Convert to int here and perform check
    except ValueError:
        print(INVALID_INPUT_MESSAGE)
        return
    if count < MIN_RANDOM:
        print(INVALID_INPUT_MESSAGE)
        return
    if count > MAX_RANDOM:
        print(INVALID_INPUT_MESSAGE)
        return

    numbers = []
    try:
        while len(numbers) < count:
            num = random.randint(MIN_RANDOM, MAX_RANDOM)    # Generate random numbers
            try:
                numbers.append(num)                             # and append them to the list
            except IndexError:
                print("Unexpected indexing error; cannot create the list of random numbers.")
                return
    except MemoryError:
        print("System memory limit reached; cannot create the list of random numbers.")
        return

    print("\nHere are the random numbers:")
    for i, v in enumerate(numbers):
        end_char = " " if i != len(numbers) - 1 else ""
        print(v, end=end_char)
    print("\n")

    # Split into evens and odds
    evens = []
    odds = []
    try:
        for i in range(len(numbers)):
            val = numbers[i]
            if val % 2 == 0:
                evens.append(val)
            else:
                odds.append(val)
    except IndexError:
        print("Unexpected indexing error while classifying numbers as even or odd.")
        return

    # Use bubble sort in normal and reversed order (via boolean)
    bubble_sort(evens, ascending=True)
    bubble_sort(odds, ascending=False)

    # Print the finished list
    print("Here are the random numbers arranged:")
    if len(evens) == 0:
        left = "No Even Numbers"
    else:
        left = " ".join(str(x) for x in evens)
    if len(odds) == 0:
        right = "No Odd Numbers"
    else:
        right = " ".join(str(x) for x in odds)
    print(f"{left} - {right}\n")

    print(f"Of the above {count} numbers, {len(evens)} were even and {len(odds)} odd")  # Print number-counter


if __name__ == "__main__":
    main()
