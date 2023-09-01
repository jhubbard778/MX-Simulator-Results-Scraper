import requests, re, sys, os

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

def isValidSimServer(url):
    response = requests.get(url)
    return (response.status_code > 199 and response.status_code < 300)

def scrapeResults(serverURL):

    print("\nScraping Results From: " + serverURL)

    # get the folder name
    serverURLArr = serverURL.split("/")
    if (serverURLArr[-1] == ''):
        serverURLArr.pop()

    folderName = serverURLArr[-1].replace('.','-').replace(':','-')

    # get the latest race number
    latestRaceNumber = -1
    if (os.path.exists(folderName)):
        for file in os.listdir(folderName):
            if (not file.endswith(".txt")):
                continue

            # get latest race number based on files
            raceNumber = int(file.replace("results-",'').replace('.txt',''))
            if (raceNumber > latestRaceNumber):
                latestRaceNumber = raceNumber
    else:
        os.makedirs(folderName)


    # do scraping
    while True:

        print("Getting Race Number: " + str(latestRaceNumber + 1) + "...")

        url = serverURL + "races/" + str(latestRaceNumber + 1) + ".html"
        response = requests.get(url)

        if (response.status_code < 200 or response.status_code > 299):
            print(LINE_UP, end=LINE_CLEAR)
            break

        latestRaceNumber += 1

        # find result lines data (re.DOTALL checks for regex across multiple lines)
        pattern = re.compile(r'resultslines=\[(.*?)\]', re.DOTALL)
        match = pattern.search(response.text)

        if match:
            # get the results content and reformat
            results_content = match.group(1)
            formattedText = results_content.replace('"', '').replace(',', '')

            # save to file
            fileName = folderName + "/results-" + str(latestRaceNumber) + ".txt"
            f = open(fileName, "w")
            f.write(formattedText)
            f.close()

        print(LINE_UP, end=LINE_CLEAR)
    
    print("Done Scraping From: " + serverURL)

def main():

    urls = sys.argv[1:]
    validUrls = list(map(isValidSimServer, urls))

    if (len(urls) == 0 or not True in validUrls):
        print("Enter a valid server link...")
        sys.exit(1)

    for i in range(len(urls)):
        if (validUrls[i] == False):
            continue

        scrapeResults(urls[i])

    print("Scraped All Data!")
    

if (__name__ == '__main__'):
    main()