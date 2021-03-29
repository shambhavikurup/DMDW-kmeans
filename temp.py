#Anjali Sajith        1020191420
#Stuti Khandelwal     1020191308
#Shambhavi Kurup      1020191577

from random import uniform
import csv 

  
def DistanceBetweenPoints(a, b):
    S = 0
    for i in range(len(a)):
        S = S + (float(a[i]) - float(b[i]))*(float(a[i]) - float(b[i]))  #calculates sum of squared differences
    distance = S**(0.5)
    return distance

def AttributeMinMax(rows, n): #input rows[i]
    #ours
    minimum = rows[0][n]
    maximum = rows[0][n]
    #theirs
    # n = len(items[0])
    # minima = [sys.maxint for i in range(n)]
    # maxima = [-sys.maxint -1 for i in range(n)]
    for i in range(len(rows)): #looping over all records 
        if(rows[i][n]<minimum):
            minimum = rows[i][n]  #reassign the value if new value is less than the current minimum value
        if(rows[i][n]>maximum):
            maximum = rows[i][n] #reassign the value if new value is more than the current maximum value
    return minimum, maximum 

def InitializeCentres( k, Min, Max): 
    
    centres = [[0 for i in range(2)] for j in range(k)]
    
    for centre in centres: 
        for i in range(2): 
            centre[i] = uniform(float(Min[i])+1, float(Max[i])-1)
  
    return centres

def Assign(centres, item): #inputs array of means and selected item
    minimum = 100000
    index = -1
    for i in range(len(centres)): 
        for j in range(2):
            distance = DistanceBetweenPoints(item[j], centres[i])  #calculate Euclidian Distance
            if(distance < minimum): 
                minimum = distance
                index = i    #finds the mean with the minimum distance from the item
    return index

def FindClusters(centres, rows):
    Clusters = [[] for i in range(len(centres))]
    for item in rows:
        index = Assign(centres, item)  #finds index of centroid closest to item
        Clusters[index].append(item)  #adds item to its cluster
    return Clusters

def UpdateCentre(n, centre, item): #n is the number of items in that cluster, item is the datapoint in that cluster
    for i in range(len(centre)): 
        m = centre[i]  #taking in the value of the current centroid
        m = (m*(n-1)+float(item[i]))/float(n) #finding the average of the points and recalculating m
        centre[i] = round(m, 3)
      
    return centre

def CalculateCentres(k, rows):
    Min = [0,0]
    Max = [0,0]
    Attributes = [9, 11] #finding minimum and maximum value of the points in the dataset
    for i in range(2):
        Min[i], Max[i] = AttributeMinMax(rows, Attributes[i])

    centres = InitializeCentres(k, Min, Max) #initializing random centres
  
    clusterLength= [0 for i in range(len(centres))] #array to hold number of items in a cluster
    liesIn = [0 for i in range(len(rows))] #array to hold the cluster an item is in
    e = 0
    constant = True
    while (constant==True or e<100000): 
        item = [0,0]
        for i in range(len(rows)): 
            for j in range(2):
                item[j] = rows[i][Attributes[j]]  #extracting the data of two relevant attributes from the rows
            index = Assign(centres,item[i]) #assigning items into a cluster
            clusterLength[index] = clusterLength[i] + 1 
            cSize = clusterLength[index]
            centres[index] = UpdateCentre(cSize,centres[index],item)
        
            if(index != liesIn[i]): 
                constant = False
                liesIn[i] = index 
        e += 1
    
    return centres
  
  
  
def main():
    filename = "fires-extended.csv" #chosen dataset
    rows = [] 

    # parsing csv file 
    with open(filename, 'r') as csvfile:        #opening file in read mode
        filereaderobj = csv.reader(csvfile)     #creating a csv file reader object
        for row in filereaderobj: 
            rows.append(row) 
        #rows[] is the array of records. each rows[i] is one record. len(rows) = number of records in the dataset
        #filereaderobj.line_num = total number of records in dataset
    rows.pop(0)

    Centres = CalculateCentres(20, rows)
    print(Centres)
    Clusters = FindClusters(Centres, rows)
    print(Centres + "\n")
    print(Clusters)

main()
