"""
exercise03.py

Here is where we put our core logic to test
"""


def lines_in_file(file_name):
    """
    Get the lines from a file

    Arguments
    ---------

    file_name: str
               full path to file

    Returns
    -------
    lines: list
    """
    with open(file_name) as f:
        lines = f.readlines()
    return lines

def get_line(file_name, line_number):
    """
    Get a particular line from a file

    Arguments
    ---------
    line_number: int
                 the index of the line to return
    Returns
    -------
    line: str
          the line at position line_number
    """

    lines = lines_in_file(file_name)
    return lines[line_number]

def fields_in_line (line, delim = ","):

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

    fields = line.strip().split(delim)
    return fields 

def n_fields_in_line(line):
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
    nf = len(line.strip().split(","))
    return nf

def longest_field_in_line(line, delim = ","):
    """
    Find the longest field in a line

    Arguments
    ---------

    line: str
         A string with delmited fields

    Returns
    -------
    field: str
           The longest field in the delimted line

    """
    
    fields = fields_in_line(line, delim)
    maxlen = 0
    maxlenfield = ""
    for field in fields:
    	if (len(field) > maxlen):
		maxlen = len(field)
		maxlenfield = field
    return maxlenfield
