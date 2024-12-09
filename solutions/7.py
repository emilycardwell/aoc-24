# AOC DAY 7

def day7(data):
    clean_data = {l.split(':')[0]: l.split(':')[1].split() for l in data.splitlines()}
    total_cal1 = 0
    total_cal2 = 0
    for k, values in clean_data.items():
        old_cal1 = [values[0]]
        old_cal2 = [values[0]]
        new_cal1 = []
        new_cal2 = []
        for v in values[1:]:
            for cal1 in old_cal1:
                if int(cal1) <= int(k):
                    new_cal1.append(int(cal1) + int(v))
                    new_cal1.append(int(cal1) * int(v))
            for cal2 in old_cal2:
                if int(cal2) <= int(k):
                    new_cal2.append(int(cal2) + int(v))
                    new_cal2.append(int(cal2) * int(v))
                    new_cal2.append(int(str(cal2) + v))
            old_cal1 = new_cal1
            old_cal2 = new_cal2
            new_cal1 = []
            new_cal2 = []

        if int(k) in old_cal1:
            total_cal1 += int(k)
        if int(k) in old_cal2:
            total_cal2 += int(k)

    return total_cal1, total_cal2


if __name__ == "__main__":
    with open('input/7.txt') as f:
        data = f.read()

    solution1, solution2 = day7(data)

    print("The solution for part 1 is:", solution1)
    print("The solution for part 2 is:", solution2)
