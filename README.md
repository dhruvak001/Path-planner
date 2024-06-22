# Path planner

***Samples file is the Dataset** </br>

The Metro Route Planner is a Python program designed to help users find the shortest path between two metro stations in a fictional metro network. It utilizes various classes such as MetroStop, MetroLine, AVLNode, AVLTree, Trip, Exploration, Path, and PathFinder to represent metro stops, metro lines, AVL trees for efficient searching, trip exploration, and pathfinding algorithms.


# **Usage:**
- Create instances of MetroLine for each metro line and populate them with stop information from respective files.</br>
- Create an instance of AVLTree and populate it with all metro lines.</br>
- Create an instance of PathFinder with the AVL tree and a list of metro lines.</br>
- Define origin and destination station names as strings.</br>
- Search for the corresponding MetroStop objects using the AVL tree.</br>
- If both origin and destination stations are found, use the PathFinder to find the shortest path between them.</br>
- Print the path and total fare for the journey.</br>

# **Note:**
Replace the file paths in the example usage with actual file paths containing metro stop information.</br>
Ensure that the file format matches the expected format for populating metro lines.</br>
Customize fare calculation logic in the calculate_fare_between_stops method as needed.

# Code Overview (if you need any particular function):

MetroStop: Represents a metro station with attributes such as name, metro line, fare, and methods to retrieve station information.</br>
MetroLine: Represents a metro line with methods to add stops, print line details, and populate line information from a file.</br>
AVLNode: Represents a node in an AVL tree used for efficient searching of metro stops.</br>
AVLTree: Represents an AVL tree data structure used for efficient searching and insertion of metro stops.</br>
Trip: Represents a trip between metro stops.</br>
Exploration: Represents exploration of metro stops during pathfinding.</br>
Path: Represents a path consisting of metro stops and calculates total fare for the path.</br>
PathFinder: Implements algorithms to find the shortest path between two metro stops.
