
def float_to_binary(f):
    dec = [2 ** x for x in range(-1, -13, -1)]
    result = ""
    for d in dec:
        if f >= d:
            f -= d
            result += '1'
        else:
            result += '0'
        if not f:
            return result
    return 'overflow'


tc = int(input())
for i in range(tc):
    f = float(input())
    print("#{0} {1}".format(i+1, float_to_binary(f)))