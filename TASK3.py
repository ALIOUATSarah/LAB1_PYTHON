
#ask the user for input 
W=float(input("enter the width "))
H=float(input("enter the height"))
D=float(input("enter the depth"))
#compute the area
area=2*W*H+2*W*D+2*H*D
#compute the volume
volume=W*H*D
#display the results for the user
print("the area of this parallelogram is: ",area,"\nthe volume of this parallelogram is :",volume)