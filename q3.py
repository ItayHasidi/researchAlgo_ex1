from pydoc import locate


def print_sorted(lst):
    types = {locate("list"), locate("tuple"), locate("set"), locate("dict")}
    types_sort = {locate("list"), locate("tuple"), locate("set")}
    if type(lst) not in types:
        print(lst)
    else:
        for item in lst:
            if type(lst[item]) in types_sort:
                lst[item].sort()
            elif type(lst[item]) == locate("dict"):
                lst[item] = sorted(lst[item].items())
                # print(sorted(lst[item].items()))
        lst = sorted(lst.items())
        print(lst)


if __name__ == '__main__':
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print_sorted(x)  # prints e.g. {"a":5, "b":[1,2,3,4], "c":6}
