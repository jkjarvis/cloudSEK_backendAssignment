import requests
import argparse
import urllib.parse
import urllib3
import threading
import queue
import sys
import time

def args_parse():
    parser = argparse.ArgumentParser(description="Web Page Brute Forcer")
    parser.add_argument('-u', '--url', action="append", dest='url', help='Enter the root url',
                        required=True)
    parser.add_argument('-w', '--wordlist', dest='wordlist', help='Enter the path to the wordlists file', required=True)
    parser.add_argument('-c', '--codes', action="append", dest="codes", help="Enter the accepted codes , single code after each -c flag", required=True )
    return parser.parse_args()


def scan(word_queue, url, codes):
    while not word_queue.empty():
        try:
            word = word_queue.get_nowait()
        except queue.Empty:
            break
        
        url = url + word.lstrip('/')
        
        response = requests.get(url)

        if str(response.status_code) in codes:
            print(f'{url} [Status Code {response.status_code}]')


def main():
    args = args_parse()

    for i in range(len(args.url)):
        if not args.url[i].endswith('/'):
            args.url[i] = args.url[i] + '/'
    print(args.url)
    words = open(args.wordlist).readlines()
    
    if len(words) < 1000:
        print("Wordlist must contain atleast 1000 words.")
        return 
    word_queue = queue.Queue()
    for word in words:
        word_queue.put(urllib.parse.quote(word.strip()))

    threads = []
    for i in range(len(args.url)):
        t = threading.Thread(target=scan, args=(word_queue, args.url[i], args.codes))
        t.start()
        threads.append(t)

    while True:
        try:
            time.sleep(0.5)
            if word_queue.empty() and True not in [t.is_alive() for t in threads]:
                sys.exit(0)
        except KeyboardInterrupt:
            while not word_queue.empty():
                try:
                    word_queue.get(block=False)
                except queue.Empty:
                    pass
            sys.exit(0)


if __name__ == "__main__":
    urllib3.disable_warnings()
    main()