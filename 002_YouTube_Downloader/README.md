# YouTube Downloader 
This program is built using **PyTube 12.1.0** and you need to have it installed! <br>
In order to install PyTube Simpley Type in your terminal: 
> pip install pytube==12.0.1 <br>

## How to Use
After Clonning the repositor using *terminal* or *CMD* go to the directory where **YT_Downloader.py** file is located. <br>
To start the Program simply *run* it using  following Command:<br>
> python YT_Downloader.py 

This Python Program will help you download YouTube Videos in any of the following Methods:
### 1. Download YouTube Single YouTube Videos:
In this method it will ask for the url which you have to provide and you can choose available *resoulution* of the video to download.
### 2. Download YouTube PlayList:
In this method you have to provide it with the link of the YouTube Playlist Link, and also choose the Resolution of the video to download.
### 3. Download Multiple Videos Using List of Links in a **.txt** File:
In this Video you have to keep all the links of the videos you want to be downloaded in a single text file. for example: **download_list.txt**. The link in the text file should be separated with a new link ( each link should be in a new line) <br>
**Example of download_list.txt file Content:**<br>
```
https://youtu.be/asdfasdfasdf
https://youtu.be/asdfsadfasdf
https://youtu.be/asdfasdfsadf
https://youtu.be/asdfasdfasdf
https://youtu.be/asdfasdfsadf
https://youtu.be/asdfasdfasdf
```
while executing the program you have to provide this file name along with it location (in case this file is not located in the location of the script).
**example:**<br>
> Enter the location/name.txt of the file containing the URLs of the videos you want to download: 
c:/users/.../download_list.txt

In case of any error the program will tell you where the error is and you will know how to solve it. <br>

## Where are the downloaded Files 
The Files will be downloaded to the folder where this script is located. <br>
In order to keep the downloaded files in diffrent Directory copy this script to your desired directory and Execute it from there. 