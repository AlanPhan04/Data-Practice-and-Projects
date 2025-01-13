import math

def classifyAPoint(points, p, k = 3):
    distance = []
    for group in points:
        for features in points[group]:
            euclidean_distance = math.sqrt((features[0]-p[0])**2 + (features[1]-p[1])**2)
            distance.append((euclidean_distance, group))

    distance = sorted(distance)[:k]
    count_group0 = 0
    count_group1 = 0
    for i in distance:
        if(i[1]==0):
            count_group0+=1
        else:
            count_group1+=1
    if(count_group0 > count_group1):
        return 0
    return 1


def main():

    points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}

    p = (2.5,7)

    k = 3

    print("The value classified to unknown point is: {}".\
          format(classifyAPoint(points,p,k)))

if __name__ == '__main__':
    main()