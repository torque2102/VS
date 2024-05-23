exp = [2200,2350,2600,2130,2190]
print(exp[1]-exp[0])


print(exp[0]+exp[1]+exp[2])


for i in range(len(exp)):
    if [i]==2000:
        print("yes")
else:
    print("no")
    
    print(2000 in exp)
    
    
exp.insert(5,1900)

print(exp)


exp[3] = exp[3] - 200
print(exp)