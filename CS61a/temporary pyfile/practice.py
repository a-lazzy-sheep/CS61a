def compu1(x):
    return x
def compu2(x):
    return x*x*x
def compu3(x):
    return 8/((4*x-3)*(4*x-1))
def general(n,k,compu):
    assert n>0 and k>0 ,'n and k must be positive'
    sum=0
    for value in range(k,n+1):
        sum+=compu(value)
    return sum
