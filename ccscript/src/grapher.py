import re
import hashlib
import unittest

#Match a heading
#A heading can be found in the report if it satisfies the following:
# - It is at the beginning of a line
# - The only letters it contains are uppercase
# - It is followed by a colon
def is_heading(line):
    '''
    Check if a line is a heading.
    :type line: str
    :rtype: bool
    '''
    pat = re.compile(r"^.*:")
    if not pat.match(line):
        return False
    if line.split(':')[0].upper() == line.split(':')[0]:
        return True
    return False

#Match a subheading
#A subheading can be found in the report if it satisfies the following:
# - It is at the beginning of a line
# - It must contain lowercase letters
# - It is followed by a colon
def is_subheading(line):
    '''
    Check if a line is a subheading.
    :type line: str
    :rtype: bool
    '''
    pat = re.compile(r"^.*:")
    if not pat.match(line):
        return False
    if not is_heading(line):
        return True
    return False

#Define the document graph
class Node:
    '''
    A node in the document graph.
    '''
    def __init__(self, _id, name, parent=None):
        '''
        :type _id: str
        :type name: str
        :type parent: Node
        '''
        self._id = _id
        self.name = name
        self.parent = parent
        self.children = []
        self.text = ""

    def __repr__(self):
        return self.name

#Build the document graph
def build_graph(report_text):
    '''
    Build the document graph.
    :type report_text: str
    :rtype: dict
    '''
    #Split the report into lines
    lines = report_text.splitlines()

    nodes = {}

    #Create the root node
    root = Node(hashlib.sha256("root".encode()).hexdigest(), "root")

    #Create the current node7
    current_node = root
    heading_node = root

    for count, line in enumerate(lines):
        
        unique_line = line + str(count)

        #Check if the line is a heading
        if is_heading(line):
            #Split the line at the semicolon
            heading = line.split(":")[0]
            line = line.split(":")[1]

            #Create a new node
            _id = hashlib.sha256(unique_line.encode()).hexdigest()
            new_node = Node(_id, line, current_node)
            new_node.name = heading
            root.children.append(new_node)
            heading_node = new_node
            current_node = new_node
            nodes[_id] = new_node

        #Check if the line is a subheading
        elif is_subheading(line):
            #Split the line at the semicolon
            subheading = line.split(":")[0]
            line = line.split(":")[1]

            #Create a new node
            _id = hashlib.sha256(unique_line.encode()).hexdigest()
            new_node = Node(_id, line, current_node)
            new_node.name = subheading
            heading_node.children.append(new_node)
            current_node = new_node
            nodes[_id] = new_node

        #Add the line to the current node otherwise
        else:
            current_node.text += line
        
    return root, nodes

##############################################################################
#                                UNIT TESTS                                  #

class TestIsHeading(unittest.TestCase):
    def test_is_heading(self):
        self.assertTrue(is_heading("HEADING:"))
        self.assertTrue(is_heading("HEADING 1: "))
        self.assertFalse(is_heading("Heading 2:"))
        self.assertFalse(is_heading("heading3:"))
        self.assertFalse(is_heading("HEADING4"))

class TestIsSubheading(unittest.TestCase):
    def test_is_subheading(self):
        self.assertTrue(is_subheading("SUB heading:"))
        self.assertTrue(is_subheading("Subheading 1: "))
        self.assertTrue(is_subheading("Subheading3:"))
        self.assertTrue(is_subheading("Subheading4:"))
        self.assertFalse(is_subheading("SUBHEADING 1: "))
        self.assertFalse(is_subheading("SUBHEADING 2:"))

class TestBuildGraph(unittest.TestCase):
    #Get text report from file
    def get_report_text(self, filename):
        with open(filename, "r") as f:
            return f.read()
    
    def test_build_graph(self):
        report_text = self.get_report_text("/Users/yassinkortam/Documents/GitHub/med_research/sample_data/report1.txt")
        nodes = build_graph(report_text)
        num_headings = 0
        for node in nodes.values():
            if node.children:
                num_headings += 1
        self.assertEqual(num_headings, 6)
                



