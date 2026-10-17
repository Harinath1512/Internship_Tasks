# Merge the Tools!

# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        result = ""

        for ch in sub:
            if ch not in result:
                result += ch

        print(result)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)