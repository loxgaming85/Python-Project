print("""
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVID""")

a = int(input("Enter Your first Number :- "))
b = int(input("Enter Your Second Number :- "))
c = input("ENTER YOUR OPRATION + , - , * , / :- ")

if c=="+":
    print("Your Answer is :- ",a+b)
elif c=="-":
    print("Your Answer is :-",a-b)
elif c=="*":
    print("Your Answer is :-",a*b)
elif c=="/":
    print("Your Answer is :- ",a/b)
else:
    print("Invailed Input\nPLEASE ENTER + , - , * , /")