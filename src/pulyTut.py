#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 21/Sep/2014
# File: pulpTut.py
# Des: an example of the pulp module
#
# Produced By CSRGXTU
from pulp import *

prob = LpProblem("test1", LpMinimize)

# Variables
x = LpVariable("x", 0, 4)
y = LpVariable("y", -1, 1)
z = LpVariable("z", 0)

# Objective
prob += x + 4*y + 9*z

# Constraints
prob += x+y <= 5
prob += x+z >= 10
prob += -y+z == 7

GLPK().solve(prob)

# Solution
print "Here comes the solution ..."
for v in prob.variables():
  print v.name, "=", v.varValue

print "objective=", value(prob.objective)
