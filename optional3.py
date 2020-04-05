def solve_math(math_expr,num1,num2,num3,num4,num5):

    a = isinstance(math_expr, str)
    print("is this a string?",a)
    b = isinstance(num1, int)
    print("is this an integer?", b)
    c = isinstance(num2, int)
    print("is this an integer?", c)
    d = isinstance(num3, int)
    print("is this an integer?", d)
    e = isinstance(num4, int)
    print("is this an integer?", e)
    f = isinstance(num5, int)
    print("is this an integer?", f)


solve_math("x*x-x/x+x",1,2,3,4,5)