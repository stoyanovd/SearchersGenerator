import random

oid = 1

art = {"detectionDistance": 5.0, "explorationDuration": 0, "explorationStartDate": 0, "id": 0, "latitude": 44.991005,
       "longitude": 41.915257, "name": "Чехарда.x0.y0", "playerId": 0, "scenarioId": 1, "state": 0, "type": 0,
       "value": "100", "visible": False, "zoneId": 6}

for i in range(4):
    f = art
    f.update({"id": oid, "latitude": 44.991195, "longitude": 41.914105, "name": "Таган.верх." + str(i), "type": 0,
              "zoneId": 3})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

for i in range(4):
    f = art
    f.update({"id": oid, "latitude": 44.990588, "longitude": 41.914990, "name": "Таган.право." + str(i), "type": 0,
              "zoneId": 4})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

for i in range(4):
    f = art
    f.update({"id": oid, "latitude": 44.989924, "longitude": 41.913872, "name": "Таган.низ." + str(i), "type": 0,
              "zoneId": 5})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

# -------------------------


for i in range(10):
    f = art
    f.update({"id": oid, "latitude": 44.992625, "longitude": 41.916695, "name": "Обзор." + str(i), "type": 0,
              "zoneId": 10})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

for i in range(8):
    f = art
    f.update({"id": oid, "latitude": 44.992241, "longitude": 41.914313, "name": "Длинная." + str(i), "type": 0,
              "zoneId": 9})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

for i in range(14):
    f = art
    f.update({"id": oid, "latitude": 44.991660, "longitude": 41.913015, "name": "Горы." + str(i), "type": 0,
              "zoneId": 7})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

# ------------------------

x = 44.990699
y = 41.904913
dx = 0.00020
dy = 0.00020

for i in range(4):
    f = art
    f.update({"id": oid, "latitude": x - dx, "longitude": y - dy, "name": "Сапер.Глаз." + str(i), "type": 0,
              "zoneId": 8})
    s = str(f)
    oid += 1
    s.replace("'", '"')
    s.replace("False", 'false')
    print(s)

for i in range(6):
    for j in range(6):
        s = '{"detectionDistance":5.0, "explorationDuration":0, "explorationStartDate":0, "id":' + \
            str(oid) + \
            ', "latitude":' + str(x - i * dx) + ', "longitude":' + str(y + j * dy) + ', "name":' + \
            '"Сапер.x' + str(i) + '.y' + str(j) \
            + '", "playerId":0, "scenarioId":1, "state":0, "type":' + str(random.randint(0, 1)) + \
            ', "value":"100", "visible":false, "zoneId":8}'
        print(s)
        oid += 1
# ------------------------
x = 44.991005
y = 41.915217

dx = 0.00002
drx = 0.00005

dy = 0.00015

for i in range(10):
    for j in range(2):
        s = '{"detectionDistance":2.5, "explorationDuration":0, "explorationStartDate":0, "id":' + \
            str(oid) + \
            ', "latitude":' + str(x + i * dy) + ', "longitude":' + str(y + i * dx + j * drx) + ', "name":' + \
            '"Чехарда.x' + str(i) + '.y' + str(j) \
            + '", "playerId":0, "scenarioId":1, "state":0, "type":' + str((j + i) % 2) + \
            ', "value":"100", "visible":false, "zoneId":6}'
        print(s)
        oid += 1
