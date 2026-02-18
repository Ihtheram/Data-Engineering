'Debugging.py'

# 'Exception Handling'
# try:
#     result = 10/5
#     print('\n10 ÷ 5 =', result,'\n\n')
# except ZeroDivisionError:
#     print("\nError: Division by zero\n\n")

# 'Assertion'
# assert 2 + 2 == 5, "math is broken"

# 'Logging'
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

"""
Mini Project
File operations can fail due to missing files or permissions. 
Create a script that handles such errors and logs them, ensuring robust automation.
"""
import os 
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

os.chdir(os.path.dirname(__file__)) # Changes the current working directory to this file's path

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
process_file('example_write.txt') 
process_file('nonexistent.txt') 