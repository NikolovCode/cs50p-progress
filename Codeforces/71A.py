n = int(input(""))
result = []
while n > 0:
    w = input("")
    first, last = w[0] ,w[-1]
    if len(w) > 10:
        result.append(f"{first}{len(w)-2}{last}")
    else:
        result.append(w)
    n -= 1
for res in result:
    print(res)    
