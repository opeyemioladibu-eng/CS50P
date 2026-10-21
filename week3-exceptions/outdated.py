monthlist = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]

while True:
    user_input = input("Date: ").strip()
    
    try:
        # Handle numeric format (MM/DD/YYYY)
        if "/" in user_input:
            month, day, year = user_input.split("/")
            
        # Handle text format (September 8, 1636)
        elif "," in user_input:
            # Split by comma first to ensure it exists
            date_part, year = user_input.split(",")
            # Split the month and day by the space
            parts = date_part.strip().split(" ")
            
            if parts[0] in monthlist:
                month = monthlist.index(parts[0]) + 1
                day = parts[1]
                year = year.strip()
            else:
                raise ValueError
        else:
            # If it has no '/' and no ',', it's an invalid format
            raise ValueError

        # Validation & Formatting
        m, d, y = int(month), int(day), int(year)
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02d}-{d:02d}")
            break
        else:
            raise ValueError
            
    except (ValueError, IndexError):
        pass
