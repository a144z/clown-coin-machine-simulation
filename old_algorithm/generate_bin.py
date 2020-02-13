solution3=[5,4,4,4,3,3,3,3,4,4,6,6,2,2,2,2,5,5,6,5,5,3,3,3,6,6,6,6,1,7,8,1,5,5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,6,6,7,5,5,5,5,4,7,6,6,6,8,1,1,1,5,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,6,6,5,5,5,5,4,4,6,6,6,6,2,2,8,2,5,5,5,5,5,4,4,4,5,5,5,5,3,3,3,3,6,6,5,5,5,5,5,5,7,6,6,6,8,7,8,9]
for i in range(128):
    x=i
    array=""
    while x>=2:
        remain=int(x%2)
        x=int((x-remain)/2)
        array=str(remain)+array
    array=str(x)+array
    while len(array)<7:
        array="0"+array
    counter=0
    for each in array:
        if each=="1":
            counter+=1
    if counter==1:
        print(solution3[i])
        #print("{"+array+"}")
