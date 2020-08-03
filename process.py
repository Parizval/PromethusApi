

def RenderTable():
    file = open("data.txt",'r')

    lines = file.readlines()
    data = {}
    counter = 0 
    for  x  in lines:
        key,val = x.split()
        data[counter] = {"field":key,"value":val} 
        counter +=1 
    return data
