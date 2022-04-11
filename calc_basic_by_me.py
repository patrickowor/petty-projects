print("**********************************")
print("**********************************")
print("complex calculator by Patrick owor")
print("**********************************")
print("**********************************")
print("enter the first number and press enter")
firstno =int(input())
print("**********************************")
print("**********************************")
print("enter your operator")
print("a for addition ")
print("s for subtraction ")
print("d for division ")
print("m for multiplication ")
print("p for power")
print("now plz pick an operator ")
print("**********************************")
print("**********************************")
op=str(input())
print("**********************************")
print("**********************************")
a="a"
s="s"
d="d"
m="m"
p="p"
print("enter the second number and press enter ")
secno = int(input())
add = firstno+secno
sub = firstno-secno
div = firstno/secno
mul= firstno*secno
pot= firstno**secno
print("**********************************")
print("**********************************")
if op== a or op == s or op == d or op == m or op==p:
           if op==a:
                   print("your answer is = ")
                   print(add)
           elif op==s:
                    print("your answer is = ")
                    print(sub)
           elif op==d:
                     print("your answer is = ")
                     print(div)
           elif op==m:
                     print("your answer is = ")
                     print(mul)
           else:
                     print("your answer is = ")
                     print(pot)
else:
           print("sorry wrong operation one of your numbers or the operator happens to be wrong redo this operation ")
print("**********************************")
print("**********************************")
