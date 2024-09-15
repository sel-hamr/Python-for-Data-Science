def NULL_not_found(object: any) -> int:
    status = 0
    listType = {
        float: "Cheese",
        int: "Zero",
        bool:"Fake",
        str:"Empty"
    }
    typeObj = type(object)
    currentType = listType.get(typeObj,"Nothing")
    if str != "" and typeObj is str:
        status = 1
        print("Type not Found")
    else :
        print(f"{currentType}: {object} {typeObj}")
    return status
            
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

    