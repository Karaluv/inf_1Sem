

max = int(input("enter length of sequence"))


def n_increase(x0,x1,current,max):

    x0,x1 = x1,x0+x1
    
    print(x1)

    if current<max:
        current += 1
        n_increase(x0,x1,current,max)
    
print("0")
print("1")
n_increase(0,1,0,max-1)
