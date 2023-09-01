import requests, sys, os, time, re

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

def sort_key(filename):
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return filename

def main():

    if (len(sys.argv) != 4):
        print("Invalid Arguments | uploader.py <folderName> <domainName> <password> |")
        sys.exit(0)

    folder = sys.argv[1]
    domainName = sys.argv[2]
    password = sys.argv[3]

    uploadResultsURL = "http://mxsimulator.com/uploadresults.php"

    if (not os.path.exists(folder)):
        print("Folder Does Not Exist!")
        sys.exit(0)

    data = {
        "name": domainName,
        "password": password,
    }

    for file in sorted(os.listdir(folder), key=sort_key):

        if (not file.endswith(".txt")):
            continue

        with open(folder + "/" + file, "r") as resultsFile:
            results = resultsFile.read()

        data['results'] = results

        print("Uploading " + file)

        # Perform the POST request
        response = requests.post(uploadResultsURL, data=data)

        # Check the response
        if response.status_code == 200:
            print(LINE_UP, end=LINE_CLEAR)
            print("Request successful.")
            print("Page Returned: " + response.text)
            if "OK - " in response.text:
                print("File Removed")
                print("\n")
                os.remove(folder + "/" + file)
        else:
            print(LINE_UP, end=LINE_CLEAR)
            print("Request failed. Status code:", response.status_code)
            print("Page Returned: " + response.text)
            print("\n")

        time.sleep(3)
        print(LINE_UP, end=LINE_CLEAR)

    print("\nAll Results Uploaded!")


if (__name__ == "__main__"):
    main()