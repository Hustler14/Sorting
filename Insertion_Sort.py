#sorting in ascending order
a = [1,6,8,0,3,9,7,4,2,5]
pos = 0
for i in range(0,len(a)):               #ith element is to be compared with all elements before
    for j in range(0,i):                #j elements are to left of i which are to be checked for insertion of ith element
        if a[i]<=a[j]:
            pos = j                     #postion the ith element is to be inserted
            elem = a[i]                 #store the ith element before removing from the list
            a.pop(i)                    #pop the ith element 
            a.insert(pos,elem)          #insert ith element at the right position
print(a)
