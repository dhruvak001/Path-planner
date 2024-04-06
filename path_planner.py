# MetroStop class
from collections import deque

class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line
    
    def set_line(self,line):
        self.line = line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop

# MetroLine class
class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None
        self.stops = []

    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def add_stop(self, stop):
        stop.set_line(self)
        self.stops.append(stop)

    def get_stops(self):
        return self.stops

    def print_line(self):
        stop = self.node
        while stop is not None:
            print(stop.get_stop_name())
            stop = stop.get_next_stop()

    def populate_line(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            prev_stop = None  # Initialize prev_stop to None
            for line in lines:
                stop_info = line.strip().split()
                if len(stop_info) < 2:  # Skip lines with insufficient data
                    continue

                stop_name = " ".join(stop_info[:-1])
                try:
                    fare = int("".join(filter(str.isdigit, stop_info[-1])))  # Convert to int after removing non-numeric characters
                except ValueError:
                    # Handle cases where fare information is not numeric
                    continue

                metro_stop = MetroStop(stop_name, self, fare)

                # Set next_stop and prev_stop attributes
                metro_stop.set_prev_stop(prev_stop)
                if prev_stop:
                    prev_stop.set_next_stop(metro_stop)

                # Update prev_stop to the current metro_stop
                prev_stop = metro_stop

                self.add_stop(metro_stop)  # Add the metro stop to the line's stops list


    def get_total_stops(self):
        return len(self.stops)  # Return the length of the stops list



# AVLNode class
class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None
        self.reference = None
        self.height = 1

    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        metro_stop.set_line(self)
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

    def set_reference(self,reference):
        self.reference = reference

# AVLTree class
class AVLTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.get_left())
        right_height = self.height(node.get_right())
        return max(left_height, right_height) + 1

    def string_compare(self, s1, s2):
        if isinstance(s1, str) and isinstance(s2, str):
            if s1 > s2:
                return 1
            elif s1 == s2:
                return 0
            else:
                return -1 
        return 0

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.get_left()) - self.height(node.get_right())
                
    def rotate_right(self, node):
        left_child = node.get_left()
        
        # Check if left_child has a right child
        if left_child is not None:
            right_subtree = left_child.get_right()
        else:
            right_subtree = None

        if left_child is not None:
        # Perform rotation
            left_child.set_right(node)
            node.set_left(right_subtree)

            # Update heights
            node.height = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
            
            if left_child is not None:
                left_child.height = 1 + max(self.height(left_child.get_left()), self.height(left_child.get_right()))

            return left_child
        return node

    def rotate_left(self, node):
        right_child = node.get_right()
        if right_child is not None:
            left_subtree = right_child.get_left()
        else:
            left_subtree = None

        if right_child is not None:
        # Perform rotation
            right_child.set_left(node)
            node.set_right(left_subtree)

            # Update heights
            node.height = 1 + max(self.height(node.get_left()), self.height(node.get_right()))

            if right_child is not None:
                right_child.height = 1 + max(self.height(right_child.get_left()), self.height(right_child.get_right()))

            return right_child
        return node

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.get_left()) - self.height(node.get_right())

    def insert(self, node, metro_stop):
        if node is None:
            #print("Inserting root:", metro_stop.get_stop_name())
            return AVLNode(metro_stop)  # Use stop_name for comparison

        stop_name1 = metro_stop.get_stop_name().lower()
        stop_name2 = node.get_stop_name().get_stop_name().lower()

        
        #print(stop_name1,"-5-",stop_name2)

        if stop_name1 < stop_name2:
            node.set_left(self.insert(node.get_left(), metro_stop))
        elif stop_name1 > stop_name2:
            node.set_right(self.insert(node.get_right(), metro_stop))
        else:
            # Handle duplicates by adding the metro_stop to the list of stops in the node
            #print("Adding stop to existing node:", metro_stop.get_stop_name())  # Debugging
            node.add_metro_stop(metro_stop)

            # Update the doubly linked list
            stops = node.get_stops()
            if stops:
                last_stop = stops[-1]
                metro_stop.set_prev_stop(last_stop)
                last_stop.set_next_stop(metro_stop)
            else:
                # If there are no stops in the list yet, set the current metro_stop as both next and previous
                metro_stop.set_prev_stop(metro_stop)
                metro_stop.set_next_stop(metro_stop)

        # Update height and balance factor
        node.height = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
        balance = self.balance_factor(node)

        # Balance the tree if needed
        if balance > 1:
            if stop_name1 < node.get_left().get_stop_name().get_stop_name().lower():
                return self.rotate_right(node)
            else:
                node.set_left(self.rotate_left(node.get_left()))
                return self.rotate_right(node)

        if balance < -1:
            if stop_name1 > node.get_right().get_stop_name().get_stop_name().lower():
                return self.rotate_left(node)
            else:
                node.set_right(self.rotate_right(node.get_right()))
                return self.rotate_left(node)

        return node


    def populate_tree(self, metro_line_or_filename):

        for stop in metro_line_or_filename.get_stops():
            #print("Inserting root2:", stop.get_stop_name())  # Debugging
            self.root = self.insert(self.root, stop)
        # elif isinstance(metro_line_or_filename, str):
        #     # If metro_line_or_filename is a string (filename), open the file and add stops
        #     with open(metro_line_or_filename, "r") as file:
        #         lines = file.readlines()
        #         for line in lines:
        #             stop_info = line.strip().split()
        #             if len(stop_info) < 2:  # Skip lines with insufficient data
        #                 continue

        #             stop_name = " ".join(stop_info[:-1])
        #             try:
        #                 fare = int("".join(filter(str.isdigit, stop_info[-1])))  # Convert to int after removing non-numeric characters
        #             except ValueError:
        #                 # Handle cases where fare information is not numeric
        #                 continue

        #             metro_stop = MetroStop(stop_name, self, fare)
        #             print("Inserting root:", metro_stop.get_stop_name())  # Debugging
        #             self.root = self.insert(self.root, metro_stop)  # Add the metro stop to the tree

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        print(node.get_stop_name())
        self.in_order_traversal(node.get_right())

    def get_total_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.get_total_nodes(node.get_left()) + self.get_total_nodes(node.get_right())

    def search_stop(self, stop_name, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        node_stop_name = node.get_stop_name().get_stop_name().lower()  # Convert to lowercase for comparison
        stop_name = stop_name.lower()  # Convert the input to lowercase

        if stop_name == node_stop_name:
            return node

        if stop_name < node_stop_name:
            return self.search_stop(stop_name, node.get_left())
        else:
            return self.search_stop(stop_name, node.get_right())

        
    def print_tree(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.print_tree(node.get_left())
            print(node.get_stop_name(), "Balance Factor:", self.balance_factor(node), "Height:", node.height)
            self.print_tree(node.get_right())

    @staticmethod
    def is_junction(node):
        if len(node.getStops()) > 1:
            return True
        else:
            return False


# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip

    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev
    
# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []

    def get_trips(self):
        return self.trips
    
    def enqueue(self, trip):
        self.trips.append(trip)

    def dequeue(self):
        if not self.trips:
            return None
        trip = self.trips.pop(0)
        current_stop = trip.get_node()

        print("Dequeued:", current_stop.get_stop_name().get_stop_name())  # Print the stop name
        if isinstance(current_stop, str):
            # Find the corresponding MetroStop object for the current_stop string
            current_stop = self.tree.search_stop(current_stop)


        return trip
    
    def is_empty(self):
        return not bool(self.trips)

# Path class
class Path:
    def __init__(self):
        self.stops = []
        self.total_fare = 0

    def get_stops(self):
        return self.stops

    def get_total_fare(self):
        return self.total_fare

    def add_stop(self, stop):
        self.stops.append(stop)

    def set_total_fare(self, fare):
        self.total_fare = fare

    def print_path(self):
        for stop in self.stops:
            print(stop.get_stop_name())

# PathFinder class
class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
            for line in self.lines:
                self.tree.populate_tree(line)

    def find_path(self, origin, destination):
        originNode = self.tree.search_stop(origin)
        destNode = self.tree.search_stop(destination)

        print(f"Origin Node: {originNode.get_stop_name().get_stop_name()}")  # Debugging statement
        print(f"Destination Node: {destNode.get_stop_name().get_stop_name()}")  # Debugging statement

        if originNode is None or destNode is None:
            return None

        explorationQueue = deque()

        if originNode.get_stops():  # Check if the stops list is not empty
            forwardTrip = Trip(originNode.get_stops()[0], None)
            explorationQueue.append(forwardTrip)
        else:
            # If originNode has no stops, create a trip with the originNode itself
            forwardTrip = Trip(originNode, None)
            explorationQueue.append(forwardTrip)

        visitedStops = set()

        while explorationQueue:
            currentTrip = explorationQueue.popleft()
            currentStop = currentTrip.get_node()

            print("Exploring:", currentStop.get_stop_name().get_stop_name())  # Debugging

            if currentStop == destNode.get_stops()[0]:
                path = Path()
                while currentTrip is not None:
                    path.add_stop(currentTrip.get_node())
                    currentTrip = currentTrip.get_prev()

                totalFare = 0
                stops = path.get_stops()
                for i in range(len(stops) - 1):
                    current = stops[i]
                    next_stop = stops[i + 1]
                    totalFare += abs(next_stop.get_fare() - current.get_fare())
                path.set_total_fare(totalFare)

                return path

            else:
                if currentStop in visitedStops:
                    continue

                visitedStops.add(currentStop)

                for line in self.lines:
                    nextStop = currentStop.get_next_stop()

                    if nextStop is not None:
                        if self.is_junction(self.tree.search_stop(nextStop.get_stop_name())):
                            nextForwardTrip = Trip(nextStop, currentTrip)
                            nextBackwardTrip = Trip(nextStop, currentTrip)
                            explorationQueue.append(nextForwardTrip)
                            explorationQueue.append(nextBackwardTrip)
                        else:
                            nextTrip = Trip(nextStop, currentTrip)
                            explorationQueue.append(nextTrip)

        return None



    def calculate_total_fare(self, path):
        total_fare = 0
        stops = path.get_stops()

        for i in range(len(stops) - 1):
            current_stop = stops[i]
            next_stop = stops[i + 1]

            # Replace these lines with actual fare calculation logic
            fare_for_segment = self.calculate_fare_between_stops(current_stop, next_stop)
            total_fare += fare_for_segment

        return total_fare

    def calculate_fare_between_stops(self, current_stop, next_stop):
        # Define fare structure for each line (you can customize this)
        fare_structure = {
            "Red Line": 3,
            "Green Line": 2,
            "Violet Line": 4,
            "Magenta Line": 3,
            "Blue Line": 2,
            "Orange Line": 3,
        }

        current_line = current_stop.get_line().get_line_name()
        next_line = next_stop.get_line().get_line_name()

        if current_line == next_line:
            # Intra-line travel, use the fare for the current line
            fare = fare_structure.get(current_line, 0)
        else:
            # Inter-line travel, use a higher inter-line fare
            fare = 5  # Set a default inter-line fare (customize as needed)

        return fare

    def print_path_and_fare(self, path):
        stops = path.get_stops()
        print("Path:")
        for stop in stops:
            print(stop.get_stop_name())
        print("Total Fare:", path.get_total_fare())


    def get_adjacent_stops(self, current_stop):
        adjacent_stops = []

        print("Checking current_stop type:", type(current_stop))  # Debugging statement

        # Ensure current_stop is a MetroStop object
        if isinstance(current_stop, MetroStop):
            print("current_stop is a MetroStop")  # Debugging statement
            # Retrieve the next and previous stops from the current_stop
            next_stop = current_stop.get_next_stop()
            prev_stop = current_stop.get_prev_stop()

            # Check if next_stop and prev_stop are valid MetroStop objects
            if isinstance(next_stop, MetroStop):
                adjacent_stops.append(next_stop)
            if isinstance(prev_stop, MetroStop):
                adjacent_stops.append(prev_stop)

        return adjacent_stops


lines = []

# Example usage:
if __name__ == "__main__":

    red_line = MetroLine("Red Line")
    red_line.populate_line("/Users/sanjay/dsa_cpp_practice/red.txt")
    green_line = MetroLine("Green Line")
    green_line.populate_line("/Users/sanjay/dsa_cpp_practice/green.txt")
    violet_line = MetroLine("Violet Line")
    violet_line.populate_line("/Users/sanjay/dsa_cpp_practice/violet.txt")
    magenta_line = MetroLine("Magenta Line")
    magenta_line.populate_line("/Users/sanjay/dsa_cpp_practice/magenta.txt")
    blue_line = MetroLine("Blue Line")
    blue_line.populate_line("/Users/sanjay/dsa_cpp_practice/blue.txt")
    orange_line = MetroLine("Orange Line")
    orange_line.populate_line("/Users/sanjay/dsa_cpp_practice/orange.txt")
    # Create AVLTree and populate it with all lines
    # Create AVLTree and populate it with all lines
    # metro_tree = AVLTree()

    # ... (previous code remains the same)

    # Create AVLTree and populate it with all lines
    metro_tree = AVLTree()

    # Populate the tree with the MetroLine objects
    for line in [red_line, green_line, violet_line, magenta_line, blue_line, orange_line]:
        metro_tree.populate_tree(line)

    metro_tree.create_avl_tree()

    # Create PathFinder with a list of MetroLine objects
    path_finder = PathFinder(
        metro_tree,
        [red_line, green_line, violet_line, magenta_line, blue_line, orange_line],
    )

    # Define the station names as strings
    origin_station_name = "Station A"  # Replace with the actual station name
    destination_station_name = "Station B"  # Replace with the actual station name

    # Search for the MetroStop objects corresponding to the station names
    origin_station = metro_tree.search_stop(origin_station_name)
    destination_station = metro_tree.search_stop(destination_station_name)

    # Check if both origin and destination stations were found
    if origin_station and destination_station:
        # Perform pathfinding using the found MetroStop objects
        path_finder.find_path(origin_station, destination_station)
    else:
        print(f"Origin station '{origin_station_name}' or destination station '{destination_station_name}' not found.")
