height = int(input())
i = height
numBlocks = 0
while i > 1:
    numBlocks += (i * i)
    i -= 1
numBlocks += 1
print(numBlocks)
