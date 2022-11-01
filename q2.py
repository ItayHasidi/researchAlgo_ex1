from typing import Any


def four_neighbor_function(node: Any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def breadth_first_search(start, end, neighbor_function):
    if start == end:
        return 0
    p = []
    q = [start]
    while len(q) > 0:
        v = q.pop(0)
        p.append(v)
        for n in neighbor_function(v):
            if n == end:
                p.append(n)
                end_path = [n]
                last_v = n
                while len(p) > 0:
                    temp_v = p.pop(len(p) - 1)
                    if temp_v in neighbor_function(last_v):
                        end_path.insert(0, temp_v)
                        last_v = temp_v
                return end_path
            if n not in q:
                q.append(n)
    return False


if __name__ == '__main__':
    print(breadth_first_search(start=(0, 0), end=(2, 2), neighbor_function=four_neighbor_function))
