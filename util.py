"""
Utility functions
"""

def get_column_by_name(header, data, attribute):
    """
    Returns a list consisting of the column associated with the given attribute name
    """
    idx = header.index(attribute)
    return [record[idx] for record in data]

# Not actually used in my system here, but this is a neat bit of code
# Converts a list to floats, by mapping the float() function onto the list
# map() returns an iterator; list converts it into a list
def list_to_float(att_list):
    return list(map(float, att_list))
#

def get_airport_by_id(header, data, id):
    # TODO: Make a function to return a lookup table instead of rebuilding the index each time?
    ids = get_column_by_name(header, data, "airport_id")
    return data[ids.index(id)]
##
def get_attribute(data, attribute_name):
    header = data[0]
    idx = header.index(attribute_name)
    return [record[idx] for record in data[1:]]

def to_float(attribute_list):
    return list(map(float, attribute_list))
          
