k = [str(x) for x in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
v = [bin(x)[2:].zfill(4) for x in range(16)]
hash_table = dict(zip(k, v))


def hex_to_binary(hex_seq):
    bin_seq = ""
    for h in hex_seq:
        bin_seq += hash_table[h]
    return bin_seq


tc = int(input())
for i in range(tc):
    _, hex_seq = input().strip().split(" ")
    print("#{0} {1}".format(i+1, hex_to_binary(hex_seq)))