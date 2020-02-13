data = open(r"C:\Users\gifte\Desktop\game\data_number.txt",'r')
x = data.readlines()
string=""
for line in x:
    for _ in line:
        if _ =="0":
            string+="a"
        elif _ =="1":
            string+="s"
        elif _ =="2":
            string+="d"
        elif _ =="3":
            string+="f"
        elif _ =="4":
            string+="g"
        elif _ =="5":
            string+="h"
        elif _ =="6":
            string+="j"
        elif _ =="7":
            string+="k"
print(string)

