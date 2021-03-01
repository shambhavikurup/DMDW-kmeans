from random import uniform

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

def InitializeCentres( k, Min, Max): 
    
    for centroid in centres[k]: 
        for i in range(len(centroid)): 
            centroid[i] = uniform(Min[i]+1, Max[i]-1); 
  
    return centres; 

def Assign(centres, item): #inputs array of means and selected item
    minimum = 100000;  
    index = -1;
    for i in range(k): 
        distance = DistanceBetweenPoints(item, centres[i])  #calculate Euclidian Distance
        if(distance < minimum): 
            minimum = distance;
            index = i;     #finds the mean with the minimum distance from the item
    return index

def FindClusters(centres, rows):
    Clusters = [[] for i in range(k)];
    for item in rows:
        index = Assign(centres, item);  #finds index of centroid closest to item
        Clusters[index].append(item);  #adds item to its cluster
    return Clusters;

def UpdateCentroid(n, centroid, item): #n is the number of items in that cluster, item is the datapoint in that cluster
    for i in range(len(centroid)): 
        m = centroid[i];  #taking in the value of the current centroid
        m = (m*(n-1)+item[i])/float(n); #finding the average of the points and recalculating m
        centroid[i] = round(m, 3); 
      
    return centroid;

def CalculateCentres(k, rows):
  Attributes = [9, 11] #finding minimum and maximum value of the points in the dataset
  for i in range(2):
      Min[i], Max[i] = AttributeMinMax(rows, Atrributes[i]);

  centres = InitializeCentres(k, Min, Max); #initiali
  
  clusterLength= [0 for i in range(len(centres))]; #array to hold number of items in a cluster
  belonging = [0 for i in range(len(rows))]; #array to hold the cluster an item is in

  for e in range(100000): 
    noChange = True; 
    for i in range(len(rows)): 
      item = rows[i]; 
      index = Assign(centres,item); #assigning items into a cluster
      clusterLength[index] = clusterLength[i] + 1; 
      cSize = clusterLength[index]; 
      centres[index] = UpdateCentroid(cSize,centres[index],item); 
      
      if(index != belongsTo[i]): 
        noChange = False; 
        belonging[i] = index; 
        
        
    if (noChange): 
            break; 
  
    return centres;