"""
Functions that deal with distance calculations
"""
import math
from . import util

def euclidean_distance(p1,p2):
    """
    Calculates the Euclidean distance between two points
    d = sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
    
    Arguments:
    p1: tuple
        (x1, y1, ...) (currently only works in 2d space)
    p2: tuple
        (x2, y2, ...)
    
    Returns:
    distance: numeric
              Distance betwween the two points
    """
    x1,y1 = p1
    x2,y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
#

def great_circle_distance(p1,p2, r=-1):
    """
    Calculates the Haversine distance between two points
    See https://en.wikipedia.org/wiki/Haversine_formula#The_haversine_formula
    
    Arguments:
    p1: tuple
        (lon1, lat1)
    p2: tuple
        (lon2, lat2)
    r:  numeric
        Radius of the planet (any units).  The default value of -1 will return
        the distance in degrees along a great circle path.  The Earth has a radius
        of approximately 6,371 km.
    Returns:
    distance: numeric
              Distance between the two points.  Units are whatever the radius 
              was passed as if it was explicitly specified (default is degrees).
    """
    lon1,lat1 = p1
    lon2,lat2 = p2
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    def hav(theta):
        return (1 - math.cos(theta))/2
    
    # Haversine formula from Wikipedia
    d = 2 * r * math.asin(math.sqrt( hav(lat2-lat1)+math.cos(lat1)*math.cos(lat2)*hav(lon2-lon1) ))
    
    # If r is -1, distance is in negative radians, so convert to degrees before returning
    if r == -1:
        return math.degrees(-d)
    else:
        return d
#

# A useless function that won't show up in the points namespace
# Unless __init__ gets edited
def local_function():
    pass
#

def nearest_airport(header, data, origin, dist_function=great_circle_distance):
    """
    Origin is an index, not a point
    """
    lat_idx = header.index("latitude")
    lon_idx = header.index("longitude")
    
    nnd = float('inf')
    best_match_index = -1
    origin_coords = (data[origin][lon_idx], data[origin][lat_idx])
    for i,point in enumerate(data):
        if i == origin: continue # not checking the point against itself
        d = dist_function( origin_coords, (data[i][lon_idx], data[i][lat_idx]) )
        if d > 0 and d < nnd:
            nnd = d
            best_match_index = i
        #
    return (best_match_index, nnd)
#

def furthest_airport(header, data, origin, dist_function=great_circle_distance):
    """
    Origin is an index, not a point
    """
    lat_idx = header.index("latitude")
    lon_idx = header.index("longitude")
    
    fnd = 0
    best_match_index = -1
    origin_coords = (data[origin][lon_idx], data[origin][lat_idx])
    for i,point in enumerate(data):
        if i == origin: continue # not checking the point against itself
        d = dist_function( origin_coords, (data[i][lon_idx], data[i][lat_idx]) )
        if d > 0 and d > fnd:
            fnd = d
            best_match_index = i
        #
    return (best_match_index, fnd)
#

########################################
# Specialized functions for Exercise05 #
########################################

def get_neighbor_list(header, data, neighbor_function=nearest_airport, dist_function=great_circle_distance):
    """
    For each airport, finds a single matching airport using the specified 
    neighbor_function, and returns a list of all airport pairs and the distances
    between them.
    
    Arguments:
    header: list
            List of strings containing the names of the columns in data
    data: list
          list of lists, where the elements of each sub-list correspond to the 
          columns specified by header.
    neighbor_function: function
                       A function that takes a data store, row index, and distance
                       function, and returns the row index and distance (or possibly
                       some other value) of a second airport.
    dist_function: function
                   The distance function to be passed to neighbor_function
    Returns:
    neighbor_list: list of tuples
                   Contains one entry for each row in the data store, with the format
                   (row_airport_id, other_airport_id, distance).
    """
    
    # Make coordinate list
    lat = util.get_column_by_name(header, data, "latitude")
    lon = util.get_column_by_name(header, data, "longitude")
    aptid = util.get_column_by_name(header, data, "airport_id")
    coords = list(zip(lon, lat))
    
    return_list = []
    
    for i,row in enumerate(data):
        match_idx, dist = neighbor_function(header, data, i, dist_function)
        origin_id = aptid[i]
        nn_id = aptid[match_idx]
        return_list.append( (origin_id, nn_id, dist) )
    #
    return return_list
#

def nearestD(DataName):
    data = read_csv('data.csv')
    Lats = to_float(get_attribute(data,'latitude'))
    Lons = to_float(get_attribute(data,'longitude'))
    Ids = to_float(get_attribute(data,'airport_id'))
    Cors = list(zip(Lats, Lons))
    distance = []
    origin_id = []
    nn_id = []
    
    for idX, i in enumerate(Cors):
        ND = float("inf")
        
        for idY, j in enumerate(Cors):
            I = list(i)
            J = list(j)
            if abs(i[1]-j[1])>180:
                if i[1]>90:
                    I[1] = 180 - i[1]
                if i[1]<-90:
                    I[1] = -180 - i[1]
                if j[1]>90:
                    J[1] = 180 - j[1]
                if j[1]<-90:
                    J[1] = -180 - j[1]
                
            dis = euclidean_distance(I,J)
            if dis < ND and dis > 0:
                ND = dis
                IDY = idY
                
        distance.append(ND)
        nn_id.append(int(Ids[IDY]))
        origin_id.append(int(Ids[idX]))
        
    return list(zip(origin_id, nn_id, distance))
#

def nearest_airport1(origin_airport, points):
    # don't calculate d_{i,i}
    nnd = math.inf
    closest_j = math.inf
    i = origin_airport
    for j, point in enumerate(points):
        d_ip = euclidean_distance(points[i], point)
        if d_ip != 0:
            if d_ip < nnd:
                nnd = d_ip
                closest_j = j
    return closest_j, nnd

def MDIS(i,lat,lon):
    
    #global data = points.read_csv('airports.csv')
    #global lat = to_float(points.get_attribute(data, 'latitude'))
    #lon = to_float(points.get_attribute(data, 'longitude'))
    min_lat = min(lat)
    min_lon = min(lon)
    max_lat = max(lat)
    max_lon = max(lon)
    max_distance = euclidean_distance((min_lat, min_lon), (max_lat, max_lon))
    points = list(zip(lon, lat))
    firstpoint = points[i]
    min_distance = max_distance
    min_id = 0
    SNF = 0
    for SJLSDR, SFN in enumerate(points):
        if SJLSDR != i:
            d = euclidean_distance(firstpoint,SNF)
            if d < min_distance:
                min_distance = d
                min_id = SJLSDR
    return (i, min_id, min_distance)