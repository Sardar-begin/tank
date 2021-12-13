s = input()

def remove_dublicates(duplist):
    m = []
    x = []
    for i in duplist:
        if i in x:
            x.append(i)
        else:
            x = []
            x.append(i)
        m.append(x)
    return m
print(remove_dublicates(s))            


            
#     return m
# print(remove_dublicates(s))