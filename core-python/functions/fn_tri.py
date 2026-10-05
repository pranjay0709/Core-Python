def tri(num):
    for i in range(num, 0, -1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

tri(5)