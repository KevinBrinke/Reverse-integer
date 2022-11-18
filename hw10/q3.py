#Kevin Brinke R01423368


def shortestDistance(points):
    minDistance = float('inf')  # set minDistance to infinity
    pointA = []  # list to hold 1st point current. referenced by i
    pointB = []  # list to hold point compared referenced by j
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
#Find distance between points (0=x,1=y,2=z) and i is current first pointA, j is compared second pointB \\\\ will compare current point with all other points to the right of current i point
            distance = ((points[i][0] - points[j][0]) **2 + (points[i][1] - points[j][1]) **2 + (points[i][2] - points[j][2]) **2)**(1/2)
            if distance < minDistance:  
                minDistance = distance  # set minDistance to calculated distance if it is less
                pointA = points[i]  # set pointA with current point/coordinates[x,y,z]
                pointB = points[j]  # set pointB to compared pointcoordinates

    print('The two points closest are:', pointA, 'and', pointB)


points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1], [2, 0.5, 9],
          [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2], [5.5, 4, -0.5]]
shortestDistance(points)