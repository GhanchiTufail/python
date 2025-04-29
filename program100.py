# program 100:

# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

# Hint:
# Use for loop to iterate all possible solutions.

def main(head,leg):
    chickens = 0
    rabbits = 0
    total_head = head
    while leg % head != 0:
        leg -= 4
        head -= 1
    chickens = head
    rabbits = total_head-chickens
    return {
        "chickens":chickens,
        "rabits":rabbits
    }
    

print(main(int(35),int(94)))