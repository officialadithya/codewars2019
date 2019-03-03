inputList = []

inputList = input().split()

hours = inputList[0]

miles = inputList[1]

speed = inputList[2]

miles = int(miles)
hours = int(hours)
speed = int(speed)

if miles / speed <= hours:
    print(str(hours), str(miles), str(speed)+". I will make it!")
else:
    print(str(hours), str(miles), str(speed)+". I will be late!")