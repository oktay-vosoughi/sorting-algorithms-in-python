def insertionsort(lst):
    for i in range(1,len(lst)):
        while lst[i-1]>lst[i]and i>0:
            lst[i-1],lst[i]=lst[i],lst[i-1]
            i-=1
    print(lst)
insertionsort([2,1,5,6,3])