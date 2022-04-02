# cloudSEK_backendAssignment
A web path brute-forcer using cli which accepts a list of URLs and a wordlist and status codes, then calls the specific paths and prints which gave the appropriate response.

# Usage 
Giving Input
* url: Type input url after '-u' , for multiple urls, add '-u' flag before each url. e.g ` python main.py -u https://github.com -u https://google.com `
* wordlist: enter the path for the wordlist after "-w" . e.g ` python manage.py -u https://github.com -w path/to/wordlist.txt `
* http codes: for a list of http codes, add single code after each "-c" flag. e.g ``` python manage.py -u https://github.com -w path/to/wordlist.txt -c 200 -c 404 ```
