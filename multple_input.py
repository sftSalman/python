if __name__ == '__main__':
    N = int(input())

lst = []

for i in range(0, N):
    s = input().split()
    if s[0] == "append":
        lst.append(int(s[1]))
    elif s[0] == "insert":
        lst.insert(int(s[1]), int(s[2]))
    elif s[0] == "remove":
        lst.remove(int(s[1]))
    elif s[0] == "pop":
        lst.pop()
    elif s[0] == "index":
        lst.index(int(s[1]))
    elif s[0] == "count":
        lst.count(int(s[1]))
    elif s[0] == "sort":
        lst.sort()
    elif s[0] == "reverse":
        lst.reverse()
    elif s[0] == "print":
        print(lst)
