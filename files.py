# We are aiming for underscore-based naming in this class
def read_airport_csv(file_name):
    """
    Load airport data from a CSV file, converting numeric columns to numbers
    Arguments
    ---------
    path: string
          Path to the CSV file to load
    Returns
    -------
    header: list
            The header row of the CSV file
    data: list
          The data rows of the CSV file
    """
    data = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f) # This is an iterator
        for line in reader:
            data.append(line)
    header = data[0]
    data   = data[1:]
    
    # Fix numeric values
    lookup = dict([(v,k) for k,v in enumerate(header)])
    lat_idx = lookup['latitude']
    lon_idx = lookup['longitude']
    aptid_idx = lookup['airport_id']
    alti_idx = lookup['altitude']
    zone_idx = lookup['zone'] # Timezone (I believe relative to UTC)
    
    for line in data:
        line[aptid_idx] = int(line[aptid_idx])
        line[lat_idx]   = float(line[lat_idx])
        line[lon_idx]   = float(line[lon_idx])
        line[alti_idx]  = float(line[alti_idx])
        line[zone_idx]  = float(line[zone_idx])
    #
    
    return (header, data)
#


##

import csv

def read_csv(file_name):
    newlines = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            newlines.append(line)
    return newlines