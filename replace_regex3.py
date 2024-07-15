import re  # Importing the regular expressions library

text = "a brown fox jumped over a white dog and they played happily"  # The original text string

pattern = [r"brown", r"white"]  # A list of regex patterns to be replaced
replace = ["red", "black"]  # A list of replacement strings corresponding to the patterns

def multi_replace(text, patterns, replacements):  # Function definition with clearer variable names
    for pattern, replacement in zip(patterns, replacements):  # Loop through pairs of patterns and replacements
        text = re.sub(pattern, replacement, text)  # Replace pattern with replacement in the text
    return text  # Return the modified text after all replacements

new_text = multi_replace(text, pattern, replace)  # Call the function and store the result

print("original text:", text)  # Print the original text
print("modified:", new_text)  # Print the modified text
