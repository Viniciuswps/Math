from math import factorial

def taylor_series(x, n):
        e = 0
        if x >= 0:
                for i in range(n):
                        e += (x ** i) * 1.0 / factorial(i)
        return e


x = int(raw_input())
n = int(raw_input())

if x >= 0:
    print "1 forma: " + str(taylor_series(x,n))
else:
    print "1 forma: " + str(taylor_series(x,n))
    print "2 forma: " + str(1 / taylor_series(-x,n))
