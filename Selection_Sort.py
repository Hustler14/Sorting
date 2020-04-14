#sorting in ascending order
a = [1,6,8,0,3,9,7,4,2,5]
for i in range(0,len(a)): 
    mini = a[i]                         #set element in position i as minimum for the iteration. 
    pos = i                             #position.
    for j in range(i,len(a)):           #run loop from i to length(a)
        if a[j]<=mini:                  
            mini = a[j]                 #if jth element is lesser than minimum, update minimum and position.
            pos = j
    dummy = a[i]                        #swap ith element with minimum element using it position.
    a[i] = mini
    a[pos] = dummy
print(a)
