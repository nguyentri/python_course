result=[]
for i in range (500, 600):
    if (i%7 == 0) and ((i%8)!=0):
        result.append(str(i))
print (",".join(result))
