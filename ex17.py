# -*- coding:utf-8 -*-
from sys import argv
#from os.path import exists

script, from_file, to_file = argv

print("Coping from {0} to {1}.".format(from_file, to_file))

out_file = open(to_file, 'w')
out_file.write(open(from_file).read())
print("All right, all done.")
#to_file.close()
out_file.close()
