# MX Simulator Results Scraper
 An MX Simulator Server Results Scraper and Uploader.

### Requirements

##### Python 3
To install python 3 visit:<br>
https://www.python.org/downloads/

##### Requests Library
To install the requests library, type into your terminal:
``` pip install requests ``` or ``` pip3 install requests ```<br>


### Descriptions
scraper.py takes in a list server domains from which you want to scrape all results from.<br><br>
uploader.py arguments are as follows: python uploader.py [folderName] [domainName] [password] where:<br>
    - folderName is the folder which holds all the results.<br>
    - domainName is the domain you want to post the results to.<br>
    - password is the password the domain has for uploading results (sets password if new domain)

### Example executions:
python scraper.py elsinore.mxsimulator.com:19800 elsinore.mxsimulator.com:19801 elsinore.mxsimulator.com:19802 <br><br>
python uploader.py results elsinore.mxsimulator.com:19800 !password12345
