import sys
import re
n=[]
a=input()




while True:
    
    ret=re.match(r"[0-9]*[0-9]$", a)
    if not ret:
        print("only number")
        a = (input())
    else:
        print(type(a))
        if (int(a)/12)>0:
            b=int(int(a)%12)
            a=(int(a)/12)
            n.append(b)
        else:        
        #        print(n)
            n.reverse()
        #        print(n)
            c=len(n)
            print(c)
            for i in range(0,c):
                if n[i]==10:
                    n[i]="A"
                elif n[i]==11:
                    n[i]="B"
                else:
                    pass
            print(n)
            break
