a=input("Enter Your Name :- ")
b=input("Enter Your Love Name :- ")

combine_string=a+b
lower_case=combine_string.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
true=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
love=l+o+v+e

love_score=int(str(love+true))

if love_score <10 or love_score >90:
 print(f"Your Score is {love_score} Your Love Like Coke and Mentos")
elif love_score >=40 and love_score <= 50:
 print(f"Your Score is {love_score} and You are alright Together")
else:
 print(f"Your Score is {love_score} ")