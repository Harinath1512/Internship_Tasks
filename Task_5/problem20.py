# Piling Up!

# https://www.hackerrank.com/challenges/piling-up/problem

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    last = float('inf')
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > last:
            possible = False
            break

        last = current

    print("Yes" if possible else "No")
