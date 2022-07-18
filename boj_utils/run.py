import re
import requests
import argparse
import subprocess
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Run solution.py')
parser.add_argument('--input', type=int, default=0, help="Test input number")
parser.add_argument('--file', default="solution.py", help="python file")
args = parser.parse_args()

with open("solution.py", 'r') as f:
    url = f.readline().lstrip("# ").rstrip()
    problem_number = url.split('/')[-1]

resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
sample_input = soup.find_all('pre', 'sampledata', id=re.compile('sample-input'))[args.input]
sample_output = soup.find_all('pre', 'sampledata', id=re.compile('sample-output'))[args.input]
sample_input, sample_output = sample_input.text.rstrip(), sample_output.text.rstrip()

print(f'\n>>> Run BOJ problem {problem_number} with Input:\n\n{sample_input}\n')

p = subprocess.run(["python", args.file], input=sample_input, capture_output=True, text=True)
if p.returncode == 0:
    print(p.stdout)
else:
    print(p.stdout)
    print(p.stderr)

