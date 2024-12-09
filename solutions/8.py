# AOC DAY 8


def day8(nodes, h, w):
    antinodes1 = set()
    antinodes2 = set()
    for node in nodes.values():
        for i in range(len(node)):
            for j in set(range(len(node))) - {i}:
                n1r, n1c, n2r, n2c = node[i][0], node[i][1], node[j][0], node[j][1]
                if h > n1r*2-n2r >= 0 and w > n1c*2-n2c >= 0:
                    antinodes1.add((n1r*2-n2r, n1c*2-n2c))
                b = round(n1r - ((n2r-n1r)/(n2c-n1c))*n1c, 4)
                for r in range(h):
                    c = round((r - b)*((n2c-n1c)/(n2r-n1r)),3)
                    if w > c >= 0 and (c % 1 == 0.0):
                        antinodes2.add((r, int(c)))

    return len(antinodes1), len(antinodes2)

if __name__ == "__main__":
    with open('input/8.txt') as f:
        data = f.read()

    clean_data = data.splitlines()
    h, w = len(clean_data), len(clean_data[0])

    nodes = {node: [(row, col) for row in range(h) for col in range(w) if clean_data[row][col] == node]
                    for node in set(data.replace('\n', '').replace('.', ''))}

    solution1, solution2 = day8(nodes, h, w)

    print("The solution for part 1 is:", solution1)
    print("The solution for part 2 is:", solution2)
