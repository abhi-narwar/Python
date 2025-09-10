n, m = map(int, input().split())

# Top part
for i in range(1, n, 2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)

# Middle part
print("WELCOME".center(m, "-"))

# Bottom part
for i in range(n-2, 0, -2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)
