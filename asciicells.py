from collections import defaultdict
import itertools


CROSS = '+'
HORIZ = '-'
VERTI = '|'

def get_width_info(L):
    info = defaultdict(int)
    for row in L:
        for item, i in zip(row, itertools.count()):
            if len(item) > info[i]:
                info[i] = len(item)
    info['width'] = sum(info.values()) + len(info) * 3 + 1
    return info


def get_table(L):
    info_w = get_width_info(L)
    width = info_w['width']

    rows = []
    for item_list in L:
        token = VERTI
        for item, i in zip(item_list, itertools.count()):
            padding = ' ' * (info_w[i] - len(item))
            token += ' {}{} {}'.format(item, padding, VERTI)
        rows.append(token)
    cross_indexes = set([])
    for c, i in zip(rows[0], itertools.count()):
        if c == VERTI:
            cross_indexes.add(i)
    border = ''
    for i in range(width):
        if i in cross_indexes:
            border += CROSS
        else:
            border += HORIZ
    rows.insert(0, border)
    rows.append(border)
    return '\n'.join(rows)


if __name__ == '__main__':
    L = list(itertools.permutations(['1', 'ascii', 'this is a test'], 3))
    print(get_table(L))
