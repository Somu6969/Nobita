
print("hello sir")
def calculator():
    x=float(input("x="))
    sym=input("")
    y=float(input("y="))

    a=(x+y)
    b=(x-y)
    c=(x*y)
    d=(x/y)
    e=(x%y)

    if sym == "+":
       print(a)
    elif sym == "-":
       print(b)
    elif sym == "*":
       print(c)
    elif sym == "/":
       print(d)
    elif sym == "%":
       print(e)



calculator()
next_calculation = input("let's do some another one?(yes or no:)")

while next_calculation == "yes":
      calculator()
next_calculation = input("let's do some another one?(yes or no:)")
next_calculation = next_calculation.lower()
if next_calculation == "no":
    print("Thanks for using our system!")
next_calculation = input("let's do some another one?(yes or No:)")
next_calculation = next_calculation.lower()
if next_calculation == "No":
    print("Thanks for using our services!")
  #x,y,sym are the parameters.
  #a,b,c,d,e are the arguments.
  #print(a,b,c,d,e) are the local variables.
  #print(a,b,c,d,e) are the global variables.
  