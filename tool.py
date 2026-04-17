import socket
import threading
from queue import Queue
import argparse
import requests

parser = argparse.ArgumentParser(description="Advanced Subdomain Enumeration Tool")
parser.add_argument("domain", help="Target domain (e.g., example.com)")
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
parser.add_argument("-o", "--output", help="Save results to file")

args = parser.parse_args()

domain = args.domain
wordlist_path = args.wordlist
threads = args.threads
output_file = args.output

queue = Queue()
results = []

def scan():
    while not queue.empty():
        sub = queue.get()
        subdomain = f"{sub}.{domain}"

        try:
            socket.gethostbyname(subdomain)

            try:
                url = f"http://{subdomain}"
                response = requests.get(url, timeout=2)
                status = response.status_code
            except:
                status = "No HTTP"

            output = f"[+] {subdomain} | Status: {status}"
            print(output)
            results.append(output)

        except:
            pass

        queue.task_done()

try:
    with open(wordlist_path, "r") as f:
        for line in f:
            queue.put(line.strip())
except:
    print("[-] Error loading wordlist")
    exit()

for _ in range(threads):
    t = threading.Thread(target=scan, daemon=True)
    t.start()

queue.join()

if output_file:
    with open(output_file, "w") as f:
        for line in results:
            f.write(line + "\n")

print("\nScan completed!")