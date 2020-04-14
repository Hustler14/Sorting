a = [1,6,8,0,3,9,7,4,2,5]
for i in range(0,len(a)):
    mini = a[i]
    pos = i
    for j in range(i,len(a)):
        if a[j]<=mini:
            mini = a[j]
            pos = j
    dummy = a[i]
    a[i] = mini
    a[pos] = dummy
print(a)
