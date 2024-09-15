def all_thing_is_obj(object: any) -> int:
    listType = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }
    typeObj = type(object)
    typeCurrent = listType.get(typeObj,None)
    
    if typeObj is str:
        print(f"{object} is in the kitchen : {typeCurrent}")
    elif typeCurrent == None:
        print("Type not found")
    else :
        print(f"{typeCurrent} is in the kitchen : {typeObj}")
    return 42