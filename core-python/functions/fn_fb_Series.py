def fb_series(num):
    a,b=0,1
    for i in range(num):
        print(a)
        a,b=b,a+b
fb_series(5)
fb_series(7)