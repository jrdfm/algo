import random
import math

def selectkth(A,l,r,kwish):
    # Find the pseudomedian.
    pmed = mom(A[l:r+1])
    # Find the index of the pseudomedian
    pmedi = 0
    while A[pmedi] != pmed:
        pmedi = pmedi + 1
    # Swap that entry with the final entry.
    A[r],A[pmedi] = A[pmedi],A[r]
    # Partition on the final entry.
    pivotindex = partition(A,l,r)
    if kwish < pivotindex+1:
        return(selectkth(A,l,pivotindex-1,kwish))
    elif kwish > pivotindex+1:
        return(selectkth(A,pivotindex+1,r,kwish))
    else:
        return(A[pivotindex])

def partition(A,l,r):
    pivot = A[r]
    t = l
    for i in range(l,r):
        if A[i] <= pivot:
            A[t],A[i] = A[i],A[t]
            t = t + 1
    temp = A[t]
    A[t] = A[r]
    A[r] = temp
    return t

def mom(A):
    # Make a copy because we're going to mess it up doing our grouped sorting.
    AA = A[:]
    n = len(AA)
    medlist = []
    for i in range(0,int(math.ceil(float(n)/5))):
        Li = 5*i
        Ri = Li + 5
        if Ri > n-1:
            Ri = n-1
        AA[Li:Ri] = sorted(AA[Li:Ri])
        medlist.append(AA[Li+(Ri-Li-1)//2])
    if len(medlist)==1:
        return medlist[0]
    return(selectkth(medlist,0,len(medlist)-1,(len(medlist)+1)//2))

LIST = []
while len(LIST) < 20:
    r = random.randint(0,100)
    if r not in LIST:
        LIST.append(r)

print('Array: '+str(LIST))
kwish = random.randint(1,len(LIST))
kth = selectkth(LIST,0,len(LIST)-1,kwish)
print("I'm looking for rank: " + str(kwish))
print('It is: ' + str(kth))
print('Here is the Python sorted array for checking:')
LIST.sort()
print(LIST)
if LIST[kwish-1] == kth:
    print('Success!')
