
code_book = {
    '3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
    '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9
}


def decode(line):
    stack, encrypted_code = [], []
    cur = line[0]
    count, valid_sum = 0, 0

    for c in line:
        if c == cur:
            count += 1
        else:
            stack.append(str(count))
            cur = c
            count = 1
    else:
        stack.append(str(count))

    for i in range(0, len(stack), 4):
        encrypted_code.append(code_book[''.join(stack[i:i+4])])

    for i, v in enumerate(encrypted_code):
        if not i % 2:
            valid_sum += v*3
        else:
            valid_sum += v

    if not valid_sum % 10:
        return sum(encrypted_code)
    else:
        return 0


def find_code(line):
    result = -1
    for e, l in enumerate(reversed(line)):
        if int(l) == 1:
            result = decode(line[-e-56:-e])
            break
    return result


code = int(input().strip())
for i in range(code):
    c, r = map(int, input().split())
    answer = None
    for _ in range(c):
        if answer:
            input()
        else:
            temp = find_code(input())
            if temp >= 0:
                answer = temp
    print("#{0} {1}".format(i+1, answer))
