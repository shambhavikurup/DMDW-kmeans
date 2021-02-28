def UpdateCentroid(n, centroid, item): #n is the number of items in that cluster, item is the datapoint in that cluster
    for i in range(len(centroid)): 
        m = centroid[i];  #taking in the value of the current centroid
        m = (m*(n-1)+item[i])/float(n); #finding the average of the points and recalculating m
        centroid[i] = round(m, 3); 
      
    return centroid;
