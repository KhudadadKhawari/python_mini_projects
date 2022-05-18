# Encrypt PDF with Python [Script + Tkinter for GUI]
This is a mini project you can practice with python. I have used [**PyPDF2**](https://pypi.org/project/PyPDF2/) Package to read PDF file and then write it's encrypted copy with the password given by the user.<br>
To ease the usage of this app I used tkinter to design a simple GUI for non-programmer users, who would like to use this app. 
## Run Using Source Code
to use this app after downloading the package or clonning it from github, go to **current Directory** in terminal and run the following **command** to install the required PyPDF2 Package:

> pip pip install PyPDF2

Then you can run the file by the following command:

> python encrypt_pdf.py

## Make Executable File
If you are using windows or any other Operating System you can make an executable file out of this App <br>
to create an Executable file you need [***PyInstaller***](https://pyinstaller.org/en/stable/) Package <br>

To install this package run the following command in terminal:

> pip install -U pyinstaller

After installing PyInstaller go to **encrypt_pdf.py** file directory and run the following command:

> pyinstaller encrypted_pdf.py

Now an executable must have been created in current location inside **dest** folder.
## Screenshots
1. ***Main Screen***:
<br>

![Main Screen image](https://github.com/KhudadadKhawari/python_mini_projects/blob/main/001_encrypt_PDF/screenshots/1.png)

2. After Opening a PDF file using **Open File** Button:
<br>

![File Opened image](https://github.com/KhudadadKhawari/python_mini_projects/blob/main/001_encrypt_PDF/screenshots/2.png)

3. ***Successfull Encryption***
<br>

![Successfull Encryption Image](https://github.com/KhudadadKhawari/python_mini_projects/blob/main/001_encrypt_PDF/screenshots/3.png)

### Developed by: [**Khudadad Khawari**](https://facebook.com/KhudadadKhawari.py)