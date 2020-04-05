while True:

    input1 = str(input("please enter something: "))


    def is_parsable(a):
        if a == int or a.isdecimal() == True or a.replace('.', '', 1).isdecimal() == True:
            print("is digit")
            return True
        else:
            print("not parsable")
            return False


    is_parsable(input1)
