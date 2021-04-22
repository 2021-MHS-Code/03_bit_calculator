# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters 
    ends = decoration * 5
    
    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    return ""
    
# Main Routine goes here

# Heading
statement_generator("Bit Calcultor for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Ask the user for the file type
