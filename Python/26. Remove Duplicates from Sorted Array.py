def removeDuplicates(nums) -> int:
    i = 1
    prev = nums[0]
    n = len(nums)
    for j in range(1, n):
        if prev != nums[j]:
            prev = nums[j]
            nums[i] = nums[j]
            i += 1
    return i


def main():
    # li = list(map(int, input().split()))
    li = [int(x) for x in input().split()]
    ans = removeDuplicates(li)
    print(ans)


if __name__ == '__main__':
    main()
