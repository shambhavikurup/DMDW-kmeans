def CalculateMeans(k, items):
  Min, Max = AttributeMinMax(13,11); #finding minimum and maximum value of the points in the dataset
  means = InitializeMeans(k, Min, Max); #initiali
  
  clusterLength= [0 for i in range(len(means))]; #array to hold number of items in a cluster
  belonging = [0 for i in range(len(items))]; #array to hold the cluster an item is in

  for e in range(100000): 
    noChange = True; 
    for i in range(len(items)): 
      item = items[i]; 
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
  
