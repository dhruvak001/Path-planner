from path_planner import *

def get_file_names():
    return ["blue.txt", "green.txt", "magenta.txt", "orange.txt", "red.txt", "violet.txt", "yellow.txt"]

def test_populate_line():
    print("Testing populateLine()")
    filenames = get_file_names()
    expected_total_stops = [44, 21, 25, 6, 29, 38, 62]
    for i in range(len(filenames)):
        line_name = filenames[i][0:len(filenames[i]) - 4]
        metro_line = MetroLine(line_name)
        metro_line.populate_line(filenames[i])
        lines.append(metro_line)        
        assert metro_line.get_total_stops() == expected_total_stops[i]

def test_populate_tree():
    print("Testing populateTree()")
    metro_tree = AVLTree()
    metro_tree.print_tree()
    filenames = get_file_names()
    tree = AVLTree()
    tree.set_root(None)
    for line in lines:
        if tree.root is None:
            tree.set_root(AVLNode(line.stops[0]))
        tree.populate_tree(line)

    assert tree.height(tree.root) == 9
    assert tree.get_total_nodes(tree.root) == 211
 


def get_expected_path():
    return ["Pul Bangash", "Pratap Nagar", "Shastri Nagar", "Inder Lok", "Kanhaiya Nagar", "Keshav Puram", "Netaji Subhash Place", "Kohat Enclave", "Pitampura"]


def test_find_path():
    print("testing find path")
    path_finder = PathFinder(AVLTree(), lines)
    path_finder.create_avl_tree()
    path = path_finder.find_path("Pitampura", "Pul Bangash")
    assert path is not None
    print("Total fare:", path.get_total_fare())
    path.print_path()
    expected_path = get_expected_path()
    for i in range(len(expected_path)):
        assert path.stops[i].get_stop_name() == expected_path[i]
    print("test doneee")


if __name__ == "__main__":
    tests = [test_populate_line, test_populate_tree, test_find_path]

    for test in tests:
        test()
