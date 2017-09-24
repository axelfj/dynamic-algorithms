# In this algorithm we have 3 towers.
# We're going to represent each tower as a list.
# A, B and C will be their names.
A = []
B = []
C = []

# In the first tower we have to set the elements we want from the major to the minor.

for i in range(1,4):
    A.append(i)

A = A[::-1]
print("We know have the first tower:", A)
print("")

# We need to send every element from A to C, using the mid tower B.
# With the condition of not having a major element over a minor.