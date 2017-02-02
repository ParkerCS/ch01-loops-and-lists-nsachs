#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.
def grade(percent):
    if percent >= 97 and percent <= 100:
        print("A+")
    elif percent >= 93 and percent <= 96:
        print("A")
    elif percent >= 90 and percent <= 92:
        print("A-")
    elif percent >= 87 and percent <= 89:
        print("B+")
    elif percent >= 83 and percent <= 86:
        print("B")
    elif percent >= 80 and percent <= 82:
        print("B-")
    elif percent >= 77 and percent <= 79:
        print("C+")
    elif percent >= 73 and percent <= 76:
        print("C")
    elif percent >= 70 and percent <= 72:
        print("C-")
    elif percent >= 67 and percent <= 69:
        print("D+")
    elif percent >= 65 and percent <= 66:
        print("D")
    if percent <= 65 and percent >= 0:
        print("F")
    else:
        print("Error")

grade(int(input("Enter your grade: ")))


# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string
'''
def vowels(words):
    vowels = 0


print(input("Enter a a phrase: "))
'''

# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
def quadratic_equation(a,b,c):
    solutions = 0
    if a == 0:
        print("Undefined")
    elif b == 0:
        print("The answer is 0.")
    else:
        x = (-b -(((b ** 2) - (4 * a * c)))** 0.5)/(2 * a)
        y = (-b - ((b ** 2) - (4 * a * c)) ** 0.5)/ (2 * a)


    print(x)

def quadtratic_equation(3,4,