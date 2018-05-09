# Get-Redirects
Script to enumerate all redirects of a given URL.  
Must have Python3 installed.  
Only compatible with Ubuntu Linux and derivatives.  
## Usage:
```bash
git clone https://github.com/ProbieK/Get-Redirects.git
cd Get-Redirects
sudo chmod +x ./get-redirects ./get-domain.py
./get-redirects -h
```
## About:
It cURL's the given URL with a randomly selected useragent string [from a list of 10 predefined] and outputs the unique domains that it was redirected to.
