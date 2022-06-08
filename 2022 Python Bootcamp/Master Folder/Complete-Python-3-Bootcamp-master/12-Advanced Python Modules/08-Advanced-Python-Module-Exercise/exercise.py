import re
import os

# pattern = r'\d{3}-\d{3}-\d{4}'
# test_string = "here is a random number 1231231234, here is phone number formatted 123-123-1234"
# answer = re.findall(pattern, test_string)
# print(answer)

def search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        answer = re.search(pattern,text)
        print(str(answer))
        return re.search(pattern, text)
    else:
        return 'Not Found'

results = []
for folder, sub_folders, files in os.walk(os.getcwd()+"\\extractecd_content"):
    for f in files:
        full_path = folder+'\\'+f

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())

