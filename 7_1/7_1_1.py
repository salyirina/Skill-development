from pprint import pprint

name = 'product.txt'
file = open(name, "r")
pprint(file.read())
upd
file.close()
