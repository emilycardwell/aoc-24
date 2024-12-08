# AOC DAY 4


def day4_1(data):
    l = len(data)
    words = (data + list(map(''.join, zip(*data))) +
            [''.join(data[i][i + k] for i in range(l - k)) for k in range(l-3)] +
            [''.join(data[i + k][i] for i in range(l - k)) for k in range(1, l-3)] +
            [''.join(data[l-1-(i+k)][i] for i in range(l - k)) for k in range(l-3)] +
            [''.join(data[l-1-i][i+k] for i in range(l - k)) for k in range(1, l-3)])

    i = 0
    for w in words:
        while w:
            idx = w.find('XMAS')
            ridx = w.find('SAMX')
            if idx == -1 and ridx == -1:
                w = None
            elif idx != -1 and ridx != -1:
                i += 1
                w = w[min(idx, ridx)+1:]
            elif idx == -1 or ridx == -1:
                i += 1
                w = w[max(idx, ridx)+1:]
            else:
                print('error in word find')
                w = None

    return i

def day4_2(data):
    c = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == 'A':
                d1 = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
                d2 = data[i-1][j+1] + data[i][j] + data[i+1][j-1]
                if (d1 == 'MAS' or d1 == 'SAM') & (d2 == 'MAS' or d2 == 'SAM'):
                    c += 1
    return c


if __name__ == "__main__":
    with open('input/4.txt') as f:
        data = f.read()
        data = data.split()

    solution1 = day4_1(data)
    solution2 = day4_2(data)

    print("The solution for part 1 is:", solution1)
    print("The solution for part 2 is:", solution2)
