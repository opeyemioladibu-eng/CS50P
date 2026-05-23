monthlist = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


while True:
    #prompt user for a date
    user_input = input("Date[MM/DD/YY]: ")
    
    
    try:
        #handle numeric format (MM/DD/YY)
        if "/" in user_input:
            month, day, year = user_input.split("/")
            
        #Handle Text Format(September 8, 1636)
        else:
            #Remove comma and split by space
            parts = user_input.replace(",", "").split(" ")
            if parts[0] in monthlist:
                month = monthlist.index(parts[0]) + 1
                day, year = parts[1], parts[2]
            else:
                raise ValueError
            
        #Validation & Formatting
        m, d, y = int(month), int(day), int(year)
        if 1 <= m <= 12 and 1<= d <=31:
            print(f"{y}-{m:02d}-{d:02d}")
            break
        else:
            raise ValueError
        
        
    except (ValueError, IndexError):
        pass