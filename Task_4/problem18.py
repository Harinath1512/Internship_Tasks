# Lists

if __name__ == '__main__':
    N = int(input())
    a=[]
    for i in range(N):
        com=input()
        commands=com.split(' ')
        if commands[0]=='append':
            a.append(0+int(commands[1]))
        elif commands[0]=='insert':
            a.insert(0+int(commands[1]),0+int(commands[2]))
        elif commands[0]=='remove':
            a.remove(0+int(commands[1]))
        elif commands[0]=='pop':
            a.pop()
        elif commands[0]=='sort':
            a.sort()
        elif commands[0]=='reverse':
            a.reverse()
        elif commands[0]=='print':
            print(a)