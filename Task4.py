"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
incoming_calls = []
receiving_calls = []
for call in calls:
    incoming_calls.append(call[0])
    incoming_calls.append(call[1])

incoming_calls = list(set(incoming_calls))
incoming_calls.sort()

incoming_texts = []
receiving_texts = []

for text in texts:
    incoming_texts.append(text[0])
    incoming_texts.append(text[1])

possible_marketing_calls = []
for call in incoming_calls:

    if not (call in receiving_calls or call in incoming_texts or call in receiving_texts):
        possible_marketing_calls.append(call)

print("These numbers could be telemarketers: ")
for _ in possible_marketing_calls:
    print(_)
