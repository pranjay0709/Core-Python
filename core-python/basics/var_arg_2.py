def sum(a,**varg):
    'varg is variable argument **varg used for dictionary'
    sum=a
    for val in varg.values():
        sum+=val
    return sum
s=sum(10,b=20,c=99,d=33)
print(s)