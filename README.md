#PageRank on an Airports' Network


==============================================================================================================================
                                              Description
==============================================================================================================================
This program applies the "PageRank" algorithm to an airports and routes network. The network was built by taking the airports
as nodes and the routes between them were represented by directed weighted edges. The weight in an edge from airport i to 
an airport j$depends on the number of routes between these airports.

==============================================================================================================================
                                              Requirements
==============================================================================================================================
The scripts were developed using:
Python 3.4
Libraries
  -PANDAS (version 0.17.0 )
  -Numpy (version 1.9.1)

==============================================================================================================================
                                              Instructions
==============================================================================================================================
There are four folders:

1. Data:

  -airports.txt: Contains a list of airports from the world. The first fields are: an OpenFlights, airport identifier, name of the
  airport, main city it serves, country, 3 letter IATA code, 4 letter ICAO code, and other stu↵. (Only major airports have IATA codes). 
  As an example, the first two lines of this file are as follows:
  1,"Goroka","Goroka","Papua New Guinea","GKA","AYGA",-6.081689,145.391881,5282,10,"U"
  2,"Madang","Madang","Papua New Guinea","MAG","AYMD",-5.207083,145.7887,20,10,"U"
  
  -routes.txt:  contains a list of routes from the world. The first fields are: an airline code, an OpenFlights airline code, 
  an origin airport code (3 letter IATA code or 4 letter ICAO code), same with OpenFlight code, a destination airport code
  (3 letter IATA code or 4letter ICAO code), then other stuff. In case of doubt about the file contents or decoding, go to OpenFlights
  page. As an example, the first two lines of this file are as follows:
  2B,410,AER,2965,ASF,2966,,0,CR2
  2B,410,AER,2965,GOJ,4274,,0,CR2
  
2. Source: Python scripts:

  - Graph.py, this file contains the preprocessing of the data to construct the most suitable airport’s network from airports.txt 
  and routes.txt files. It also calls the function PageRank from the script PageRank.py and print and save in a txt. file the page rank
  values of each airport in descendant order.
  
  - PageRank.py, computes the algorithm for the PageRank.

3. Results:
Here, some results and performance analysis are given for the sake of reproducibility.

  - Routes_90.csv, the PageRank results for the airports when the damping factor is 0.90 and the tolerance error 1E-5.
  
  - Routes_85.csv, the PageRank results for the airports when the damping factor is 0.85 and the tolerance error 1E-5
  
  -Page_Rank_Performance.txt, gives a detail information about the performance of the PageRank computation in the airports network.
  
4. Documentation:

  -pagerank_airports_network.pdf - Full description, theory, implementation, and results are provided. 

