"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
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
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
list_of_calls = []
for call in calls:
    list_of_calls.append(call[0])
    list_of_calls.append(call[1])

calls_as_set = set(list_of_calls)

list_of_texts = []
for text in texts:
    list_of_texts.append(text[0])
    list_of_texts.append(text[1])

texts_as_set = set(list_of_texts)

total_unique_phone_number = len(calls_as_set.union(texts_as_set))
print("There are {} different telephone numbers in the records.".format(total_unique_phone_number))
