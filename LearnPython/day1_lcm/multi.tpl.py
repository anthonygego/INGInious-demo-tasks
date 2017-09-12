def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

@@multi@@

def __my_gcd_multi__(a_list):
    current_gcd = a_list[0]
    for i in a_list:
        current_gcd = gcd(current_gcd, i)
    return current_gcd

def __test_gcd_multi__(a_list):
    mine = __my_gcd_multi__(a_list)
    theirs = gcd_multi(a_list)
    if mine != theirs:
        return "gcd_multi(%s) returned %i, but it should have returned %i" % (str(a_list), theirs, mine)
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
    ret = __test_gcd_multi__(test)
    if ret is not None:
        print ret
        exit(0)
print 'OK'