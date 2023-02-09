#This code capitalizes user input

#requesting input from user
print("Please type what you would like the computer to capitalize:")

#lable input
INP = input()

#returning input capitalized 
returning = "Here is what you asked the computer to capitalize: "


for CAP in INP:
  CAP = CAP.upper()
  returning += CAP
  
print(returning)
