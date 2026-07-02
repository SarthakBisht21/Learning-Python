# method 1:
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))

print("Values before swap are:\nA = ",a,"\nB = ",b)

c=a+b
a=c-a
b=c-a

print("Values after swap are:\nA = ",a,"\nB = ",b)

# method 2:
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))

print("Values before swap are:\nA = ",a,"\nB = ",b)

temp=a
a=b
b=temp

print("Values after swap are:\nA = ",a,"\nB = ",b)

# method 3:
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))

print("Values before swap are:\nA = ",a,"\nB = ",b)

a , b = b , a

print("Values after swap are:\nA = ",a,"\nB = ",b)