# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # The variable inside the square brackets should be 'key' instead of 'k'

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd\'oh!',      # There was a back slash '\' missing after the character 'd' to be able to take the apostrophe as part of the value.
                         "maggie": "(Pacifier Suck)"
                         }

print() # This just adds an extra line in the terminal to make the output cleaner
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # This function was trying to send more than 2 arguments because the square brackets were missing.


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

