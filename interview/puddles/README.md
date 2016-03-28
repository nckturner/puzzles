PUDDLES

```


|                                |
|                     __ __      |
|                    |  |  |__   |
|      __            |  |  |  |  |
|     |  |         __|  |  |  |  |
|     |  |      __|  |  |  |  |  |
|   __|  |   __|  |  |  |  |  |  |
|  |  |  |__|  |  |  |  |  |  |  |
|__|__|__|__|__|__|__|__|__|__|__|
    2  5  1  2  3  4  7  7  6
```


In this picture we have walls of different heights. This picture is represented by an array of integers, where the value at each index is the height of the wall. The picture above is represented with an array as [2,5,1,2,3,4,7,7,6].

Now imagine it rains. How much water is going to be accumulated in puddles between walls?


PUDDLES 2.0

Same as the first question, but use a 2d array to create a 3d height map.  Where do the puddles form?  What is the volume of water that accumulates?

e.g. 

[ 4, 5, 6, 4, 5 ]
[ 4, 2, 2, 4, 5 ]
[ 5, 1, 5, 3, 5 ]
[ 2, 4, 6, 5, 7 ]
[ 2, 4, 6, 7, 9 ]


  .  .  .  .  . 
  .  x  x  .  . 
  .  x  .  x  . 
  .  .  .  .  . 
  .  .  .  .  . 


Make the output pretty.
