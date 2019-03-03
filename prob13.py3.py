numerator1 = input()
denominator1 = input()
numerator2 = input()
denominator2 = input()

x = 0

if numerator1 == "X":
    denominator1 = float(denominator1)
    numerator2 = float(numerator2)
    denominator2 = float(denominator2)
    numerator1 = 1
    x = 1
elif denominator1 == "X":
    numerator1 = float(numerator1)
    numerator2 = float(numerator2)
    denominator2 = float(denominator2)
    denominator1 = 1
    x = 2
elif numerator2 == "X":
    numerator1 = float(numerator1)
    denominator1 = float(denominator1)
    denominator2 = float(denominator2)
    numerator2 = 1
    x = 3
elif denominator2 == "X":
    numerator1 = float(numerator1)
    numerator2 = float(numerator2)
    denominator1 = float(denominator1)
    denominator2 = 1
    x = 4



leftside = numerator1*denominator2
rightside = numerator2*denominator1

leftside = float(leftside)
numerator1 = float(numerator1)
denominator2 = float(denominator2)
denominator1 = float(denominator1)


if x == 1:
    print(rightside/denominator2)
elif x == 2:
    print(leftside/numerator2)
elif x == 3:
    print(leftside/denominator1)
elif x == 4:
    print(rightside/numerator1)