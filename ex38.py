ten_things = "Apples Oranges Crows Telephone Light SUgar"

print("Wait there are not ten things in the list. Lets fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day","Night", "Song","Frisbee","Corn","Banana","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding ",next_one)
    stuff.append(next_one)
    print("There are ", len(stuff)," items now.")

print('There we go ', stuff)

print("Lets do somethings with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:6]))
print(stuff)
