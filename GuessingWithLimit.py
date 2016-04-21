from math import pi
spaces = "                                                           "
spaces2 = "                                                                      "
print ("%sShapes available to compute: Triangle, Square, Rectangle, Circle" %spaces)
def multiplier(counter,number,retain,shape):
    return number if counter == 1 else multiplier(counter-1, number+retain, retain, shape)

def square():
    print "%s------Enter dimensions of the square------" % spaces
    side = (raw_input("%sEnter side: " % spaces2))
    if side.isdigit():
        area = multiplier(int(side), int(side), int(side), "square")
        return area
    else:
        return square()
def rectangle():
    print "%s------Enter dimensions of the rectangle------" % spaces
    length, width = raw_input("%sEnter length: " % spaces2), raw_input("%sEnter width: " % spaces2)
    if length.isdigit() and width.isdigit():
        area = multiplier(int(length), int(width), int(width), "rectangle")
        return area
    else:
        return rectangle()
def circle():
    print "%s------Enter dimensions of the circle------" % spaces
    radius = raw_input("%sEnter radius: " % spaces2)
    if radius.isdigit():
        area = multiplier(int(radius), int(radius), int(radius), "circle")
        area1 = multiplier(area, pi, pi, "circle")
        return area1
    else:
        return circle()
def triangle():
    print "%s------Enter dimensions of the triangle------" % spaces
    base, height = raw_input("%sEnter base: " % spaces2), raw_input("%sEnter height: " % spaces2)
    if base.isdigit() and height.isdigit():
        area = multiplier(multiplier(int(base), int(height), int(height), "triangle"), .5, .5, "triangle")
        return area
    else:
        return triangle()

list_of_area = [square(), rectangle(), circle(), triangle()]
highest = max(list_of_area)
if highest == list_of_area[0]:
    highest_shape = "SQUARE"
elif highest == list_of_area[1]:
    highest_shape = "RECTANGLE"
elif highest == list_of_area[2]:
    highest_shape = "CIRCLE"
else:
    highest_shape = "TRIANGLE"
guess = (raw_input("%sEnter guess: " % spaces2).upper())
def guessing(count,highest,guess):
    if count > 1:
        guess2 = (raw_input("%sWRONG ANSWER, TRY AGAIN\n%s(You have one more try): " % (spaces2, spaces2)).upper())
        guessing(count-1, highest, guess2)
        return guess2
if highest_shape != guess:
    result = guessing(2, highest_shape, guess)
    if result == highest_shape:
        print "%sYOU WON!" % spaces2
    else:
        print "%sYOU LOSE! THE CORRECT ANSWER IS %s!" % (spaces, highest_shape)
else:
    print "%sYOU WIN THE GAME! CONGRATS!" % spaces2