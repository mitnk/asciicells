import re
from collections import defaultdict
import itertools


CROSS = '+'
HORIZ = '-'
VERTI = '|'
MAX_WIDTH = 72
MIN_CELL_WIDTH = 10

def get_width_info(L):
    info = defaultdict(int)
    for row in L:
        for item, i in zip(row, itertools.count()):
            if len(item) > info[i]:
                info[i] = len(item)
    width_extra = len(info) * 3 + 1
    info['width'] = sum(info.values()) + width_extra
    if info['width'] > MAX_WIDTH:
        info['width'] = MAX_WIDTH

    index_to_wrap = itertools.count()
    while sum([info[i] for i in range(len(L[0]))]) > info['width'] - width_extra:
        index = index_to_wrap.__next__() % len(L[0])
        if info[index] <= MIN_CELL_WIDTH:
            continue
        info[index] -= 1
    return info


def _get_empty_row(token):
    return re.sub(r'[^{}]'.format(VERTI), ' ', token)


def _split_column_str(column, width):
    return column[:width], column[width:]


def _get_normal_row(item_list, width_info, orphans):
    token = VERTI
    if isinstance(item_list, defaultdict):
        item_list = [item_list[i] for i in range(len(item_list))]
    for item, i in zip(item_list, itertools.count()):
        if len(item) > width_info[i]:
            padding = ''
            str_curr, str_left = _split_column_str(item, width_info[i])
            orphans[i] = str_left
        else:
            padding = ' ' * (width_info[i] - len(item))
            str_curr = item
            orphans[i] = ''
        token += ' {}{} {}'.format(str_curr, padding, VERTI)
    return token


def _are_orphans_left(orphans):
    for k in orphans:
        if len(orphans[k]) > 0:
            return True
    return False


def get_table(L):
    info_w = get_width_info(L)
    width = info_w['width']

    rows = []
    orphans = defaultdict(str)
    for item_list in L:
        token = _get_normal_row(item_list, info_w, orphans)
        rows.append(token)
        while _are_orphans_left(orphans):
            token = _get_normal_row(orphans, info_w, orphans)
            rows.append(token)
        rows.append(_get_empty_row(token))

    rows.pop()  # pop out the last empty row

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
    L1 = list(itertools.permutations(['1', 'ascii', 'this is a test'], 3))
    L2 = [
        [
            'it must be continuously available',
            'In 2011, millions of people began to use the China Railways '
                'website on a daily basis and the system began experiencing '
                'problems with performance.',
            'Extra',
            'N/A',
        ],
        [
            'his team performed a root cause',
            'the old system: the relational database was overloaded and '
                'could not handle either the scale of incoming requests or '
                'the level of reliability.',
            'Python',
            '-',
        ],
    ]
    print(get_table(L2))
