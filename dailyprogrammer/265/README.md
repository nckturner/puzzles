# Challenge #265 [Easy] Permutations and combinations part 1

Permutations

The "permutations of 3" for the sake of this text are the possible arrangements of the list of first 3 numbers (0 based but optional) in sorted order
0 1 2
0 2 1
1 0 2
1 2 0
2 0 1
2 1 0
The permutation number is the index in this list. The "3rd permutation of 3" is 1 0 2. "1 2 0 has permutation number 3 (0 based)"
input:
what is 240th permutation of 6
what is 3240th permutation of 7
output:
1 5 4 3 2 0
4 2 6 5 3 1 0
combinations

The "combinations of 3 out of 6" is the sorted list of the possible ways to take 3 items out of the first 6 numbers (as a set where order does not matter)
0 1 2
0 1 3
0 1 4
0 1 5
0 2 3
0 2 4
0 2 5
0 3 4
0 3 5
0 4 5
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
The "3rd combination number of 3 out of 6 is 0 1 4". "0 2 4 is combination index/number 5 or the 6th combination of 3 out of 6"
input:
24th combination of 3 out of 8
112th combination of 4 out of 9
output
1 2 5
3 4 5 6
Brute force solutions (generate full list, then take the number/index) to all of today's challenges are encouraged.

# Challenge #265 [Easy] Permutations and combinations part 2

Basically the same challenge as Monday's, but with much larger numbers and so code that must find permutation and combination numbers without generating the full list.
permutation number

https://en.wikipedia.org/wiki/Factorial_number_system is the traditional technique used to solve this, but a very similar recursive approach can calculate how many permutation indexes were skipped in order to set the next position.
input:
what is the 12345678901234 permutation index of 42-length list
output:
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 35 32 36 34 39 29 27 33 26 37 40 30 31 41 28 38
input2:
what is the permutation number of:  25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 35 32 36 34 39 29 27 33 26 37 40 30 31 41 28 38
output:
836313165329095177704251551336018791641145678901234
combination number

https://en.wikipedia.org/wiki/Combinatorial_number_system and https://msdn.microsoft.com/en-us/library/aa289166%28VS.71%29.aspx show the theory.
It may also be useful to know that the number of combinations of 4 out of 10 that start with 0 1 2 3 4 5 6 are (in J notation ! is out of operator)
   3 ! 9 8 7 6 5 4 3 
84 56 35 20 10 4 1
with the last combination 6 7 8 9 (84 combinations for 4 out of 10 start with 0, 56 start with 1...)
input: (find the combination number)
0 1 2 88 from 4 out of 100
output:
85
challenge input: (find the combination number)
0 1 2 88 111 from 5 out of 120
15 25 35 45 55 65 85 from 7 out of 100
challenge input 2
what is the 123456789 combination index for 5 out of 100
bonus:
how many combinations from 30 out of 100 start with 10 30 40
bonus2: write a function that compresses a sorted list of numbers based on its lowest and highest values. Should return: low, high, count, combination number.
example list:
15 25 35 45 55 65 85
output with missing combination number (x):
15 85 7 x


# Challenge #265 [Hard] Permutations with repeat

 The number of permutations of a list that includes repeats is `(factorial of list length) / (product of factorials of each items repeat frequency)
for the list 0 0 1 2 the permutations in order are

0 0 1 2
0 0 2 1
0 1 0 2
0 1 2 0
0 2 0 1
0 2 1 0
1 0 0 2
1 0 2 0
1 2 0 0
2 0 0 1
2 0 1 0
2 1 0 0

1. Calculate permutation number of list that may include repeats

The permutation number is similar to Monday and Wednesday's challenge. But only wednesday's approach of calculating it without generating the full list will work (fast) for the longer inputs. The input varies from previous ones in that you are provided a list rather than a number to account for possible repeats. If there are no repeats, then the answer is the same as the part 2 (wednesday) challenge.
input:
5 4 3 2 1 0
2 1 0 0
5 0 1 2 5 0 1 2 0 0 1 1 5 4 3 2 1 0
8 8 8 8 8 8 8 8 8 7 7 7 6 5 0 1 2 5 0 1 2 0 0 1 1 5 4 3 2 1 0 6 7 8
output: (0 based indexes)
719
11
10577286119
3269605362042919527837624

2. retrieve list from permutation number and sorted list

input is in format: permutation_number, sorted list to permute
output format is above part 1 input rows.
input:
 719, 0 1 2 3 4 5  
 11, 0 0 1 2
 10577286119, 0 0 0 0 0 1 1 1 1 1 2 2 2 3 4 5 5 5
 3269605362042919527837624, 0 0 0 0 0 1 1 1 1 1 2 2 2 3 4 5 5 5 6 6 7 7 7 7 8 8 8 8 8 8 8 8 8 8

3. bonus

use the above function and wednesday's combination number (optional) to compress/encode a list into a fixed set of numbers (with enough information to decode it)
input:
hello, heely owler world!
You might wish to convert to ascii, then calculate the combination number for the unique ascii codes, then calculate the permutation number with each letter replaced by contiguous indexes.<Paste>
