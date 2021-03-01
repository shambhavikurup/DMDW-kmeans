
def DistanceBetweenPoints(x1, x2, y1, y2):
    distance = ((x2 - x1)**2 + (y2- y1)**2)**(0.5)
    return distance

def AttributeMinMax(column): #input rows[i]
    minimum = column[0];
    maximum = column[0];
    for i in range(len(column)): #looping over all records 
        if(rows[i]<minimum):
            minimum = column[i]  #reassign the value if new value is less than the current minimum value
        if(rows[i]>maximum):
            maximum = column[i] #reassign the value if new value is more than the current maximum value
