def marks():
    li=[]
    for i in range (1,4):
        print("Enter Subject {} Marks: ".format(i),end="\t")
        li.append(int(input()))

    max=li[0]
    min=li[0]
    for i in li:
        if i>max:
            max=i
        if i<min:
            min=i

    print("Max: {}".format(max))
    print("Min: {}".format(min))

marks()