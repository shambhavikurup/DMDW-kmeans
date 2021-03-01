def InitializeMeans(items, k, Min, Max): 
    for i in range k: 
  
     centroid[i] = uniform(Min[i]+1, Max[i]-1); 
     if(EuclideanDistance(centroid[i],centroid[i-1])<0.1):
         centroid[i] = uniform(Min[i]+1, Max[i]-1); 
      
        
     
    return centroid[]; 
