# Roadtimes
This is an approximation of a possible way to solve the problem I Road Times of the ACM ICPC World Finals 2016.

## First part
This problem has two rather independent components. The first component is to compute the shortest paths between the a and b (one-way direction). This part can be solved using Dijkstra’s algorithm.

## Second part

I have tested to get a min/max time using a normal distribution, but didn't included it in the code because the results were not close of those expected.

In order to optimize minimum and maximum times and speeds, it is required a linear programming approach and run a Simplex algorithm.

Haven't tested a combinatorial approach because execution time would not be optimal and algorithm would have problems to scale.

Min and max times are calculated using a fixed speed of 60 and 30.

# Dijkstra

Used Maria's Dijkstra algorithm implementation on python with modifications.
https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

# Run
python3 main.py
