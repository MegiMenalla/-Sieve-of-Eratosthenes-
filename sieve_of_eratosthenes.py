from numpy import sqrt
def inicializo(A,n):
    for i in range(2,n+1):
        A.append(True)

def eratosthenes(n):
    if n<=1:
        print('Argumenti duhet ne jete me i madh se 1.')
    else:
        A=[]
        n=int(n)
        inicializo(A,n)
        for i in range(2,int(sqrt(n))):
            if A[i]==True:
                x=0
                j=i**2+i*x
                while j<n-1:
                    A[j]=False
                    x=x+1
                    j=i**2+i*x
    B=[]
    for tmp in range(2,len(A)):
        if A[tmp]==True:
            B.append(tmp)
    return B

print(eratosthenes(100))