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

def InitializeMeans( k, Min, Max): 
    
    for centroid in means[k]: 
        for i in range(len(centroid)): 
            centroid[i] = uniform(Min[i]+1, Max[i]-1); 
  
    return means; 

def Assign(means, item): #inputs array of means and selected item
    minimum = 100000;  
    index = -1;
    for i in range(k): 
        distance = DistanceBetweenPoints(item, means[i])  #calculate Euclidian Distance
        if(distance < minimum): 
            minimum = distance;
            index = i;     #finds the mean with the minimum distance from the item
    return index

def FindClusters(means, rows):
    Clusters = [[] for i in range(k)];
    for item in rows:
        index = Assign(means, item);  #finds index of centroid closest to item
        Clusters[index].append(item);  #adds item to its cluster
    return Clusters;

def UpdateCentroid(n, centroid, item): #n is the number of items in that cluster, item is the datapoint in that cluster
    for i in range(len(centroid)): 
        m = centroid[i];  #taking in the value of the current centroid
        m = (m*(n-1)+item[i])/float(n); #finding the average of the points and recalculating m
        centroid[i] = round(m, 3); 
      
    return centroid;

def CalculateMeans(k, rows):
  Attributes = [11, 13] #finding minimum and maximum value of the points in the dataset
  for i in range(2):
      Min[i], Max[i] = AttributeMinMax(rows, Atrributes[i]);

  means = InitializeMeans(k, Min, Max); #initiali
  
  clusterLength= [0 for i in range(len(means))]; #array to hold number of items in a cluster
  belonging = [0 for i in range(len(rows))]; #array to hold the cluster an item is in

  for e in range(100000): 
    noChange = True; 
    for i in range(len(rows)): 
      item = rows[i]; 
      index = Assign(means,item); #assigning items into a cluster
      clusterLength[index] = clusterLength[i] + 1; 
      cSize = clusterLength[index]; 
      means[index] = UpdateCentroid(cSize,means[index],item); 
      
      if(index != belongsTo[i]): 
        noChange = False; 
        belonging[i] = index; 
        
        
    if (noChange): 
            break; 
  
    return means;