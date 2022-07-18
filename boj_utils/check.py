import re
import requests
import subprocess
from bs4 import BeautifulSoup

with open("solution.py", 'r') as f:
    url = f.readline().lstrip("# ").rstrip()
    problem_number = url.split('/')[-1]

resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

sample_inputs = soup.find_all('pre', 'sampledata', id=re.compile('sample-input'))
sample_outputs = soup.find_all('pre', 'sampledata', id=re.compile('sample-output'))

print(f'\nChecking BOJ problem {problem_number}...\n')

for i, (sample_input, sample_output) in enumerate(zip(sample_inputs, sample_outputs), 1):
    sample_input, sample_output = sample_input.text.rstrip(), sample_output.text.rstrip()
    sample_input, sample_output = '\n'.join(sample_input.splitlines()), '\n'.join(sample_output.splitlines())
    p = subprocess.run(["python", "solution.py"], input=sample_input, capture_output=True, text=True)
    if p.returncode == 0:
        if sample_output == p.stdout.rstrip():
            print(f'[Test {i}] Passed!')
        else:
            print(f'[Test {i}] Failed.')
            print('Solution Ouput:')
            print(p.stdout.rstrip())
            print('Expected Ouput:')
            print(sample_output)
    else:
        print(f'[Test {i}] Error.')
        print('Error:')
        print(p.stderr)
    print()

