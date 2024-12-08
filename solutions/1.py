# AOC DAY 1


def day1_1(data):
    clean_ids = [sorted(list(map(int,x))) for x in list(zip(*[x.split() for x in data.splitlines()]))]
    return sum([abs(a - b) for a, b in zip(*clean_ids)])

def day1_2(data):
    clean_ids = [(list(map(int,x))) for x in list(zip(*[x.split() for x in data.splitlines()]))]
    return sum([i * clean_ids[1].count(i) for i in clean_ids[0]])


if __name__ == "__main__":
    with open('input/1.txt') as f:
        data = f.read()
    solution1 = day1_1(data)
    solution2 = day1_2(data)

    print("The solution for part 1 is:", solution1)
    print("The solution for part 2 is:", solution2)
