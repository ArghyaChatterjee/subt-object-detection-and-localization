#! /usr/bin/env python

# Create & Open the file for writing
# Use your pc user name in place of 'user' in the path
dataFile = open('/home/user/darknet/data/test.txt', 'w')

# Loop through 1 to 271 to write it to the output file.
for i in range (1351, 1501) :
    dataFile.write('data/test/'+str(i)+'.jpg'+'\n')

# Close the output file
dataFile.close()