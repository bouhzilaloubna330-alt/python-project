num1 = float(int(input("first number = ")))
num2 = float(int(input("secend number = ")))
op = input (" chose the operation(+,-,*,/):")

if op =="+":
         print("resolt",num1+num2)       
elif op == "-":
        print("resolt",num1-num2)
elif op == "*":
        print("resolt",num1*num2) 
elif op =="/":
        if num2!=0:
          print("resolt",num1/num2)

        print("error: cannot divide by zero")  
else:
  print("invailed operation")                        
        
