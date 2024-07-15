a = int(input("enter a: "))
b = int(input("enter b: "))

def add():
    import calc2 as dop
    #dop.golob_var()
    sum = a + b + dop.addition(dop.num1, dop.num2)
    print("sum = ", sum)
    return sum

add()

# def sub():
#     #dop.golob_var()
#     minus = a + b - int(add())
#     print("minus = ", minus)

# sub()
