num = int(input())
li = [0, 0, 1, 1]

if num > 4:
    N = 4
    while N != num + 1:
        if N % 3 == 0:
            if N % 2 == 0:
                li.append(min(li[N - 1] + 1, li[N // 2] + 1, li[N // 3] + 1))
            else:
                li.append(min(li[N - 1] + 1, li[N // 3] + 1))
        elif N % 2 == 0:
            li.append(min(li[N - 1] + 1, li[N // 2] + 1))
        else:
            li.append(li[N - 1] + 1)
        N += 1

if num == 4:
    print(2)
else:
    print(li[num])