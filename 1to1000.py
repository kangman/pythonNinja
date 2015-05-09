
f = open('numbers.txt', 'wb')
x = range(1000)
for i in x:
    y = str(x)
    f.write(y)

f.close()
