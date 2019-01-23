def main():
    prob1()
    prob2()
    chall1()






#Create a function that has a loop that quits with q.
# If the user doesn't enter q, ask them to input another string.

#BONUS: Make sure the code can handle whatever case the
# User enters the q as (uppercase or lowercase).

def prob1():


    writeSent = input("Enter a sentence")
    while True:
        writeSent = input("Enter another sentence")
        if writeSent == "q":
            break



# Write 2 functions:
# exercise2() and exercise2_helper(num1, num2, num3. operation)
# The function exercise2_helper(num1, num2, num3)
# should expect 3 numbers, and an operation to perform as a String as parameters.

#
def prob2():




    def prob2operate(num1, num2, num3, operate):

        if(operate == "sum"):
            result = ("The sum of ", num1, num2, num3, "is",   (num1 + num2 + num3))
            return result
        elif(operate == "prod" ):
            result = ("The prod of ", num1, num2, num3, "is",  (num1*num2*num3))
            return result
        elif (operate == "avg"):
            result = ("The avg of ", num1, num2, num3, "is",  (num1 + num2 + num3 / 3))
            return result
        else:
            print("INVALID OPERATION")




    print(prob2operate(5, 6, 7, "sum"))
    print(prob2operate(5, 6, 7, "prod"))
    print(prob2operate(5, 6, 7, "avg"))
    print(prob2operate(5, 6, 7, "none"))





#Write a function that prompts the User for the number of stars to print.
# Then use a loop to print a number of stars/asterisks starting with
# 1 and up to the number entered by the User.



def chall1():

    enterstar = input("Enter more than one star")






































if __name__ == '__main__':
    main()