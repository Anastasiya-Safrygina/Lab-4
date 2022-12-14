from suffix_trees import STree
import re

def load_file(file_name):
    f = open(file_name)
    # lines = re.findall(r"'''\s*(\w+)\s*'''", f.read())
    lines = f.readlines()
    f.close()
    return lines

lines = load_file('test2.txt')
lcs_str = STree.STree(lines)
print(lcs_str.lcs())