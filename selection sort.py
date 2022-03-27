def selection_sort(lst):
    for i in range(len(lst)):
        min=lst[i]
        for j in range(i+1,len(lst)):
                if lst[j]<lst[i]:
                    lst[j],lst[i]=lst[i],lst[j]
    print(lst)

selection_sort([1,4,2,5,6,1,9,-2,-5,7])