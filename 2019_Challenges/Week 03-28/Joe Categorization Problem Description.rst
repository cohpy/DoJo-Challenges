
**********************
Categorization Problem
**********************

Proposed by Joe Friedrich

Problem Description
===================

Given a a table with four fields -- ID, Category, Type and Value -- print a
report with Category down the side, Type across the top and the contents are
the values in the appropriate location in the resulting grid.

Sample Table 1

===  =========  =====  =====
ID   Category   Type   Value
===  =========  =====  =====
1    1          A      2
2    3          D      5
3    4          B      7
4    2          C      8
5    4          D      9
6    4          C      1
7    1          D      3
8    3          C      9
9    1          A      5
10   3          A      4
11   1          B      6
12   4          A      2
13   2          D      6
14   3          B      3
15   2          B      8
16   1          C      0
===  =========  =====  =====

Sample Report 1

+----------+-----+-----+-----+-----+
| Category |  A  |  B  |  C  |  D  |
+==========+=====+=====+=====+=====+
|        1 |  5  |  6  |  0  |  3  |
+----------+-----+-----+-----+-----+
|        2 |  5  |  8  |  8  |  6  |
+----------+-----+-----+-----+-----+
|        3 |  4  |  3  |  9  |  5  |
+----------+-----+-----+-----+-----+
|        4 |  2  |  7  |  1  |  9  |
+----------+-----+-----+-----+-----+
