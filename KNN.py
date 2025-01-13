import math

def classifyAPoint(points, p, k = 3):
    distance = []
    for group in points:
        for feature in points[group]:
            manhattan_distance = math.sqrt(abs(feature[0] - p[0]) + abs(feature[1]-p[1]))
            distance.append((manhattan_distance, group))
    distance = sorted(distance)[:k]
    count0 = 0
    count1 = 1
    for i in distance:
        if(i[1]==0):
            count0 += 1
        else:
            count1 += 1
    if(count0 > count1):
        return 0
    return 1


def main():

    points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}

    p = (10,7)

    k = 3

    print("The value classified to unknown point is: {}".\
          format(classifyAPoint(points,p,k)))

if __name__ == '__main__':
    main()