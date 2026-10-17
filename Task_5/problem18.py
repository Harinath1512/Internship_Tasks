# The Minion Game

# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    vowels = 'AEIOU'
    stuart=0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)