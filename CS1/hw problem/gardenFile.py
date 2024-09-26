R = int(input("length of a row, in feet "))
E = int(input("thea amount of space, in feet, used by an end post assembly "))
S = int(input("amount of space between lines "))

v = (R - (2*E))/S

print( f"the number that will fit in each row is {int(v)}")

#length of a row, in feet 9
#thea amount of space, in feet, used by an end post assembly 9
#amount of space between lines 9
#the number that will fit in each row is -1