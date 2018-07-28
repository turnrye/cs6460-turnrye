## Background information

```
experience
I code for work sometimes                             6
I work as a developer                                31
I'm working towards a career that includes coding     1
Name: experience, dtype: int64
formal_study
No      8
Yes    30
Name: formal_study, dtype: int64
js_experience
I prefer to use JavaScript     5
I've used it extensively      17
I've used it some             16
Name: js_experience, dtype: int64
rn_familiarity
I use it most days                                   5
I've done a few projects with it                     9
I've looked at it, but not really worked with it    18
I've worked on a single project in it                6
Name: rn_familiarity, dtype: int64
```

## Favorite Tools

```
best_tool
0    9
1    7
2    1
3    6
4    6
5    6
6    2
7    1
Name: best_tool, dtype: int64
```

### Chi Square

```
(13.368421052631579, 0.0636246995347717)
```

## Tool Usage

```
stack_overflow              33
blog                        28
microblog                    9
online_class                16
book                         8
peer_discussion             17
hackathon                    2
professional_workshop        4
university_class             6
documentation               28
reference_implementation    18
source_code                  1
chat                         2
dtype: int64
```

### Total sample count

```
172
```

### Chi Square

```
(110.06976744186046, 5.796915649593724e-18)
```

## Satisfaction by Tool

```
           needs_satisfied
best_tool                 
0                 3.888889
1                 4.000000
2                 4.000000
3                 3.500000
4                 3.833333
5                 3.500000
6                 4.000000
7                 3.000000
```

### Kruskal Wallis test

```
(2.1087732250523046, 0.7157607653056588)
```

## Completion by Tool

```
best_tool
0    [0, 1, 0, 0, 0, 0, 0, 0, 0]
1          [1, 1, 1, 1, 1, 1, 0]
3             [0, 0, 1, 0, 1, 0]
4             [1, 0, 0, 0, 1, 0]
5             [0, 1, 0, 1, 0, 1]
Name: completed_learning_unit, dtype: object
```

### Kruskal Wallis test

```
(9.30697278911566, 0.0538682526778574)
```

## Completion vs Non Completion by Tool

```
           Didn't Complete Unit  Completed Unit
best_tool                                      
0                             8               1
1                             1               6
3                             4               2
4                             4               2
5                             3               3
```

## Learning in Response to Change

```
No     25
Yes    13
Name: was_learning_in_response_to_change, dtype: int64
```


## How Soon Was It Used

```
Immediately                                   21
It was within a day or so                      6
I haven't used it yet                          4
I was already using it, but I learned more     4
Many days later                                3
Name: how_soon_was_it_used, dtype: int64
```

## User Satisfaction

```
0     5
1     3
2     5
3     3
4     5
5     4
6     4
7     2
8     3
9     4
10    5
11    3
12    3
13    4
14    4
15    4
16    4
17    4
18    3
19    3
20    5
21    2
22    4
23    4
24    3
25    4
26    4
27    4
28    4
29    4
30    5
31    4
32    3
33    5
34    4
35    2
36    4
37    3
Name: needs_satisfied, dtype: int64
```

