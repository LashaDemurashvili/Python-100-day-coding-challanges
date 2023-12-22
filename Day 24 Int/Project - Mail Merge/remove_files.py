import os

# Specify the directory where your text files are located
directory_path = "./Output/ReadyToSend"

# Loop through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
