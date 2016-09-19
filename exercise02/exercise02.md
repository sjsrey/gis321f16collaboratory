## Instructions

This exercise uses the airport data in `data.csv`. To complete your assignment submit one text file that lists the shell commands you used to answer the following questions.

1. How many unique countries are in the data set?
2. How many unique cities are in the data set?
3. How would you create a new file called `sorted_lat.csv` that ordered the airports from most northern to most southern?
4. Find the following airports:
	- The western most airport in the northern hemisphere
	- The western most airport in the southern hemisphere
	- The southern most airport in the western hemisphere
	- The northern most airport in the eastern hemisphere


Quan Zhou
Assignment 1 for GIS321


Quan@QuanZhou MINGW64 ~/Documents
$ grep -v 'airport_id' data.csv |cut -d , -f 4-4 | sort | uniq | wc -l
245

Quan@QuanZhou MINGW64 ~/Documents
$ grep -v 'airport_id' data.csv |cut -d , -f 3-4 | sort | uniq | wc -l
6204 # this is my update code. Because there are many different cities in different countries share the same name.

Quan@QuanZhou MINGW64 ~/Documents
$ grep -v 'airport_id' data.csv |sort -n -k7,7 -r -t , -o sorted_lat.csv

Quan@QuanZhou MINGW64 ~/Documents
$ awk -F ',' '{if($7>0)print $0}' data.csv | sort -n -k8,8 -t , | head -1
2253,Midway Atoll,Midway,Midway Islands,MDY,PMDY,28.201725,-177.380636,13,-11,U

Quan@QuanZhou MINGW64 ~/Documents
$ awk -F ',' '{if($7<0)print $0}' data.csv | sort -n -k8,8 -t , | head -1
5875,Matei Airport,Matei,Fiji,TVU,NFNM,-16.6906,-179.877,60,12,U

Quan@QuanZhou MINGW64 ~/Documents
$ awk -F ',' '{if($8<0)print $0}' data.csv | sort -n -k7,7 -t , | head -1
6437,South Shetland,South Shetland,Antarctica,,,-68,-58,0,-4,N

Quan@QuanZhou MINGW64 ~/Documents
$ awk -F ',' '{if($8>0)print $0}' data.csv | sort -n -k7,7 -t , | tail -1
7452,Ny-Alesund Airport,Ny-Alesund,Svalbard,,ENAS,78.9275,11.874167,50,1,U

