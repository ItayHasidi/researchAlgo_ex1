from pydoc import locate
list_type = locate("list")
tuple_type = locate("tuple")
set_type = locate("set")
dict_type = locate("dict")
types = {list_type, tuple_type, set_type, dict_type}


def rec_sort(data):
    """
    Gets any kind of data and converts whatever is not a dataset into string.
    All datasets are also turned into strings (deep iterative).
    Afterwards sorts and returns.
    """
    if type(data) == list_type:
        new_data: list = []
        for item in data:
            if type(item) in types:
                item = rec_sort(item)
            else:
                item = str(item)
            new_data.append(item)
        data = new_data
        data.sort()

    elif type(data) == tuple_type or type(data) == set_type or type(data) == dict_type:
        if type(data) == tuple_type or type(data) == set_type:
            new_data: list = []
            for item in data:
                if type(item) in types:
                    item = rec_sort(item)
                else:
                    item = str(item)
                new_data.append(item)
            new_data.sort()
            if type(data) == tuple_type:
                data = tuple(new_data)
            else:
                data = list(new_data)

        else:
            new_lst: dict = {}
            for item_key in data:
                if type(data[item_key]) in types:
                    data[item_key] = rec_sort(data[item_key])
                # else:
                item_val = data[item_key]
                item_key = str(item_key)
                new_lst[item_key] = item_val
            # print(new_lst)
            # data = dict(new_lst)
            data = dict(sorted(new_lst.items()))

    return data


def print_sorted(lst):
    print(rec_sort(lst))


if __name__ == '__main__':
    x = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print_sorted(x)  # prints e.g. {"a":5, "b":[1,2,3,4], "c":6}
    x = {"a": 5, 1: 6, "b": [1, 3, 2, 4], 0: "a", "2": {"b", "c", 1, 0, -1, "A"}}
    print_sorted(x)  # prints e.g. {"a":5, "b":[1,2,3,4], "c":6}
