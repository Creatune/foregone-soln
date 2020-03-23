count = 0
while(True):
    N = input('Enter prize value: ')
    N = int(N)
    if(N%2 == 0):
        A = int(N/2)
    else:
        A = round(N/2)
    B = N - A
    lstA = [int(k) for k in str(A)]
    lstB = [int(j) for j in str(B)]
    count += 1
    for i in lstA:
        if(i != 4):
            for p in lstB:
                if(p != 4):
                    print('case #{}: {} {}'.format(count, A, B))
                    break
        else:
            for p in lstB:
                if(p != 4):
                    A += 1
                    B = N - A
                    print('case #{}: {} {}'.format(count, A, B))


        break
