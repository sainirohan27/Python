days=int(input(" "))
months=int(days/30)
weeks=int((days-(months*30))/7)
day=days-(months*30)-(weeks*7)
print("M=",months)
print("W=",weeks)
print("D=",day)