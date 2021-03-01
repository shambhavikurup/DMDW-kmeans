def InitializeMeans(items, k, Min, Max): 
    
    f = len(items[0]); 
   
    for centroid in means[for j in range(k)]: 
        for i in range(len(centroid)): 
            centroid[i] = uniform(Min[i]+1, Max[i]-1); 
  
    return means; 
