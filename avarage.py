n =  int(input("Enter the number of students:"))
record = {}
for i in range(n):
    name = input("Enter name:")
    record[name] = name
    score = int(input('Enter the marks'))
    record[score]= score
print(record[name])