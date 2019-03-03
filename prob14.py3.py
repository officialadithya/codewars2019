term1 = input()
term2 = input()
ListFib = []
ListFib.append(term1)
ListFib.append(term2)
x = 1
repeat = int(input())
while repeat > 2:
    repeat -= 1
    ListFib.append(str(int(ListFib[x]) + int(ListFib[x - 1])))
    x += 1
print(','.join(ListFib))