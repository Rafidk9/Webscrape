import os
# Specify the directory where your text files are located
directory_path = "C:\\Users\\Admin\\Desktop\\Webscrape"
text_files = []
for i in range(1,16):
    # Get a list of all text files in the directory
    for file in os.listdir(directory_path):
        if file.endswith(F'.txt{i}'):
            text_files.append(file)
# Initialize an empty list to store the content of each file
file_contents = []

# Read the content of each text file and store it in the list
for file_name in text_files:
    file_path = os.path.join(directory_path, file_name)
    try:
        with open(file_path, "r",encoding='utf-8') as file:
            lines = file.read()
            lines = [line.strip() for line in lines]
            file_contents.append(lines)
            print(f"Content of {file_name} successfully read and stored in an array.")
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping...")
print(text_files)
# print((file_contents)[0])
# print(''.join(file_contents[0][0]))
# Now you can iterate over the file_contents list using a for loop
for content in file_contents:
    print((content))
