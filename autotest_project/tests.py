pro = [0, 1, 2]


def get_build():
    build_id = {}
    v = []
    for a in range(1, 4):
        v.append(a)
        for i in pro:
            # print(i)
            build_id[i] = v
    return build_id


def get_unit():
    build_id = {0: [1, 2, 3], 1: [4, 5, 6]}
    b_id = list(build_id.values())
    print(b_id)
    unit_id = {}


b = get_build()
print(b)
# print(b.values())
# lis = list(b.values())
# print(lis[0])

u = get_unit()
