import sys
a=input("Enter series :")
l=0
b=0
front_dict={}
back_dict={}
i=0
while i < len(a) :

    for j in range(int(a[i])) :
        front_dict[l]=b
        if j == int(a[i]) -1 :
            l=l+1
            b=b
        else :
            l=l+1
            b=b+1
    i=i+1
    if i == len(a) :
        break
    for j in range(int(a[i])) :
        back_dict[l]=b
        if j == int(a[i]) -1 :
            l=l+1
            b=b
        else :
            l=l+1
            b=b-1
    i=i+1
print(front_dict)
print(back_dict)
max_y=max(front_dict.values())
min_y=min(back_dict.values())
if min_y >0 :
    min_y=0
print(max_y)
print(min_y)

for i in range(max_y,min_y-1,-1) :
    for j in range(l) :
        if j in back_dict :
            if back_dict[j] == i :
                sys.stdout.write("\\")
            else :
                sys.stdout.write(" ")
                
        elif j in front_dict :
            if front_dict[j] == i :
                sys.stdout.write("/")
            else :
                sys.stdout.write(" ")
                
        else :
            sys.stdout.write(" ")

    sys.stdout.write("\n")
