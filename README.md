# python_challenge
Repo for Module 3 Challenge


Code Sources:

Geeks For Geeks: 
Writing to a .txt file 
PyBank : Lines 41-46 , 51-58
PyPoll: Lines 39-48
https://www.geeksforgeeks.org/writing-to-file-in-python/
[with open ("analysis/output.txt) as file:]


Stack Overflow: 
Rounding up to 2 decimals 
PyBank ; Line 31
https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
[round((..),2)]


AskBSC: 
Output corrent amount of decimal places 
PyPoll ; Line 36
AskBCS agent suggested I multiply "val/total_votes" by 100 first and then round to the thrid decimal place
{round((val/total_votes *100),3)}


Programiz:
How to work with just values in a dictionary
PyPoll ; Line 27
https://www.programiz.com/python-programming/methods/dictionary/values
[print(results.values())]


Geeks for Geeks:
How to work with all items in a dictionary
PyPoll ; Line 30, Line 35
https://www.geeksforgeeks.org/python-dictionary-items-method/
[print(results.items())]


I/O FLOOD: 
How to sort a dictionary by value
PyPoll ; Line 4 , Line 30
https://ioflood.com/blog/python-sort-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by,items()%2C%20key%3Doperator.
[import operator 
dict(sorted(results.items(), key= operator.itemgetter(1), reverse=True))]


W3 Schools: 
How to work with just keys in a dictionary
PyPoll ; Line 21 , Line 31
https://www.w3schools.com/python/ref_dictionary_keys.asp
[print(results.keys())]


Geeks for Geeks: 
How to get the first key in a dictionary
PyPoll ; Line 31
https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
[winner = list(sorted_rresults.keys())[0]]






