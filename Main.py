# Think of at least three different animals that have a
# common characteristic. Store the names of these
# animals in a list, and then use a for loop to print
# out the name of each animal.

# Modify your program to print a statement about each
# animal, such as "A dog would be a great pet."

# Add a line at the end of your program stating what
# these animals have in common. You could print a
# sentence such as "Any of these animals would make
# a great pet!"

mythical_creatures = ["chimera", "dragon", "griffin"]

for mythical_creature in mythical_creatures:
    print(f"A {mythical_creature.title()} would make a "
          f"great pet!")
print(f"The {mythical_creatures[0].title()}, "
      f"{mythical_creatures[1].title()},"
      f"\nand {mythical_creatures[2].title()} are all "
      f"mythical creatures, creatures of fantasy and "
      f"\nimagination, and any of these animals would "
      f"make a great pet!")
