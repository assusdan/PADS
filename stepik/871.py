def stairway_up(stairs):
    previous = 0
    current = stairs[0]

    for stair in stairs[1:]:
        previous, current = current, max(previous, current) + stair

    return current


def main():
    n_ = input()
    stairs = [int(i) for i in input().split()]

    print(stairway_up(stairs))


if __name__ == '__main__':
    main()
