if __name__ == '__main__':
    N = int(input())   # number of commands
    my_list = []       # initialize empty list
    
    for _ in range(N):
        command = input().split()   # split command by spaces
        cmd = command[0]            # first word is the command
        
        if cmd == "insert":
            i = int(command[1])
            e = int(command[2])
            my_list.insert(i, e)
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif cmd == "append":
            e = int(command[1])
            my_list.append(e)
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
