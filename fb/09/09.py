#!/usr/bin/python3

import time

start = time.time()
arr = [0, 4, 7, 1, 5, 8, -1, 4, 2, -5, 2, 24, 57, 23, 45, 65, 45, 23, 3, 67, 3, 4, 54, -3, 45, 67, 23, 45, 56, 34, 56, 67, 78, 34, 2, 23, -42, -4, -5, -6, -7, 23, 234, 765, 123, -345, -343, -465, 0, 4, 7, 1, 5, 8, -1, 4, 2, -5, 2, 24, 57, 23, 45, 65, 45, 23, 3, 67, 3, 4, 54, -3, 45, 67, 23, 45, 56, 34, 56, 67, 78, 34, 2, 23, -42, -4, -5, -6, -7, 23, 234, 765, 123, -345, -343, -465]
s = 0
count = 0
arr = sorted(arr)


if __name__ == "__main__":
    for i,x in enumerate(arr):
        for j,y in enumerate(arr): 
            if j == i:
                continue
            for k,z in enumerate(arr): 
                if k == j or k == i:
                    continue
                if x + y + z == s: 
                    count += 1
                elif x + y + z > s:  #optimization yaaaaa
                    break
end = time.time()
print(end - start)
print(count)
