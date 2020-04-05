

def check_integer(a):
    if type(a) != int:
        print("please input an integer")
        exit()


def is_even(a):
    check_integer(a)
    if a % 2 == 0:
        print("true")
        return True
    else:
        print("false")
        return False


is_even(2)
is_even(3)
is_even("cat")


