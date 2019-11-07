# merJson

Utility to merge a series of files containing JSON array of Objects
into a single file containing one JSON object.

## Run
python3 main.py

## Tests
python3 test.py

## Time Complexity Analysis 

If there are N files each with size M. 
Time complexity  will be O(MN).

All other extra operations will be bounded by this complexity.
For example parsing json data to a python dictionary is linear complexity with respect to characters in the json text.

Each file is read once. converted to python dictionary, appended to the result json dictionary.
Insert operations in existing json dictionary are O(1)



## Features

Every time the program is run, new output file is generated with the next valid sequence number in that directory.

Suffices in the input files need not be consecutive integers. The program handles the numeric sorting of these suffixes.
For eg : data1.json , data3.json, data456.json

supporting non-English characters.

any kind of JSON array can
be merged. (e.g.: The root key "strikers" becomes "employees". The objects
in the array carry fields like "name", "id", "designation", etc.)

Merged files will never be greater than Max File Size.

## Env
Developed and tested on Ubuntu 18 with python3.6. 
No external libraries.
