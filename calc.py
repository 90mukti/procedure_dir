# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))

a = -30
b = -20

def addition():
#    c = int(input("enter c: "))
    # c = 70
    # add = a + b + c
    # print("addition:", add)
    global a
    #return c
    a = 40


def substraction():

    # sub = a - b
    global a
    a=50
    
    #sub = a - b -c

    # print("substraction:", sub)
substraction()
addition()

print(a+b)


#a = int(input("Enter a: "))
#b = int(input("Enter b: "))

#def addition():
    #c = int(input("Enter c: "))
    #add = a + b + c
    #print("Addition result:", add)
    #return c

#def subtraction(c):
   # sub = a - b - c
   # print("Subtraction result:", sub)

# Call addition and capture the return value
#c = addition()
# Pass the captured value to subtraction
#subtraction(c)