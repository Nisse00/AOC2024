def is_safe(sequence):
    increasing = all(1 <= sequence[i] - sequence[i - 1] <= 3 for i in range(1, len(sequence)))
    decreasing = all(1 <= sequence[i - 1] - sequence[i] <= 3 for i in range(1, len(sequence)))
    return increasing or decreasing

safe = 0

with open("input", "r") as file:
    for line in file:
        temp = list(map(int, line.split()))
        if is_safe(temp):
            safe += 1
            continue

        for i in range(len(temp)):
            modified = temp[:i] + temp[i + 1:]
            if is_safe(modified):
                safe += 1
                break

print(safe)
