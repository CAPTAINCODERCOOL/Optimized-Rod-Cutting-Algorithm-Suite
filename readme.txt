Rod Cutting Algorithm Analysis
Overview
This project implements and analyzes three rod-cutting algorithms:

Cut Rod: A recursive solution with cuts tracking.
Bottom-Up Cut Rod: An iterative dynamic programming solution.
Extended Bottom-Up Cut Rod: An extended solution with both maximum revenue and cut tracking.
The project includes a comparison script (comp_analysis.py) that runs the algorithms, measures their execution times, and visualizes their performance.

Prerequisites

Python Version: Python 3.7 or later.
Dependencies:
matplotlib for generating graphs.
Environment:
Ensure all the scripts are in the same directory.
Input Format
The input.txt file specifies the problem parameters:

Line 1: The length of the rod (n).
Line 2: A space-separated list of prices for each rod length from 1 to n.

Commands to Execute
1. Run Individual Algorithms
Each algorithm script can be executed independently by providing the input.txt file as a command-line argument.

Cut Rod:

python CUT_ROD.py input.txt
Example Output:

Maximum Revenue: 250
Rod Cuts: [8]
Execution Time: 0.001001 seconds
Execution completed successfully.
Bottom-Up Cut Rod:

python BOTTOM_UP_CUT_ROD.py input.txt
Example Output:

Maximum Revenue: 250
Cuts: [8]
Execution Time: 0.000000 seconds
Execution completed successfully.
Extended Bottom-Up Cut Rod:

python EXTENDED_BOTTOM_UP_CUT_ROD.py input.txt
Example Output:

Cut sizes that maximize revenue: [8]
Maximum Revenue: 250
Execution Time: 0.000000 seconds
Execution completed successfully.
2. Run the Comparison Analysis
To compare the performance of all three algorithms and generate visualizations:

python comp_analysis.py input.txt
Output
The comp_analysis.py script:

Executes all three algorithms and displays their outputs.
Measures and compares their execution times.
Generates two graphs:
execution_comparison_all_algorithms.png: Shows execution times for all three algorithms.
time_difference_graph.png: Displays the time difference between CUT_ROD and BOTTOM_UP_CUT_ROD.
Example Output:

Executing standalone scripts...
Maximum Revenue: 250
Rod Cuts: [8]
Execution completed successfully for python CUT_ROD.py input.txt
Maximum Revenue: 250
Cuts: [8]
Execution completed successfully for python BOTTOM_UP_CUT_ROD.py input.txt
Cut sizes that maximize revenue: [8]
Maximum Revenue: 250
Execution completed successfully for python EXTENDED_BOTTOM_UP_CUT_ROD.py input.txt
Time difference between CUT_ROD and BOTTOM_UP_CUT_ROD exceeded 60 seconds at rod length 27.
Cuts: [8]
Maximum Revenue: 250
How to Execute
Clone or download the project files into a directory.
Install the required Python dependencies:
pip install matplotlib
Prepare the input.txt file with the desired rod length and prices.
Run individual scripts or the comp_analysis.py for comparison.


FOR THE GRAPH AFTER FIRST GRAPH IS GENERATED THEN PRESS X (CLOSE) ON THE GRAPH TO SEE THE SECOND GRAPH AS WELL.
REST ALL IS ALMOST THE same