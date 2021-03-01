import csv 

filename = "fires-extended.csv"
  
attributes = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: #opening file in read mode
    filereaderobj = csv.reader(csvfile) 
    attributes = next(filereaderobj) #return current record = record containing attribute names
    for row in filereaderobj: 
        rows.append(row) 
    #rows[] is the array of records. each rows[i] is one record
    #so rows is a list of lists. length of rows[] is the number of records in the dataset
    print("Total no. of records: %d"%(filereaderobj.line_num)) 
  
print('Attributes of the dataset are: ' + ', '.join(attribute for attribute in attributes)) 
  

print('\nLatitude, longitude of first 5 records are:\n') 
for row in rows[:5]: 
    print(row[2] + ": " + row[0] + ", " + row[1])

