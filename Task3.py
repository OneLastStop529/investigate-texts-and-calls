"""
Intro to Python Lab 1, Task 3

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

calls_dictionary = {}


def calls_dict(incoming_calls, answering_calls):
    """Define the method that take incoming calls and answering calls,
       and turn it into a dictionary
    """
    calls_dictionary[incoming_calls] = answering_calls


for call in calls:
    # see if the incoming calls contains "080"
    if "080" in call[0]:
        calls_dict(call[0], call[1])

list_of_codes = []

for bangalore_call in calls_dictionary:
    if "(0" in calls_dictionary[bangalore_call]:
        """ use [:str.index(...)+1} to crop out fixed line area code, +1 to include the closing parentheses,
            same method applies to mobile and Telemarketers' prefix
        """
        list_of_codes.append(calls_dictionary[bangalore_call][:calls_dictionary[bangalore_call].index(")") + 1])
    elif " " in calls_dictionary[bangalore_call] and (
            calls_dictionary[bangalore_call].startswith("7") or calls_dictionary[bangalore_call].startswith("8") or
                calls_dictionary[bangalore_call].startswith("9")):
        # crop out the first four digits out of the number
        list_of_codes.append(calls_dictionary[bangalore_call][:4])
    elif "140" in calls_dictionary[bangalore_call]:
        list_of_codes.append(calls_dictionary[bangalore_call][:3])

    # take out the duplicates
    list_of_codes_as_set = set(list_of_codes)
    list_of_codes = list(list_of_codes_as_set)
    # sort it lexicographically
    list_of_codes.sort()

# Start wondering why there is no "140" in the output.
# then I guess nobody would actually call Telemarkets' number spontaneously
print("The numbers called by people in Bangalore have codes:{}")
for code in list_of_codes:
    print(code)


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
bangalore_receive = 0
bangalore_calling = len(calls_dictionary)


for bangalore_call in calls_dictionary:
    if "080" in calls_dictionary[bangalore_call]:
        bangalore_receive += 1
# keep the 4 digits after the floating point
percentage = round((bangalore_receive/bangalore_calling), 4)*100

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))