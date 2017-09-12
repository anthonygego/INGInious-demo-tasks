def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

@@multi_multi@@

def __my_gcd_list__(a_list):
    current_gcd = a_list[0]
    retval = []
    for i in a_list:
        current_gcd = gcd(current_gcd, i)
        retval.append(current_gcd)
    return retval

def __test_gcd_list__(a_list):
    mine = __my_gcd_list__(a_list)
    theirs = gcd_list(a_list)
    if mine != theirs:
        return "gcd_list(%s) returned %s, but it should have returned %s" % (str(a_list), str(theirs), str(mine))
    else:
    	return None

tests = [
    [10, 12, 26, 89, 865, 234],
    [2, 4, 6, 8, 10],
    [6, 12, 18, 24, 32],
    [6, 12, 18, 24, 33],
    [1000, 2000, 3000, 4000, 4500]
]
for test in tests:
    ret = __test_gcd_list__(test)
    if ret is not None:
        print ret
        exit(0)
print 'OK'