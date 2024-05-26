import math as m

A = 0
B = 0

A = int(input("Please input A: "))
B = int(input("Please input B: "))

#Count = int(0)
KeepGoing = True

while(KeepGoing != False):
    #print("A is not zero: ", A, " B is not zero: ", B)
    #Count += 1
    
    if(A > B):
        Q = m.floor(A / B)
        R = A - B * Q
        A = B
        B = R

    if(B > A):
        Q = m.floor(B / A)
        R = B - A * Q
        B = A
        A = R
    
    if(int(A) == 0 or int(B) == 0):
        KeepGoing = False
    
    print(" Value for A: " + str(A), "Value for B: " + str(B))
    
print("Value for A: " + str(A), "Value for B: " + str(B))