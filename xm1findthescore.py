

def get_attr_number(node):
    return sum(len(elem.attrib) for elem in node.iter())
