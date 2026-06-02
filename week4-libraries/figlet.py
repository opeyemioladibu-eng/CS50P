import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
available_fonts = figlet.getFonts()


# len(sys.argv) is 1 means just the filename was provided (0 extra argument)
if len(sys.argv) == 1:
    font_choice = random.choice(available_fonts)
    
    
# len(sys.argv) is 3 means the filename and 2 extra arguments were provided
elif len(sys.argv) == 3:
    flag = sys.argv[1]
    font_name = sys.argv[2]
    

    #check if flag is correct and the font actually exists
    if flag in["-f", "--font"] and font_name in available_fonts:
        font_choice = font_name
    else:
        sys.exit("Invalid Usage")
        
        
# any other configuration is incorrect
else:
    sys.exit("Invalid Usage")


figlet.setFont(font = font_choice)
user_input = input("Text:")
print('Output:')
print(figlet.renderText(user_input))