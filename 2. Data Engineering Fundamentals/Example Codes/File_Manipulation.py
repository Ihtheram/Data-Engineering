import os # Importing the os module for file and directory manipulation
import shutil # Importing shutil module for high-level file operations

# Get the name of this file
print("\nFile Name:", os.path.basename(__file__))

# Get the name of this folder
print("\nFolder Name:", os.path.dirname(__file__))

# Get the current working directory
print("\nCurrent Working Directory:", os.getcwd(), "\n")

# Change the current working directory to this file's path
os.chdir(os.path.dirname(__file__))

# Verify the change
print("\nCurrent Working Directory:", os.getcwd(), "\n")

# List all files and directories in the current working directory
print(os.listdir('.'))

# List all directories in the current directory
# for item in os.listdir('.'):
#     if os.path.isdir(item):
#         print("\nDirectory:", item)
# One-liner version
print("\nDirectories:")
items = [item for item in os.listdir('.') if os.path.isdir(item)]
for item in items: print(item)

#List all files in the current directory
# for item in os.listdir('.'):
#     if os.path.isfile(item):
#         print("\nFile:", item)
# One-liner version
print("\nFiles:")
items = [item for item in os.listdir('.') if os.path.isfile(item)]
for item in items: print(item)

# List all files with a specific extension (e.g., .txt)
# for item in os.listdir('.'):
#     if item.endswith('.txt'):
#         print("\nText File:", item)
# One-liner version
print("\nText Files:")
items = [item for item in os.listdir('.') if item.endswith('.txt')]
for item in items: print(item)




# Writing to a file
with open("./example_write.txt",'w') as f:
    f.write("This is an example of writing to a file.\n")
    f.write("File manipulation is essential in data engineering.\n")

# Reading a file
with open("./example_write.txt",'r') as f:
    print("\n", f.read(), "\n")

# Appending to a file
with open("./example_write.txt",'a') as f:
    f.write("Appending a new line to the file.\n")
# Reading the updated file
with open("./example_write.txt",'r') as f:
    print("\nUpdated file content:\n", f.read())



shutil.copy("./example_write.txt", "./copied_file.txt")
print("\nexample_write.txt has been copied to copied_file.txt.")
# Verify copying
print("\nCurrent files after copying:", os.listdir('.'))


# Renaming a file
os.rename("./copied_file.txt", "./renamed_file.txt")
print("\ncopied_file.txt has been renamed to renamed_file.txt.")  
# Verify renaming
print("\nCurrent files after renaming:", os.listdir('.'))

# Renaming a directory
os.rename("./new_directory", "./renamed_directory")

0# Creating a new directory
os.mkdir("./new_directory")
print("\nnew_directory has been created.")
# Verify directory creation
print("\nCurrent directories after creation:", os.listdir('.'))

# Creating a new file in the new directory without writing content
open("./new_directory/empty_file.txt", 'w').close()

# Moving a file into the new directory
shutil.move("./renamed_file.txt", "./new_directory/renamed_file.txt")
print("\nrenamed_file.txt has been moved to new_directory.")
# Verify moving the file
print("\nCurrent files in new_directory:", os.listdir('./new_directory'))

# Deleting a file
os.remove("./new_directory/renamed_file.txt")
print("\nrenamed_file.txt has been deleted.")

# Verify deletion
print("\nCurrent files after deletion:", os.listdir('.'))

# Deleting the created directory
os.rmdir("./new_directory")
print("\nnew_directory has been deleted.")
# Verify directory deletion
print("\nCurrent directories after deletion:", os.listdir('.'))

# Deleting a directory with contents
shutil.rmtree("./new_directory", ignore_errors=True)  # Just in case it still exists