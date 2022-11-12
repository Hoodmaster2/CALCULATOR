'''
use "+","-","×","÷","/" \n for doing your calculation'''


num1= int (input ("enter first number: "))
sign=(input ("enter the operation type : "))
num2=int(input ("enter second number: "))
if sign == "+":
  print (num1 + num2)
elif sign == "-":
  print(num1 - num2)
elif sign == "*":
  print (num1 * num2)
elif sign == "×":
  print (num1*num2)
elif sign == "÷":
  print (num1/num2)
elif sign == "/":
    print (num1/num2)
else:
  print ("error")
  print ("thank for using my programme\n hope you enjoyed it")