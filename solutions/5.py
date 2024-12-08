# AOC DAY 5


def day5_1(rules, updates):
    return sum((update[len(update) // 2])
               for update in updates if not any(
                   set(rule).issubset(update) and update.index(rule[0]) > update.index(rule[1]) for rule in rules))


def day5_2(rules, updates):

    def reorder(update):
        new = update.copy()

        for rule in rules:
            if set(rule).issubset(new):
                idx_1, idx_2 = new.index(rule[0]), new.index(rule[1])
                if idx_1 > idx_2:
                    new = new[:idx_2] + new[idx_2+1:idx_1] + rule + new[idx_1+1:]

        if new == update:
            return update
        else:
            return reorder(new)

    return sum(reorder(update)[len(update) // 2]
               for update in updates
               if any(set(rule).issubset(update) and update.index(rule[0]) > update.index(rule[1])
                      for rule in rules))



if __name__ == "__main__":
    with open('input/5.txt') as f:
        data = f.read()
        rules, updates = [[list(map(int,l.replace('|', ',').split(','))) for l in i.splitlines()] for i in data.split('\n\n')]

    solution1 = day5_1(rules, updates)
    solution2 = day5_2(rules, updates)

    print("The solution for part 1 is:", solution1)
    print("The solution for part 2 is:", solution2)
