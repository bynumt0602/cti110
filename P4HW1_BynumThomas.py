#Thomas Bynum

#07/11/2025

#P4HW1

#Assignment assess student ability to edit and enhance exiting programs


# 1. Ask user how many scores they want to enter.
# 2. Create an empty list to hold the scores.
# 3. Use a loop to collect each score:
#    a. Ask for the score.
#    b. If it's not between 0 and 100, show an error and ask again.
#    c. If it's valid, add it to the list.
# 4. After collecting all scores:
#    a. Find the lowest score.
#    b. Remove the lowest score from the list.
#    c. Calculate the average of the new list.
#    d. Use if-elif-else to decide the letter grade.
# 5. Display results: lowest score, modified list, average, and grade.



num_scores = int(input("How many scores do you want to enter? "))
print()

score_list = []  
score_num = 1   

while len(score_list) < num_scores:
    score = float(input(f"Enter score #{score_num}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))  

    score_list.append(score)
    score_num += 1

lowest = min(score_list)
score_list.remove(lowest)

average = sum(score_list) / len(score_list)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print()
print()

print("-------------Results-------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("---------------------------------")
