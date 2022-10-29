from math import *
class LezerLoveszet():
    def __init__(self, txt):
        self.nev = txt[0]
        self.x = makeFloat(txt[1].split(","))
        self.y = makeFloat(txt[2].split(","))
        self.dif = getDif(self)
        self.point = getPoint(self)
    
    def displayItSelf(self, num):
        return f"\n        {num+1}.; {self.nev}; x={self.x}; y={self.y}; távolság: {self.dif}"
class tabla():
    def __init__(self, txt):
        self.x = makeFloat(txt[0].split(","))
        self.y = makeFloat(txt[1].split(","))

tablakozepe = []

def makeFloat(list):
        return float(f"{list[0]}.{list[1]}")

def getDif(obj):
    xdif = tablakozepe[0].x - obj.x
    ydif = tablakozepe[0].y - obj.y
    return sqrt(xdif**2 + ydif**2)

def getPoint(obj):
    if (10 - obj.dif) < 0:
        return 0
    return (10 - obj.dif)

def countZero(list):
    temp = 0
    for i in range(len(list)):
        if list[i].point == 0:
            temp += 1
    return temp

def findAllPlayers(list):
    temp = []
    for i in range(len(list)):
        if list[i].nev not in temp:
            temp.append(list[i].nev)
    return temp

def statMember(list, type, win):
    temp = ""
    temp_most_points = 0
    name = []
    var = findAllPlayers(list)
    for i in var:
        count_num = 0
        all_points = 0
        for j in list:
            if j.nev == i:
                count_num += 1
                all_points += j.point
        if type == 0:
            temp += f"\n        {i} - {count_num} db"
        else:
            temp += f"\n        {i} - {all_points/count_num}"
            if all_points/count_num > temp_most_points:
                temp_most_points = all_points
                name.append(i)
    if win != 1:
        return temp
    return name[-1]

def importFromTXT():
    temp = []
    f = open("lovesek.txt", "r").read()
    lines = f.split("\n")
    j = 0
    for i in lines:
        if j > 0:
            temp.append(LezerLoveszet(i.split(";")))
        else:
            tablakozepe.append(tabla(i.split(";")))
            j += 1
    return temp

def findNearest(list):
    temp = 0
    for i in range(len(list)):
        if list[temp].dif > list[i].dif:
            temp = i
    return list[temp].displayItSelf(temp)

def main():
    main_list = importFromTXT()
    print(f"5. feladat: Lövések száma: {len(main_list)} db")
    print(f"7. feladat: Legpontosabb lövés: {findNearest(main_list)}")
    print(f"9. feladat: Nulla pontos lövések száma {countZero(main_list)} db")
    print(f"10.feladat: Játékosok száma: {len(findAllPlayers(main_list))}")
    print(f"11.feladat: Lövések száma {statMember(main_list, 0, 0)}")
    print(f"12.feladat: Átlagpontszámok {statMember(main_list, 1, 0)}")
    print(f"13. feladat: A játék nyertese: {statMember(main_list, 1, 1)}")

main()