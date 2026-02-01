# **Python Automation**
Documentation on Python Automation

**[⇐ Python Automation](./README.md)**

## Debugging

Debugging is like being a detective for your code, finding and fixing errors. Python offers tools like exception handling to catch errors, assertions to check assumptions, and logging to track what your program does, making it easier to spot issues. 

### Exception Handling 

Use try-except blocks to handle errors gracefully. 
```python
try: 
    result = 10 / 0 
except ZeroDivisionError: 
    print("Error: Division by zero") 
```
### Assertions 
Assertions check if a condition is true, raising an `AssertionError` if false. 
```py
assert 2 + 2 == 4, "Math is broken!" 
```
### Logging 

The logging module records events at different levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). 
```python
import logging 

logging.basicConfig(level=logging.DEBUG) 
logging.debug("This is a debug message") 
logging.info("This is an info message") 
logging.warning("This is a warning message") 
logging.error("This is an error message") 
logging.critical("This is a critical message") 
```

### Mini-Project: Robust File Processor 

#### **Reason**
File operations can fail due to missing files or permissions. This script handles such errors and logs them, ensuring robust automation. 

```python
import os 
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

def process_file(file_path): 
    if not os.path.exists(file_path): 
        logging.error(f"File does not exist: {file_path}") 
        return 

    try: 
        with open(file_path, 'r') as f: 
            content = f.read() 

            # Process the content, e.g., count words 
            word_count = len(content.split()) 
            logging.info(f"Processed {file_path}: {word_count} words") 
    except Exception as e: 
        logging.error(f"Error processing {file_path}: {e}") 

# Example usage 
process_file('existing.txt') 
process_file('nonexistent.txt') 
```

#### **Explanation**

This script checks if a file exists, reads it, counts words, and logs the result. Errors are caught and logged, preventing crashes.