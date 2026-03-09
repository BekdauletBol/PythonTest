"""
// if i dont care about the order of the elements
    and i know that there're should be unique,then i use

    set will not save elements twice
    for example

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

in the output we dont see {1,2,3,4,3}

we see {1,2,3,4}
no element ever appears moe than once inside of set
SET


we can remove elements from set just use remove
e.g s.remove(3) and element 3 will remove from set

len will give us the length of a sequence

e.g print(len(s))

"""

# Create an empty set

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(3)

print(f"The set has {len(s)} elements")