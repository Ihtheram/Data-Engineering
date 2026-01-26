# Python Automation
Documentation on Python Automation

**[⇐ Data Engineering Fundamentals](./README.md)**

## Python File Manipulation
---

* Get current working directory
    - `os.getcwd()`
* Change current working directory
    - `os.chdir("target_directory_path")`

* Get this file's directory name
    - `os.path.dirname(__file__)`
* Get this file's name
    - `os.path.basename(__file__)`

* Check Presence of a File on Path or Directory
    - `os.path.exists("filepath"))`
* Check if an item is a directory
    - `os.path.isdir("item"))`
* Check if an item is a file
    - `os.path.isfile("item"))`
* Check if a file is of a specific type
    - `os.path.endswith(".extension"))`

* List all files and directories in the current directory
    - `os.listdir(".")`

* List all directories in the current directory
```py
    [item for item in os.listdir('.') if os.path.isdir(item)]
```

* List all files in the current directory
```py
    [item for item in os.listdir('.') if os.path.isfile(item)]
```

* List all files with a specific extension (e.g. txt)
```py
    [file for file in os.listdir('.') if file.endswith('.txt')]
```

* Read a file
```py
    with open("filepath",'r') as f:
        print(f.read())
```

* Creating a new directory
    - `os.mkdir("path")`

* Creating a new file
    - `open("filepath", 'w').close()`

* Writing to a file
```py
with open("filepath",'w') as f:
    f.write("Text")
```

* Appending to a file
```py
with open("filepath",'a') as f:
    f.write("Text")
```

* Renaming a directory or file
    - `os.rename("path", "new_name")`
* Copy a directory or file
    - `shutil.copy("path", "copypath")`
* Move a directory or file
    - `shutil.move("path", "movepath")`
* Deleting the created directory
    - `os.rmdir("path")`

* Deleting a file
    - `os.remove("filepath")`

* Deleting a directory with contents
    - `shutil.rmtree("directorypath", ignore_errors=True)`


---


