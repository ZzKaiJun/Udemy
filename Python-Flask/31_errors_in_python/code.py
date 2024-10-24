
def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor can`t be 0. ")
        raise ZeroDivisionError("Divisor can`t be 0. ")
        


    return dividend / divisor



grades = []

print("welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
except ValueError:
    print()
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")