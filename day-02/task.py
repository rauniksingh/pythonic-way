# # Subscripting
# print("hello"[1])

# # String
# print("123" + "456")

# # Integer = Whole number
# print(123 + 456)

# # Large Integers
# print(123_456_890_123)

# # Float = Floating Point Number
# print(2.90)

# # Boolean
# print(True)
# print(False)

# print(int("123") + int(456))

# int()
# float()
# str()
# bool()

# # Number manipulation 
# print("Number of letter in your name: ", len(input("Enter your name")))

# name_of_the_user = input("Enter your name\n");
# print(type(name_of_the_user))

# length_of_name = len(name_of_the_user);
# print(type(length_of_name))

# print("Number of letter in your name: " + str(length_of_name))

# print("My age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(5 / 3)
# print(5 // 3)
# print(2**3)

# print(3 * (3 + 3) / 3 - 3)

# bmi = 84 / 1.65 ** 2;
# print(bmi)

# print(int(bmi))

# print(round(bmi))

# print(round(bmi, 2))

# score = 0

# # User scores a point

# score += 1
# print(score)

# # f-Strings
# score = 0
# height = 1.8
# is_winning = True

# print(f"Your score is {score}, Your Height is {height} and you are winning {is_winning}")

print("welcome to the tip calculator")

bill = float(input("What was the total bill? $ "));
tip = int(input("How much tip you want to give ? 10, 12 0r 15 ? "))
people = int(input("How many people split the bill ? "))


bill_with_tip = tip / 100 * bill + bill;
total_bill = bill_with_tip / people

print(f"Each person should pay: ${round(total_bill, 2)}")