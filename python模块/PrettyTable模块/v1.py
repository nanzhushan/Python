#coding:utf8
from prettytable import PrettyTable
table = PrettyTable(["animal", "ferocity","age"])
table.add_row(["wolverine", 100,2])
table.add_row(["grizzly", 87,3])
table.add_row(["Rabbit of Caerbannog", 110,4])
table.add_row(["cat", -1,5])
table.add_row(["platypus", 23,6])
table.add_row(["dolphin", 63,7])
table.add_row(["albatross", 44,9])
# table.sort_key("ferocity")
# table.reversesort = True
print table
