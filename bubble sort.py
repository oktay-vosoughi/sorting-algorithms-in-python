from turtle import st


def bubblesort(lst):
    for i in range(len(lst)-1):
        print('i',lst[i])
        for j in range(len(lst)-i-1):
            print('j',lst[j])
            if lst[j]>lst[j+1]:
                print('j+1',lst[j+1])
                lst[j],lst[j+1]=lst[j+1],lst[j]
                print('j',lst[j],'j+1',lst[j+1])
            else:
                print('else','j',lst[j],'j+1',lst[j+1])

    print(lst)
bubblesort([2,1,4,6,3])