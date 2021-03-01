def InitializeMeans( k, Min, Max): 
    
    for centroid in means[for j in range(k)]: 
        for i in range(len(centroid)): 
            centroid[i] = uniform(Min[i]+1, Max[i]-1); 
  
    return means; 
