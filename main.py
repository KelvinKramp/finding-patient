import pandas as pd
database = pd.read_csv("https://medicalprogress.dev/dummy_data/dummy_db.csv")
database

# Get input from user
name = input("Provide name: \n")
birthdate = input("Provide birthdate in format dd/mm/yyyy: \n")

# Search birthdate in database
name_database = None
for index, row in database.iterrows():
    if row[1] == birthdate:
        name_database = row[0]
        address = row[2]

# Check if birthdate was found
if name_database is not None:
    print("First name in database that corresponds with input birthdate =", name_database)
else:
    raise Exception("Patient not found based on birthdate", birthdate)


# Do fuzzywuzzy comparison
from fuzzywuzzy import fuzz
Str1 = name
Str2 = name_database
partial_ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
if partial_ratio > 80:
    print("During search based on birthdate a name match was found...")
    print("Partial string ratio =", partial_ratio)
    print("Was", name_database, "with birthdate", birthdate, "living on", address, "the person that you were looking for?")
else:
    print("Person not found with birthdate", birthdate, "and name", name)
