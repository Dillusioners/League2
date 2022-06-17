print(
        "*********************************************************************************************************************")
print(
        "*                                       WELCOME TO THE UNIT CHECKER                                                *")
print(
        "*********************************************************************************************************************")
#taking the unit input from the user
unit = input("Enter the unit in either abbreviated or complete form...Eg. --> Km or KiloMetre ===> ")
#looping input until given input is valid
while unit == "":
    unit = input("Enter the unit correctly again ===> ")
#changing the unit string to lower case
unit = unit.lower()
fundamental_unit_array = ["kilogram","kg","meter","m","second",	"s","Kelvin","K","mole","mol","ampere","a","candela","cd"]
#running loop until it reaches the n index of the array where n is the final element
for i in range(len(fundamental_unit_array)):
    if unit in fundamental_unit_array:
        #here if the unit belongs to the array it is a fundamental quantity
        print("Unit is a Fundamental")
        break
        #anything else is a fundamental quantity
    else:
        print("It is a derived quantity...")
        print("F.A.Q since derived quantities root from physical quantities literally any representation of a unit is a derived unit"+"\n"+"if it does not belong to the fundamental quantity list."+"\n"+"\n"+"For example abcd is not a physical quantity hence inputting abdc will print that its a derived quantity")
        break
