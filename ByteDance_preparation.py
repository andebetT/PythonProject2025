#

def killkthbit(n,k):
    binary=list(bin(n)[2:])
    binary[-k]=0
    print(binary)
    joind="".join(binary)
    print(joind)



print(killkthbit(37,3))