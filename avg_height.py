data = input("enter height seperated by comma: ")
count=0
sum=0.0
numbers = data.split(",")
for i in numbers :
    height = float(i.strip())
    count += 1
    sum += height

avg=sum/count
print(f"the average of height is {avg}")
print(f"rounded off to closest integer : {round(avg)}")



