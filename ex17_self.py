from sys import argv
from os.path import exists

script, from_file, to_file = argv
# don't need too many media variables
open(to_file,'w').write(open(from_file,'r').read())
