from typing import List


# This function is for part one
def is_safe(arr: List[int]) -> bool:
    # See if level is compliant with the rules
    # Check decreasing
    i = 0
    j = 1

    decreasing = True
    increasing = True
    while i < len(arr) - 1:
        while j < len(arr):
            if arr[j] < arr[i] and abs(arr[j] - arr[i]) < 4:
                j += 1
                i += 1
            else:
                decreasing = False
                break
        if not decreasing:
            break

    i = 0
    j = 1
    # Check increasing
    while i < len(arr) - 1:
        while j < len(arr):
            if arr[j] > arr[i] and abs(arr[j] - arr[i]) < 4:
                j += 1
                i += 1
            else:
                increasing = False
                break
        if not increasing:
            break
    return decreasing or increasing


# This function is for part two
def problem_dampener(arr: List[int]) -> bool:
    # See if we can skip one element to get level safe
    for skip in range(len(arr)):
        temp_arr = [arr[i] for i in range(len(arr)) if i != skip]
        if is_safe(temp_arr):
            return True

    print("\n\n")

    return False


if __name__ == "__main__":
    f = open("./input.txt")
    all_levels = []
    for line in f.readlines():
        arr = line.split(" ")
        arr[-1] = arr[-1].strip()
        arr = list(map(int, arr))
        all_levels.append(arr)

    safe = 0
    unsafe_levels = []
    for arr in all_levels:
        if is_safe(arr):
            safe += 1
        else:
            unsafe_levels.append(arr)

    print(f"There are {safe} levels")

    for arr in unsafe_levels:
        if problem_dampener(arr):
            safe += 1

    print(f"After problem dampner {safe}")
