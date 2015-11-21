# ASCII Cells - Another ASCII Table Generator


## Targeted at Python3

This tool is based on latest Python3 (v3.5.0). It does support Python2.7,
but this is an accident.


## Install

```bash
$ sudo pip install asciicells
```

or

```bash
$ sudo python setup.py install
```


## High level usages

After installed, an executable `asciicells` would available for use.
If not, please replace following examples with `python -m asciicells`.

```
$ asciicells -f demo.csv

+-----+---------+-----------+
| No. | sample  | name      |
|     |         |           |
| 1   | a,b,c   | lettes    |
|     |         |           |
| 2   | + - x / | operators |
+-----+---------+-----------+
```

With header:

```
$ asciicells -f demo.csv -H

+-----+---------+-----------+
| No. | sample  | name      |
+-----+---------+-----------+
| 1   | a,b,c   | lettes    |
|     |         |           |
| 2   | + - x / | operators |
+-----+---------+-----------+
```

Also support TSV: `asciicells -f demo.tsv -t -H`


## Low level usages

```python
>>> import asciicells
>>> ac = asciicells.AsciiCells()
>>> L = [['a', 'b'], ['1', '2']]
>>> print(ac.render(L))
+---+---+
| a | b |
|   |   |
| 1 | 2 |
+---+---+
```

See [test.py](https://github.com/mitnk/asciicells/blob/master/test.py)
for more examples.


## Why another ASCII table generator?

When [needing an ASCII table](https://mitnk.com/unix/gdb/) generator,
I googled some but they neither cannot
[wrap long lines](https://ozh.github.io/ascii-tables/) in single table cell,
or [do not support quoted COMMAs](http://ascii.gallery/table) in csv file.
So I have to write my own version.

```
+--------------+----------------------------------------------+--------+
| it must be   | In 2011, millions of people began to use the | Extra  |
| indeed-cont- | China Railways website on a daily basis and  |        |
| inuously     | the system began experiencing problems with  |        |
| available    | performance.                                 |        |
|              |                                              |        |
| his team     | the old system: the relational database was  | Python |
| performed a  | overloaded and could not handle either the   |        |
| root cause   | scale of incoming requests or the level of   |        |
|              | reliability.                                 |        |
+--------------+----------------------------------------------+--------+
```


## Tests and Pull Request

This tool works as long as it generate neat tables. So yes, we have tests
by eyes: just run `python test.py` and check its outputs.

Following KISS, I consider this tool as feature completed. So only accept
PRs with bug fixes or code improvements.


## Author

mitnk (w@mitnk.com)


## License

[MIT](https://opensource.org/licenses/MIT) License
