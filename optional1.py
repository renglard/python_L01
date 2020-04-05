height = input("please enter a number of rows: ")

def is_integer(height):
    if height.isdecimal() != True:
        print("that's not a valid height")
        exit()

def make_int(height):
    return int(height)



def greater_than_zero(height):
    if height < 1:
        print("number needs to be greater than 0")
        exit()

def build_pyramid(height):
    is_integer(height)
    height = make_int(height)
    print(type(height))
    greater_than_zero(height)

    for i in range(0, height):
        for x in range(0,height-i-1):
            print(end=" ")
        for x in range(0,i+1):
            print("*", end=" ")
        print()

build_pyramid(height)

