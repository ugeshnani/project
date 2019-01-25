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
                                      
