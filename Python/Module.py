def sum(num1,num2):
    return num1+num2

def main():
    name=" Mr. Motubhai Soni"
    print("Hi I belive you're {} ?".format(name))
    Name=input("If not, what is your name, pal? ")
    age=input("And your age is? ")
    print("Awesome {} !!! You're {} years old 😃 😃 😃".format(Name,age))
    a=int(input("\nEnter number 1: "))
    b=int(input("Enter number 2: "))
    print("Sum is {}".format(sum(a,b)))

if __name__=="__main__":
    main()