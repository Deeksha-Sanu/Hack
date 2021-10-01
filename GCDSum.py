import math
 # Gcd(x,y), where y is the sum of all digits of the number x
 
testcase=int(input())
while testcase!=0:
    gcd=0
    num=int(input())
    while gcd==0:
        suma=0G
        for i in str(num):
            suma=suma+int(i)
        gc=math.gcd(num,suma)
        if gc<=1:
            num=num+1 
        elif gc>1:
            print(num)
            gcd=1 
    
    testcase=testcase-1