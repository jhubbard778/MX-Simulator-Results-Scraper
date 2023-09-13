# MX Simulator Results Scraper
 An MX Simulator Server Results Scraper and Uploader.

 scraper.py takes in a list of urls from which you want to scrape all results from.<br>
 uploader.py arguments are as follows: python uploader.py [folderName] [domainName] [password] where:<br>
    - folderName is the folder which holds all the results.<br>
    - domainName is the domain you want to post the results to.<br>
    - password is the password the domain has for uploading results (sets password if new domain)

Example executions:<br>
python scraper.py https://servers.mxsimulator.com/servers/elsinore.mxsimulator.com:19800/ https://servers.mxsimulator.com/servers/elsinore.mxsimulator.com:19801/ <br>
python uploader.py results elsinore.mxsimulator.com:19800 !password12345
