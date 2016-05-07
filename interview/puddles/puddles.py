from timeit import default_timer as timer

# Test heights: 

#heights = [7, 3, 2, 5, 3, 4, 7, 2, 1 ]
# vol: 18

#heights = [2,1,4,2,2,5,2,2,4,4,1,2]
# vol: 10

heights = [5,1,3,1,4,1,3,1,2,1,4]
# vol: 19


""" A puddle in constructed in this program
with a tuple:
(left_index, left_height, right_index, right_height)
where the left pair represents the left lip of the 
puddle and the right pair represents the right lip. 
E.g. (1,2,3,1) could represent:
  _
 | |  _
_| |_| |___
0 1 2 3 4 5
"""


""" Find the previous location with equal or
greater height, or if there is none, find the 
previous highest peak.  If there is neither, 
then we are on the first peak.  The lip is 
described with the tuple (location, height).
"""
def find_left_lip(peaks, ri, rh):
    max_height = 0
    max_index = 0
    for i,h in reversed(peaks):
        if h >= rh:
            return i,h
        else:
            if h > max_height:
                max_height = h
                max_index = i
    return max_index, max_height


def add_puddle(puddles, to_add):
    print("               Add puddle to: {0}".format(puddles))
    to_remove = []
    ai,ah,bi,bh = to_add
    for i,p in enumerate(puddles): 
        li,lh,ri,rh = p
        print("               Finding subsets: {0} <= {1} and {2} <= {3}".format(ai,li,ri,bi))
        if ai <= li and ri <= bi:
            # puddle to add surrounds a puddle already in list, mark to remove
            to_remove.append(p)
    print("               To remove: ",to_remove)
    for r in to_remove:
        print("               Removing: ",to_remove)
        deleted = puddles.remove(r)
        print("               Deleted {0} in favor of {1}".format(r, to_add))
    puddles.append(to_add)

def water_level(puddle):
    _,lh,_,rh = puddle
    return min(lh,rh)

def puddle_volume(heights):
    previ = 0
    prevh = 0
    left_lip = 0
    uphill = True
    peaks = []
    puddles = []
    total_vol = 0
    found_first = False
    debug_str = ""

    heights.append(0)
    heights.insert(0,0)

    for h in heights:
        print("{0}".format(h), end=" ")
    print("")
    for i,h in enumerate(heights): 
        print("{0:3}   {2:3}, peaks: {1}".format(i, peaks, h))
        if uphill:
            if h >= prevh:
                pass
            elif h < prevh: 
                print("        /\\")
                if found_first: 
                    li, lh = find_left_lip(peaks,previ,prevh)  
                    puddle = (li, lh, previ, prevh) 
                    add_puddle(puddles, puddle)
                    print("\n               - The left lip of this peak is index: {0}, height: {1}".format(li, lh))
                peaks.append((previ,prevh))
                uphill = False
                found_first = True
        else: 
            if h > prevh:
                uphill = True
            if h <= prevh:
                pass

        prevh = h
        previ = i

    print("\nSumming puddle volumes")
    for p in puddles:
        li,lh,ri,rh = p
        for i in range(li+1,ri):
            total_vol += water_level(p) - heights[i]
            print("Vol: ",total_vol)

    print("\nRun finished")
    print("Puddles: ", puddles)
    print("Total Volume: ", total_vol,"\n")


if __name__ == "__main__":
    start = timer()
    puddle_volume(heights)
    end = timer()
    print(end - start) 
