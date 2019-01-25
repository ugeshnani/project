import sys
a=str(input("Enter the series : "))
l=0
b=0
front_dict={}
back_dict={}
front_list=[]
back_list=[]
i=0
count=0
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
max_y=max(front_dict.values())
min_y=min(back_dict.values())
if min_y >0 :
    min_y=0
highest_point=[]

for i in back_dict.keys() :
       if back_dict[i] == max_y :
                highest_point.append([i,max_y])

for value in front_dict.values():
	if value == max_y:
		count=count+1
print(count)

l=l+count
highest_point.sort(key=lambda x: x[0],reverse=True)


print(highest_point)
for j in range(len(highest_point)) :
        for i in range(l-1,0,-1) :
                if i >= highest_point[j][0] :
                        if i in front_dict :
                                front_dict[i+1]=front_dict.pop(i)
                        if i in back_dict :
                                back_dict[i+1]=back_dict.pop(i)
                else :
                        break
highest_point=[]

for i in back_dict.keys() :
       if back_dict[i] == max_y :
                highest_point.append([i,max_y])



less_co=[]
greater_co=[]
front_co=[]
straight_co=[]
back_co=[]
zero_co=[]
for i in highest_point :
        less_co.append(i[0]-2)
        greater_co.append(i[0])
        front_co.append(i[0]-2)
        straight_co.append(i[0]-1)
        back_co.append(i[0])
        zero_co.append(i[0]-1)

for j in range(l) :
        if j in zero_co :
                sys.stdout.write("0")
        else :
                sys.stdout.write(" ")
sys.stdout.write("\n")
for j in range(l) :
        if j in front_co :
                sys.stdout.write("/")
        elif j in straight_co :
                sys.stdout.write("|")
        elif j in back_co :
                sys.stdout.write("\\")
        else :
                sys.stdout.write(" ")
sys.stdout.write("\n")
for k in range(l) :
        if k in less_co :
                sys.stdout.write("<")
        elif k in greater_co :
                sys.stdout.write(">")
        else :
                sys.stdout.write(" ")

sys.stdout.write("\n")
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
                                      
