# Python Automation
Documentation on Python Automation

**[⇐ Data Engineering Fundamentals](../README.md)**
- [File Manipulation](./i.%20Python%20File%20Manipulation.md)
- [Regular Expressions](./ii.%20Python%20Regular%20Expressions.md)
- [Debugging](./iii.%20Debugging.md)
- [Excel Manipulation](./iii.%20Excel%20Manipulation.md)
- [JSON Manipulation](./iv.%20JSON%20Manipulation.md)

- [Threading & Scheduling](./v.%20Threading%20&%20Scheduling.md)
- [Sending & Retrieving Emails](./vi.%20Sending%20&%20Retrieving%20Emails.md)
- [GUI Automation](./vii.%20GUI%20Automation.md) 


## Automation
Automation is the process of using technology to perform tasks with minimal or no human intervention, it involves the use of systems or software to automatically execute repetitive, rule-based tasks that would otherwise require manual effort. Examples: Automatic Coffee Machine

* Benefits of Automation: Saves time, improves accuracy, increases efficiency, cost effective, scalability, reliability

## Python Automation
Python is high-level programming language widely used for automation because of its simple syntax, rich ecosystem of libraries, cross-platform support, strong community support.

### Python Libraries and Scripts for Automation
* **Web Automation**: Selenium, Playwright, `requests`, BeautifulSoup
* **File Automation**: `os`, `shutil`, `pathlib`, `watchdog`
* **Excel/CSV Automation**: `pandas`, `openpyxl`, `csv`
* **Email Automation**: `smtplib`, `imaplib`, `email`
* **Desktop Automation**: `pyautogui`, `pywinauto`
* **Task Scheduling**: `schedule`, APScheduler
* **API Automation**: `requests`, `httpx`


### Real-World Examples of Python Automation 

1. **Web Scraping** and **Data Collection** 
    * **Use case**: Collecting prices from e-commerce websites.
    * **Libraries**: requests, BeautifulSoup, Scrapy
    * **Example**: Automatically pulling daily stock prices from a financial site. 
2. **Automated Email Reports**
    * **Use case**: Sending daily sales reports via email.
    * **Libraries**: pandas, smtplib, email
    * **Example**: Generate an Excel file of sales data and email it every morning. 

3. **File and Folder Management**
    * **Use case**: Organizing downloaded files by type or date.
    * **Libraries**: os, shutil, pathlib
    * **Example**: Automatically move images from Downloads to Pictures folder. 

4. Browser Automation (Testing, Form Submission)
    * **Use case**: Filling out online forms or testing web apps.
    * **Libraries**: Selenium, Playwright
    * **Example**: Automatically log in to a website and download a file. 

5. PDF and Document Handling
    * **Use case**: Extracting text from PDFs or merging documents.
    * **Libraries**: PyPDF2, pdfplumber, docx
    * **Example**: Merge multiple PDFs into one document automatically. 

6. Task Scheduling
    * **Use case**: Run a Python script at specific intervals.
    * **Libraries**: schedule, cron (Linux), Task Scheduler (Windows)
    * **Example**: Run a backup script daily at midnight. 

7. Chatbot or Customer Support Bot
    * **Use case**: Automating replies to FAQs on a website.
    * **Libraries**: ChatterBot, transformers, Flask
    * **Example**: Deploy a customer support chatbot with pre-trained responses. 

8. GUI Automation (Desktop Tasks)
    * **Use case**: Automate button clicks, mouse movements, or form-filling.
    * **Libraries**: pyautogui
    * **Example**: Automatically open an application and perform a set of actions.