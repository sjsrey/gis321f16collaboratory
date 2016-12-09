"""
exercise03.py

Here is where we put our core logic to test
"""


def lines_in_file(file_name): # I wrote the counting feature
    count = 0
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines: # counts the number of lines in a file
        count  = count + 1 
    return count, lines

def get_line(file_name, line_number):
    count, lines = lines_in_file(file_name)
    return lines[line_number]

def fields_in_line(line, delim=","):
    """
    Get the fields in a line delimited by delim

    Arguments
    ---------
    line: str
          A long string
    delim: str
           A single character used to delimit the fields

    Returns
    -------
    fields: list
            Sequence of fields separated by delim
    """

    fields = line.strip().split(delim) # I did not write this method
    return fields

def n_fields_in_line(line):
    count = 0
    """
    Find number of fields in a delmited line

    Arguments
    ---------
    line: str
         A string with delmited fields

    Returns
    -------
    nf: int
        The number of fields in the string
    """
    fields =line.split()
    for feild in feilds:
        count = count + 1
    return count
def longest_field_in_line(line):
    answer = 1
    fields = line.split()
    for field in fields:
	lenOfField = len(field)
	if lenOfField > answer:
            answer = lenOfFeild
    return answer
