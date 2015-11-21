"""
A Simple ASCII Table Generator.

>>> import asciicells
>>> ac = asciicells.AsciiCells()
>>> L = [['a', 'b'], ['1', '2']]
>>> print(ac.render(L))
+---+---+
| a | b |
|   |   |
| 1 | 2 |
+---+---+

More usage: https://github.com/mitnk/asciicells
By mitnk (w@mitnk.com) under MIT License
"""

import argparse
import csv
import itertools
import os.path
import re
from collections import defaultdict


CROSS = '+'
HORIZ = '-'
VERTI = '|'
MAX_TABLE_WIDTH = 72
MIN_CELL_WIDTH = 12


class AsciiCells(object):
    def __init__(self, header=False):
        self.header = header
        self.orphans = defaultdict(str)

    def get_width_info(self, L):
        count_max = 0
        info = defaultdict(int)
        for row in L:
            for item, i in zip(row, itertools.count()):
                if '\t' in item:
                    item = re.sub('\t', '    ', item)
                if i + 1 > count_max:
                    count_max = i + 1
                if len(item) > info[i]:
                    info[i] = len(item)

        for row in L:  # align columns in all rows
            span = count_max - len(row)
            if span > 0:
                row.append(' ')

        width_extra = len(info) * 3 + 1
        table_width = sum(info.values()) + width_extra
        if table_width > MAX_TABLE_WIDTH:
            table_width = MAX_TABLE_WIDTH

        index_to_wrap = itertools.count()
        while sum(info.values()) > table_width - width_extra:
            index = next(index_to_wrap) % len(L[0])
            if info[index] <= MIN_CELL_WIDTH:
                continue
            info[index] -= 1

        info['width'] = table_width
        return info

    def _get_empty_row(self, token, char=' '):
        empty_row = re.sub(r'[^{}]'.format(VERTI), char, token)
        if char != ' ':
            empty_row = re.sub(r'[{}]'.format(VERTI), CROSS, empty_row)
        return empty_row

    def _hard_split(self, column, width, word_break=False):
        if word_break:
            return column[:width-1] + '-', column[width-1:]
        return column[:width], column[width:]

    def _split_column_str(self, column, width):
        if ' ' not in column.strip():
            return self._hard_split(column, width)
        index_split = 0
        for i in range(len(column)):
            if i > width:
                break
            if column[i] == ' ':
                index_split = i
        if index_split == 0:
            return self._hard_split(column, width, word_break=True)
        return column[:index_split], column[index_split:]

    def _get_normal_row(self, item_list, width_info):
        token = VERTI
        if isinstance(item_list, defaultdict):
            item_list = [item_list[i] for i in range(len(item_list))]
        for item, i in zip(item_list, itertools.count()):
            if '\t' in item:
                item = re.sub('\t', '    ', item)
            item = item.strip()
            width = width_info[i]
            if len(item) > width:
                padding = ''
                str_curr, str_remaining = self._split_column_str(item, width)
                str_curr = str_curr.strip()
                if len(str_curr) < width:
                    str_curr += ' ' * (width - len(str_curr))
                self.orphans[i] = str_remaining
            else:
                padding = ' ' * (width_info[i] - len(item))
                if item.startswith(' '):
                    str_curr = item[1:] + ' '
                else:
                    str_curr = item
                self.orphans[i] = ''
            token += ' {}{} {}'.format(str_curr, padding, VERTI)
        return token

    def _are_orphans_left(self):
        for k in self.orphans:
            if len(self.orphans[k]) > 0:
                return True
        return False

    def render(self, L):
        info_w = self.get_width_info(L)
        width = info_w['width']

        rows = []
        for item_list, i in zip(L, itertools.count()):
            token = self._get_normal_row(item_list, info_w)
            rows.append(token)
            while self._are_orphans_left():
                token = self._get_normal_row(self.orphans, info_w)
                rows.append(token)
            if self.header and i == 0:
                rows.append(self._get_empty_row(token, char='-'))
            else:
                rows.append(self._get_empty_row(token))

        # pop out the last empty row
        rows.pop()

        # add top and bottom borders
        border = ''
        cross_indexes = set([])
        for c, i in zip(rows[0], itertools.count()):
            if c == VERTI:
                cross_indexes.add(i)
        for i in range(width):
            if i in cross_indexes:
                border += CROSS
            else:
                border += HORIZ
        rows.insert(0, border)
        rows.append(border)

        return '\n'.join(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True,
                        help='CSV file to render')
    parser.add_argument('-H', '--header', action='store_true',
                        help='Render first row as header')
    parser.add_argument('-t', '--tsv', action='store_true',
                        help='using TSV format instead of CSV')
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print('No such file: {}'.format(args.file))
        exit(1)

    L = []
    with open(args.file) as f:
        delimiter = '\t' if args.tsv else ','
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            L.append(row)

    ac = AsciiCells(header=args.header)
    t = ac.render(L)
    print(t)


if __name__ == '__main__':
    main()
