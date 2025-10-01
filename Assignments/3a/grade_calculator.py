def get_final_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def enter_scores(scores):
    for i in range(1, 6):
        score = float(input(f"Enter the score for Subject {i}: "))
        scores.append(score)


scores = []
enter_scores(scores)
average = sum(scores) / 5

print("Grade Report")
print("----------------------")
for i in range(1, 6):
    print(f"Subject {i}: {scores[i-1]}")

print(f"\nAverage Score: {average:.2f}")
print("Final Grade: ", get_final_grade(average))
