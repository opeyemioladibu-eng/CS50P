def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    for index, char in enumerate(s):
        if char.isdigit():
            if char == "0":
                return False
            if not s[index:].isdigit():
                return False
            
            break
    return True
        
    
    
main()