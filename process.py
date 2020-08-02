

def RenderTable():
    file = open("data.txt",'r')

    lines = file.readlines()
    data = {}
    for  x  in lines:
        key,val = x.split()
        data[key] = val 

    return data
