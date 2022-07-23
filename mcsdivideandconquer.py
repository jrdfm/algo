import random

A = []
for i in range(0,10):
    A.append(random.randint(-10,10))
n = len(A)
print(A)

def mcs(A,l,r,indentlevel):
    print(indentlevel*'.' + 'Finding mcs in A='+str(A[l:r+1]))
    if l == r:
        print(indentlevel*'.' + 'It is '+str(A[l]))
        return(A[l])
    else:
        c = (l+r) // 2
        lhmax = A[c]
        lhsum = 0
        for i in range(c,l-1,-1):
            lhsum = lhsum + A[i]
            if lhsum > lhmax:
                lhmax = lhsum
        rhmax = A[c+1]
        rhsum = 0
        for i in range(c+1,r+1):
            rhsum = rhsum + A[i]
            if rhsum > rhmax:
                rhmax = rhsum
        cmax = lhmax + rhmax
        print(indentlevel*'.' + 'Straddle max is '+str(cmax))
        lmax = mcs(A,l,c,indentlevel+2)
        rmax = mcs(A,c+1,r,indentlevel+2)
        omax = max([lmax,rmax,cmax])
        print(indentlevel*'.' + 'It is '+str(omax))
        return(omax)

print(mcs(A,0,len(A)-1,0))
