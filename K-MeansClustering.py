
def DistanceBetweenPoints(a, b):
    S = 0;
    for i in range(len(x)):
        S = S + (a[i] - b[i])**2  #calculates sum of squared differences
    distance = S**(0.5);
    return distance

def AttributeMinMax(rows, n): #input rows[i]
    minimum = rows[0][n];
    maximum = rows[0][n];
    for i in range(len(rows)): #looping over all records 
        if(rows[i][n]<minimum):
            minimum = rows[i][n]  #reassign the value if new value is less than the current minimum value
        if(rows[i][n]>maximum):
            maximum = rows[i][n] #reassign the value if new value is more than the current maximum value
    return minimum, maximum 

def Assign(means, item): #inputs array of means and selected item
    minimum = 100000;  
    index = -1;
    for i in means[k]: 
        distance = DistanceBetweenPoints(item, means[i])  #calculate Euclidian Distance
        if(distance < minimum): 
            minimum = distance;
            index = i;     #finds the mean with the minimum distance from the item
    return index

