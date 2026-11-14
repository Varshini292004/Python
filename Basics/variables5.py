#[ ] Print the type of each variable using type().
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
salary = int(input("Enter your salary: "))
experience = bool(input("More than 2 years? "))

print("Name: ", type(name))
print("Age: ", type(age))
print("Height: ", type(height))
print("Salary: ", type(salary))
print("More than 2 years experience(yes/no): ",type(experience))
