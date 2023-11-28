def plusOne(digits):
    s = ""
    for d in digits:
        s += str(d)
    num = int(s)
    num = num + 1
    li = []

    while num > 0:
        li.append(num % 10)
        print(num % 10)
        num = num // 10
    li.reverse()
    return li


def main():
    # li = list(map(int, input().split()))
    li = [int(x) for x in input().split()]
    ans = plusOne(li)
    print(ans)


if __name__ == '__main__':
    main()
