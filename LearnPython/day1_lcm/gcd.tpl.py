@@gcd@@

def __my_gcd__(a, b):
    if b == 0:
        return a
    return __my_gcd__(b,a%b)

def __test_gcd__(a,b):
    mine = __my_gcd__(a,b)
    theirs = gcd(a,b)
    if mine != theirs:
        return "gcd(%i, %i) returned %i, but it should have returned %i" % (a, b, theirs, mine)
    else:
    	return None
   
for i in range(0, 1000):
    for j in range(0, 1000):
        ret = __test_gcd__(i, j)
        if ret is not None:
            print ret
            exit(0)
print 'OK'