def sum_01(a, *varg):
    'varg is variable argument *varg represent tuples'
    sum=a
    for value in varg:
        sum+=value
    return sum
s=sum_01(10,5,6,74,4)
print(s)

# def sumnum( a, *varg ):
#    t = a
#    print(t)
#    for i in varg:
#       print("t = ", t, "i = ", i)
#       t+=i
#    return t;
#
# total = sumnum(2,2,3,4,5)
# print('Total', total)