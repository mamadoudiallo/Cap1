# UPDATE: try this one out

import math
import csv

latitude = float(input("Please enter a latitude: "))
longitude = float(input("Please enter a longitude: "))


def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees

    return dist


csvmod = "listings.csv"
file = open(csvmod, newline='')
reader = csv.reader(file)

header = next(reader)
data=[]
location_list = []
dist = []
smallest = 1000000
location = []
distance = []
count = 0
stp = []
for row in reader:
    lat2 = float(row[48])
    long2 = float(row[49])
    # data.append([fltlat, fltlong])
    # distance.append(distance_between(latitude, longitude, lat2, long2))
    distance = (distance_between(latitude, longitude, lat2, long2))
    if distance < smallest:
        smallest = distance
        location.append(row)

location.sort()
low1 = location[0]
low2 = location[1]
low3 = location[2]
low4 = location[3]
low5 = location[4]

full_list = []
full_list.append(low1)
full_list.append(low2)
full_list.append(low3)
full_list.append(low4)
full_list.append(low5)

# price = []
# values = 5
#
# for i in full_list:
#     price.append(i[60])
# print(price)

price = []
for i in full_list:
    price.append(i[60])

final_list = []
for value in price:
    new = value.strip('$.')
    final_list.append(new)

intofvalues = []
for value in final_list:
    fin = float(value)
    intofvalues.append(fin)

intofvalues.sort()
avg = sum(intofvalues) / 5
minimum = min(intofvalues)
maximum = max(intofvalues)
print(avg)
print(full_list)
