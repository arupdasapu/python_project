# Define conditions for the house

good_condition = True
reasonable_price = False
poor_foundation = False

# Check if the house is in good condition and reasonably priced
if good_condition and reasonable_price:
    print("We will buy the house")

# Check if the house is in good condition or reasonably priced
if good_condition or reasonable_price:
    print("We are interested")

# Check if the house is in good condition and has no poor foundation
if good_condition and not poor_foundation:
    print("It is a good deal")
