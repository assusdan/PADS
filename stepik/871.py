def count_max(stairs):
    prev = 0
    curr = stairs[0]

    for stair in stairs[1:]:
        prev, curr = curr, max(prev, curr) + stair

    return curr


def main():
    input()
    stairs = [int(i) for i in input().split()]

    print(stairway_up(stairs))


if __name__ == '__main__':
    main()
