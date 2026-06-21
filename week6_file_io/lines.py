import sys


def main():
    """ Ensure exactly one command-line argument is passed"""
    if len(sys.argv) > 2:
        sys.exit("Too many arguments!")
    if len(sys.argv) < 2:
        sys.exit("Too few argument!")

    """ Check if it's a Python file"""
    file = sys.argv[1]
    if not file.endswith(".py"):
        sys.exit("Input a Python file only!")
        
    # Read the file and count lines of code
    try:
        with open(file, "r") as file:
            line_count = 0
            for line in file:
                """ Remove whitespace"""
                stripped_line = line.strip()
                
                
                """ Exclude blank lines and comment starting with """
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue
                
                line_count += 1
                
                
            print(line_count)
    
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
            