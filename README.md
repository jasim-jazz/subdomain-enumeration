# Advanced Subdomain Enumeration Tool

This project is a Python-based subdomain enumeration tool developed for learning and practicing reconnaissance techniques used in cybersecurity and bug bounty hunting.

The tool performs subdomain discovery using wordlist-based brute forcing, DNS resolution, and HTTP status checking.

---

## Features

* Multi-threaded subdomain enumeration
* Wordlist-based brute forcing
* DNS resolution to identify valid subdomains
* HTTP status code detection for discovered hosts
* Option to save results to a file
* Command-line interface using argparse

---

## Requirements

* Python 3.x
* requests library

Install dependencies:

```bash
pip install requests
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/subdomain-enumerator.git
cd subdomain-enumerator
```

---

## Usage

```bash
python3 subdomain.py <domain> -w <wordlist> [options]
```

---

## Arguments

| Argument       | Description                      |
| -------------- | -------------------------------- |
| domain         | Target domain (example.com)      |
| -w, --wordlist | Path to wordlist file (required) |
| -t, --threads  | Number of threads (default: 100) |
| -o, --output   | Save results to file             |

---

## Examples

Basic scan:

```bash
python3 subdomain.py example.com -w subdomains.txt
```

Using custom thread count:

```bash
python3 subdomain.py example.com -w subdomains.txt -t 200
```

Save results to file:

```bash
python3 subdomain.py example.com -w subdomains.txt -o results.txt
```

Using a larger wordlist:

```bash
python3 subdomain.py example.com -w /path/to/wordlist.txt
```

---

## How It Works

1. Loads subdomains from a wordlist
2. Attempts DNS resolution for each subdomain
3. If valid, sends an HTTP request
4. Displays the subdomain with its HTTP status
5. Optionally saves results to a file

---

## Example Output

```
[+] admin.example.com | Status: 200
[+] dev.example.com | Status: 403
[+] test.example.com | Status: No HTTP
```

---

## Disclaimer

This tool is intended for educational purposes only.

Only use it on systems you own or have explicit permission to test. Unauthorized scanning is illegal.

---

## Author

Mohamed Jasim

---

## Future Improvements

* HTTPS support
* Improved error handling
* Integration with larger wordlists
* Faster DNS resolution methods
* Output formatting improvements
