# empty string return false
# any numerical value other than 0 is considered true
# any string/char that is not empty (including spaces) is considered true
# "if 2-3:" will return true as it is a number that is not 0
# "if 2-2:" will return false as it is 0

x=0
if x:
    print("True statement")
else:
    print("False statement")
# "if True" will return the first one, "if False" would return the second one
# "if x:" will return false because x is 0, but if it is any other number, it will return true
    
if True<False:
    print("Greater")
else:
    print("Less")

a=" "
if True == a:
    print("First option")
else:
    print("Second option")
