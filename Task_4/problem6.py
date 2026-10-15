# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    large=float('-inf')
    second=float('-inf')
    for i in arr:
        if i>large:
            second=large
            large=i
        elif i!=large and i>second:
            second=i
    print(second)