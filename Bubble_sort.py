#Sorting in Ascending order.
a = [1,6,8,0,3,9,7,4,2,5]
for i in range(0,len(a)): 
    for j in range(0,len(a)-i-1):                       #largest number gets bubbled to the right
        if a[j+1]<=a[j]:                                #check adjacent numbers and swap them based on requirement
            dummy = a[j]
            a[j] = a[j+1]
            a[j+1] = dummy
print(a)
