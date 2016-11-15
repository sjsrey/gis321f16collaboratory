import math
import csv


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx*dx + dy*dy)



def read_csv(file_name):
    newlines = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            newlines.append(line)
    return newlines


def get_attribute(data, attribute_name):
    header = data[0]
    idx = header.index(attribute_name)
    return [record[idx] for record in data[1:]]


def to_float(attribute_list):
    return list(map(float, attribute_list))

def Min_distance(i):
    data = read_csv('airports.csv')
    lat = to_float(get_attribute(data, 'latitude'))
    lon = to_float(get_attribute(data, 'longitude'))
    min_lat = min(lat)
    min_lon = min(lon)
    max_lat = max(lat)
    max_lon = max(lon)
    max_distance = distance((min_lat, min_lon), (max_lat, max_lon))
    points = list(zip(lon, lat))
    firstpoint = points[i]
    min_distance = max_distance
    min_id = 0
    for SJLSDR, SFN in enumerate(points):
        if SJLSDR != i:
            d = distance(firstpoint,SNF)
            if d < min_distance:
                min_distance = d
                min_id = SJLSDR
    return (i, min_id, min_distance)

def airport_list():
    data = read_csv('airports.csv')
    lat = to_float(get_attribute(data, 'latitude'))
    lon = to_float(get_attribute(data, 'longitude'))
    airports = []
    points = list(zip(lon, lat))
    for SP in enumerate(points):
        airports.append(Min_distance(SP))
    return airports

def findFurthestNeighbor ():
    airports = airport_list()
    max_distance = 0
    airport1 = 1
    airport2 = 3
    for SJLSDR in enumerate(airports):
        if float(airports[SJLSDR][2]) > max_distance:
            max_distance = float(airports[SJLSDR][2])
            airport1 = float(airports[SJLSDR][0])
            airport2 = float(airports[SJLSDR][1])
    return airport1, airport2, max_distance
def mostIsolated_1():
    airports = airport_list()
    max_distance = 0
    airportId = 0
    for SJLSDR in enumerate(airports):
        airport2 = airport[SJLSDR][1]
        if airports[SJLSDR][2] > max_distance:
            if airports[SJLSDR][2] == airports[airport2][2] :
                airportId = airports[SJLSDR][0]
                max_distance = airports[SJLSDR][2]
    return airportId, max_distance

def HavercineDistance(point1, point2): # Havercine equation is from http://mathworld.wolfram.com/GreatCircle.html
    lat1, long1 = point1
    lat2, long2 = point2
    distance = 6378 * (math.acos((math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)) + (math.sin(lat1) * math.sin(lat2)))) # 6378 kilometers fron the website
    return distance

def Min_distance_2(i):
    data = read_csv('airports.csv')
    lat = to_float(get_attribute(data, 'latitude'))
    lon = to_float(get_attribute(data, 'longitude'))
    min_lat = min(lat)
    min_lon = min(lon)
    max_lat = max(lat)
    max_lon = max(lon)
    max_distance = HavercineDistance((min_lat, min_lon), (max_lat, max_lon))
    points = list(zip(lon, lat))
    firstpoint = points[i]
    min_distance = max_distance
    min_id = 0
    for SJLSDR, SFN in enumerate(points):
        if SJLSDR != i:
            d = HavercineDistance(firstpoint,SNF)
            if d < min_distance:
                min_distance = d
                min_id = SJLSDR
    return (i, min_id, min_distance)


def airport_list_2():
    data = read_csv('airports.csv')
    lat = to_float(get_attribute(data, 'latitude'))
    lon = to_float(get_attribute(data, 'longitude'))
    airports = []
    points = list(zip(lon, lat))
    for SP in enumerate(points):
        airports.append(Min_distance_2(SP))
    return airports

def findFurthestNeighbor ():
    airports = airport_list_2()
    max_distance = 0
    airport1 = 1
    airport2 = 3
    for SJLSDR in enumerate(airports):
        if float(airports[SJLSDR][2]) > max_distance:
            max_distance = float(airports[SJLSDR][2])
            airport1 = float(airports[SJLSDR][0])
            airport2 = float(airports[SJLSDR][1])
    return airport1, airport2, max_distance

def mostIsolated_1():
    airports = airport_list_2()
    max_distance = 0
    airportId = 0
    for SJLSDR in enumerate(airports):
        airport2 = airport[SJLSDR][1]
        if airports[SJLSDR][2] > max_distance:
            if airports[SJLSDR][2] == airports[airport2][2] :
                airportId = airports[SJLSDR][0]
                max_distance = airports[SJLSDR][2]
    return airportId, max_distance
            
            
