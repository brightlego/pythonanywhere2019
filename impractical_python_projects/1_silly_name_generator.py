import random
firstnames = """John Josh Jamees Jane Joseph Josephine""".split()
surnames = "Ellis Black Winsor".split()
choice = raw_input("Do you want a new name? (y|n) ").lower() == 'y'
while choice:
    print
    print random.choice(firstnames),random.choice(surnames)
    choice = raw_input("Do you want a new name? (y|n) ").lower() == 'y'
print("Bye!")