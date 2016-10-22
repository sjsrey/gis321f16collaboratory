
"""
points.py

a module to deal with point patterns

"""

import math
import csv


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx*dx + dy*dy)


def haversine_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    dlat = lat1 - lat2
    dlon = lon1 - lon2
    p1 = (math.sin(dlat/2))**2
    p2 = math.cos(lat1)*math.cos(lat2)
    p3 = (math.sin(dlon/2))**2
    r = 12800*math.asin(math.sqrt(p1+p2*p3))
    
    return r


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

def nearestD_haversine_distance(DataName):
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
                
            dis = haversine_distance(I,J)
            if dis < ND and dis > 0:
                ND = dis
                IDY = idY
                
        distance.append(ND)
        nn_id.append(int(Ids[IDY]))
        origin_id.append(int(Ids[idX]))
        
    return list(zip(origin_id, nn_id, distance))