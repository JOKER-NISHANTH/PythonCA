    # Dict --> Key Values Pairs
DI = {}
print(DI, " ", type(DI))

DI = {"Kishan": "Burger", "Vasee": "Chicken", "Surya": "Watermelon", "Nisha": "Pure Veg", "Cyber": {"Mor": "Water", 'AFT': 'Juice', 'Night': "Milk"}}

print(DI)
print("-------------------------------------------------------------------------")

print(DI["Nisha"])
print("-------------------------------------------------------------------------")

print(DI["Cyber"]["AFT"])
print("-------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Print Keys
print("Keys-->",DI.keys(),end="\n\t\n")
print("Values-->",DI.values(),end="\n\t\n")
print("Items-->", DI.items(), end="\n\t\n")
print("---------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------
# Adding
D2 = dict()
D2["Vijay"] = "Chappathi"
D2["Naveen"] = "Dosa"
D2["AAdhi"]="Idly"
print(D2)
print("-------------------------------------------------------------------------")
# Update
d4 = dict()
d4.update({"Rani":"Tofee"})
d4.update({"Ram": "coffee"})
print(d4)
print("-------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------
# Delecting
del D2["AAdhi"]
D3 = D2
print(D2)

#------------------------------------------------------------------------------------------------------------
D3["Sandy"]="RX-100"
print(D3)

# Get
# Objet_name.Get(key)  or  Object_name["Key"]
print(D2.get("Nandy"))
D2.get("Nandy")
print(D2)
print("-------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Copy  ===> d3 is one copy of D2
d3 = D2.copy()
del d3["Naveen"]
D2["Nandy"]="Pulsar"
print(D2)
print(d3)
print("-------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------
