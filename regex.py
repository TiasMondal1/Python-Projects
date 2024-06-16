import re

# Read the original file
with open('regex.txt', 'r') as file:
    data = file.read()

# Remove the '\t' character
cleaned_data = data.lstrip()
cleaned_data = re.sub(r"\t", '', data)

# Write the cleaned data to a new file
with open('output.txt', 'w') as file:
    file.write(cleaned_data)