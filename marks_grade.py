#Write a program to accept percentage from the user and display the grade according to the following criteria:

  #       Marks                                    Grade
 #        > 90                                         A
  #       > 80 and <= 90                               B
  #       >= 60 and <= 80                              C
   #      below 60                                     D
marks=0
marks =int(input("Enter your marks "))
if marks > 90:
    print("congrats your for A GRADE")
elif marks>80 and marks<=90:
    print("B GRADE")
elif marks>=60 and marks<=80:
    print("C GRADE")
elif marks<60 and marks>=35:
    print("D GRADE")
else:
    print("Failed")
    
    