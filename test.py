"""Let's test with our eyes!"""

import itertools
from asciicells import AsciiCells


L = [['a', 'b']]
ac = AsciiCells()
t = ac.render(L)
print(t)


L = ['a'], ['b']
ac = AsciiCells()
t = ac.render(L)
print(t)



L = ['1', 'a', 'b'], ['2', 'C\tN', 'U\tS']
ac = AsciiCells()
t = ac.render(L)
print(t)


L = list(itertools.permutations(['7', 'ascii', 'this is a test'], 3))
ac = AsciiCells()
t = ac.render(L)
print(t)


L = ([
        'it must be indeed-continuously available',
        'In 2011, millions of people began to use the China Railways '
            'website on a daily basis and the system began experiencing '
            'problems with performance.',
        'Extra',  # missing an element here
    ],
    [
        'his team performed a root cause',
        'the old system: the relational database was overloaded and '
            'could not handle either the scale of incoming requests or '
            'the level of reliability.',
        'Python',
        '-'
])
t = ac.render(L)
print(t)
