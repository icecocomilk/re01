
a=[1,2,3,4,5]
"""
for i in range(5):
    #print(i)
    m=input()
    a.append(m)
print(a)
"""
m=int(a[0])
n=int(a[0])
for i in range(1,5):
   
    if m < int(a[i]):
        m=int(a[i])
        print(i)
    if n > int(a[i]):
        n=int(a[i])
        #print(i)    
print(m)
print(n)

a.remove(m)
a.remove(n)
print(a)

    


