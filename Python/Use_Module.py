from Module import *

print("Loop with negative step")
for i in range(11,1,-1):
    print("{:2d} ".format(i),end="\t")
print("\nThe sum is {:3d}".format(sum(10,20)))
fname=["Avinash"]
fname.append("Soni")
fname.append(input("\nEnter String to append: "))
print(fname)