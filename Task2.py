"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""

call_duration_dict = {}


def calls_as_dictionary(phone_number, duration):
    if phone_number in call_duration:
        call_duration_dict[phone_number] += duration
    else:
        call_duration_dict[phone_number] = duration


call_number = []
call_duration = []
longest_calls_duration = 0

for call in calls:
    """
    collect the phone number and duration of incoming caller
    collect the phone number and duration of call recever
    """
    call_number.append(call[0])
    call_duration.append(call[3])
    call_number.append(call[1])
    call_duration.append(call[3])

for each_call in range(len(call_number)):
    calls_as_dictionary(call_number[each_call], int(call_duration[each_call]))

for phone_number in call_duration_dict:
    """
    I was strongly inspired by the solution pattern in Lesson 3 section 11: Prolific Year
    """
    if call_duration_dict[phone_number] > longest_calls_duration:
        longest_calls = []
        longest_calls.append(phone_number)
        longest_calls_duration = call_duration_dict[phone_number]
    elif call_duration_dict[phone_number] == longest_calls_duration and not (phone_number in longest_calls):
        longest_calls.append(phone_number)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_calls,
                                                                                          longest_calls_duration))
