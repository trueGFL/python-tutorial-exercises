xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
loopnum = 0
a = 1
x = a


for x in xs :
    loopnum = loopnum + 1
    total = total + x
    a = a * x
    product = total * x
    print ("Valeur #", loopnum, ":", x)

    
    
print ("Total :", total)
print ("Product :", a)
