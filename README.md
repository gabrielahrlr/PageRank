These flies, jointly, compute the Page Rank of an airports’  network.

This folder contains the following files:

1. Graph.py, this file contains the preprocessing of the data to construct
the most suitable airport’s network from airports.txt and routes.txt files. It also calls the function PageRank from the script PageRank.py and print and save in a txt. file the page rank values of each airport in descendant order.

2.PageRank.py, computes the algorithm for the PageRank.

3. airports.txt, the original airports given.

4. routes.txt, the original routes give.

5. Routes_90.csv, the PageRank results for the airports when the damping
factor is 0.90 and the tolerance error 1E-5.

6. Routes_85.csv, the PageRank results for the airports when the damping
factor is 0.85 and the tolerance error 1E-5.

7.Page_Rank_Performance.txt, gives a detail information about the performance
of the PageRank computation in our airports.

Please notice that for running the scripts it is necessary to place the files
Graph.py, PageRank.py, airports.txt and routes.txt in the same folder. The libraries
PANDAS (version 0.17.0 ) and Numpy (version 1.9.1) are also required.
