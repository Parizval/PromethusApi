import uuid 


field_map = {}
value_map = {}

def RenderTable():
    file = open("data.txt",'r')
    
    global field_map 
    global value_map 

    lines = file.readlines()
    data = {}
    counter = 0 
    for  x  in lines:

        key,val = x.split()
        number = uuid.uuid4()        
        
        data[counter] = {"field":key,"value":val,"id":number}

        field_map[number] = key 
        value_map[number] = val 
        
        counter +=1

    return data

RenderTable()
