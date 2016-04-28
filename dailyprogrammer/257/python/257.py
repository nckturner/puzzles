#!/usr/bin/python

years = range(1700,2050)
pairs = []
count = [0 for x in range(1700,2050)]
maximum = {"loc": 0, "val": 0, "year": 0}

def parse(line):
    chunks = line.split(",") 
    b = chunks[1].split(" ")
    d = chunks[3].split(" ")
    def eat_ws(arr): 
        try:
            while True:
                arr.remove('')
        except: 
            pass
    eat_ws(b)
    eat_ws(d)
    return b,d

if __name__ == "__main__":
    f = open("../presidents.csv", "r")
    for line in f:
        birth, death = parse(line)
        pairs.append((birth,death))
    for i,y in enumerate(years): 
        for p in pairs:
            birth = p[0]
            death = p[1]
            byear = 999999
            dyear = 0
            if len(birth) < 3:
                continue
            if len(death) < 3:
                death = None
            else:
                dyear = death[2]
            byear = birth[2]
            if int(byear) <= y <= int(dyear):
                count[i] += 1
                if count[i] > maximum["val"]:
                    maximum = {"loc": i, "val": count[i], "year": y}

    print("{0} Presidents were alive in the year {1}.".format(maximum["val"], maximum["year"]))
