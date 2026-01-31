# Python Automation
Documentation on Python Automation

**[⇐ Python Automation](./README.md)**
.
## Regular Expression

A sequence of characters that forms a pattern, used to find or replace specific string which matches with the pattern. For example, you can use regex to extract all email addresses from a document or check if a phone number is formatted correctly. It’s like a super-smart find-and-replace function. 

### RegEx Module
In Python, The `re` module handles regex 
```py
import re
```

### RegEx Functions

* **Compile**: Creates a regex object for reusable patterns and uses capturing groups surrounded by parentheses to capture parts of matches
    ```py
    regex = re.compile(r'pattern') 
    ```
    *The "r" in the beginning is making sure that the string is being treated as a "raw string"*

* **Search**: Searches the string for a match, and returns a Match object if there is a match
    ```py
    match = regex.search('string') 
    ```
    Or use directly with the `re` module
    ```py
    match = re.search('pattern', 'string')
    ```
    * **Group**: Used to get a group from the match object
        - Group 0, get the whole match
            ```py
            if match:
                grp0 = match.group(0) 
            ```
        - Group 1, 2, ... Get the first, second etc capturing groups sequentially
            ```py
                grp1 = match.group(1) 
                grp2 = match.group(2)
            ...
        - Groups: Get a list of all capturing groups
            ```py
                groups = match.groups() 
            ```
* **Find All**: Returns a list containing all matches
    - `regex.findall(string)` or `re.findall(pattern, string)`
* **Split**: Returns a list of strings extracted from a string that has been split at each match
    - `re.split(string)` or `re.split(pattern, string)`
* **Sub**: Replaces the matches with a new text
    - `re.sub(replacement, string, occurance_optional)` or `re.sub(pattern, replacement, string, occurance_optional)`


### Metacharacters

* `()`: **Capturing Group**, captures a group of characters exactly as specified in a pair of parentheses
* `[]`: **Character Set/Class** matches any of the specified set of characters specified inside a pair of square brackets []
    - [ab12] → Returns a match where one of the specified characters (a, b, 1, or 2) is present	
    - `-` → **between**, returns a match for any character between two characters
    - `^` → **except**,	Returns a match for any character except the specified ones
    - `+`, `*`, `.`, `|`, `()`, `$`,`{}` in set has no special meaning, return a match for the exact character
* `x{quantity}`: Surrounds the **quantity** specifying exact number of repetition of the preceding character (`x`)
* `x?`: Marks the preceding character (`x`) as an **optional match**, repeating 0 to 1 time
* `x*`: Marks the preceding character (`x`) as **repeating 0 to any number of times**
    - `*?`: Non-greedy matching
* `x+`: Marks the preceding character (`x`) as **Repeating 1 to any number of times**
* `^`: **Start** of a line. 
* `String$`: Matches the **end** of a string.
* `x|y`: Matches either `x` or `y`
* `.`: Matches **Any character**
* `*?`: Non-greedy matching. By default, regex is greedy (matches as much as possible). Use ? for non-greedy matching.
    ```py
    text = "<p>First</p><p>Second</p>" 

    greedy = re.compile(r'<p>.*</p>') 
    non_greedy = re.compile(r'<p>.*?</p>') 

    print(greedy.findall(text))  # ['<p>First</p><p>Second</p>'] 
    print(non_greedy.findall(text))  # ['<p>First</p>', '<p>Second</p>'] 
    ```
* `\`: Marks the following as a special sequence or escape character e.g. `\d` for digits

### Special Sequences
* `\A` → Absolute start, meaning absolute beginning of a whole string
* `\b` | `\B` → boundary | non-boundary
    - start of a line, or an end of a line, or a whitespace
* `\d`|`\D` → Digit | Non-Digit
    - a character from 0 to 9
* `\s`|`\S` → White Space | Not a White-space
* `\w`|`\W` → Word Character | Not Word Character
    - a character from a to Z, or a digit from 0-9, or the underscore `_` character
* `\Z` → End of the string or just before a final newline

### Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

### Flags

* `re.IGNORECASE` | `re.I`: Case-Insensitive Matching & Substitution
    - `re.findall(r'pattern', text, flags=re.IGNORECASE)`
* `re.VERBOSE` | `re.X`: Allows whitespaces and comments inside patterns
* `re.MULTILINE` | `re.M`: Returns only matches at the beginning of each line
* `re.DOTALL` | `re.S`: The `.` metacharacter match all characters (including `\n`)
* `re.ASCII` | `re.A`: Returns only ASCII matches
* `re.DEBUG`: Displays debug information

### Mini-Project: Extract Data from Log Files 

**Reason**: Log files often contain critical information like errors or timestamps. Extracting this data manually is tedious, but regex can automate it, making analysis faster.

```py
import re 

def extract_errors(log_file): 
    errors = [] 

    with open(log_file, 'r') as f: 
        for line in f: 
            match = re.search(r'ERROR - (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)', line) 

            if match: 
                timestamp, message = match.groups() 
                errors.append((timestamp, message)) 
    return errors 
 

# Example usage 
errors = extract_errors('error.log') 

for timestamp, message in errors: 
    print(f"{timestamp}: {message}") 
```

**Explanation**

This script reads a log file, uses regex to find lines starting with "ERROR -", and extracts the timestamp and message. It returns a list of tuples for further analysis.