#Day3 the topic covered are random, import, from, packages, statistics, sys, sys.argv, slices, json, request
import random
import sys

if len(sys.argv) < 2:
    sys.exit("Error please provide the name")

sel = random.choice(sys.argv[1:])
print("Winner, name is ", sel)

#for arg in sys.argv[1:]:
#    print("hello, my name is ", arg)
