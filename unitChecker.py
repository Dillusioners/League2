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
    print("There is a theoretically infinite number. The entire set is enumerated with ∏a**(a**(na)) where a∈{s,m,kg,A,K,mol} and na∈Z."+"\n"+"As for how many are in common usage, I would say at least a few of them. Lets just see how many I can name…"+"\n"+"1.area ===> m^2"+"\n"+"2.volume ===> m^3"+"\n"+"3.charge ===> Cforce"+"\n"+"4.Nlinear density ===> kg/m"+"\n"+"5.surface density ===> kg/m^2"+"\n"+"6.volume density ===> kg/m^3"+"\n"+"7.linear charge density ===> C/m")



