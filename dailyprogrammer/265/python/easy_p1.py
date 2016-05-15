import math,copy

def nthPermutationOfM(n,m):
    perms = recursive_permutations([x for x in range(m)]) 
    return perms[n]

def recursive_permutations(alist):
    if len(alist) == 2:
        return [[alist[0],alist[1]],[alist[1],alist[0]]]
    l = []
    for i,x in enumerate(alist):
        sub = copy.deepcopy(alist)
        sub.remove(x) 
        perms = recursive_permutations(sub)
        for j,p in enumerate(perms):
            perms[j].insert(0,x)
            l.append(perms[j])
    return l

def nthCombinationOfM(x,y,z):
    combs = recursive_combinations(y, [x for x in range(z)])
    return combs[x]

def recursive_combinations(n, alist):
    if n == 1:
        return alist
    l = []
    for i,x in enumerate(alist):
        if i+1 >= len(alist):
            continue
        combs = recursive_combinations(n-1, alist[i+1:])
        for j,r in enumerate(combs): 
            if not isinstance(combs[j], list):
                l.append([x, combs[j]])
            else:
                combs[j].insert(0,x)
                l.append(combs[j])
    return l

if __name__ == "__main__":
    
    print(recursive_permutations([0,1,2,"tree"]))
    n = 500
    m = 6
    nth = nthPermutationOfM(n,m)
    print("The {0} permutation of {1} is {2}".format(n,m,nth))

    print(recursive_combinations(2, [1,2,3,4]))
    x = 12
    y = 3
    z = 15
    nth = nthCombinationOfM(x,y,z)
    print("The {0} combination of {1} out of {2} is {3}".format(x,y,z,nth))


    print("\n\n")
    print(recursive_combinations(3, [1,2,3,4,5,6,7]))
