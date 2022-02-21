# my solution to weekly task 02
# author: Maria Puchkina
# program calculates somebody's Body Mass Index (BMI)
# BMI is the body mass divided by the square of the body height
height = float(input("Input your height in Meters: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your BMI is: ", round(weight / (height * height), 2))
