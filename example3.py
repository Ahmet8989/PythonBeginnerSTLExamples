salaryEmployeeA = 5000
salaryEmployeeB = 4000
tax = 0.37
print(salaryEmployeeA - (salaryEmployeeA * tax))
print(salaryEmployeeB - (salaryEmployeeB * tax))

salaryEmployeeB += 3000
print(salaryEmployeeB)

numA = 3            #int
numB = 2.3          #float
name = "Ahmet"      #string
isStudent = True    #bool

# numA, numB, name, isStudent = (3, 2.3, "Ahmet", True) --> We also could define this with this way in one line

firstName = "Ahmet "
sirName = "Be"
print(firstName + sirName)

# Variable Definition Rules 
# Variable name can not start with a number
# Variable dependent about how it is written (with upper-case or lower-case)
# Variables can not contain spaces 


# Solution of example one 

custumerName, customerSirname, customerFullName, customerGender, customerID, customerBirthYear, customerAdress, customerAge  = ("Aslan", "Yilmaz", "AslanYilmaz", 'Male', 'xyz456', 1998, "Bursa", 23)

# Solution of example two 

orderOnePrice = 110
orderTwoPrice = 1100.5
orderThreePrice = 356.95
total = orderOnePrice + orderTwoPrice + orderThreePrice
print(total)
