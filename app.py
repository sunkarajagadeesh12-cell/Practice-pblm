

def calculate_average(marks):
    if not marks:
        return 0;
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg>=90:
        print("You achieved A Grade with avg of :", avg)
    elif avg>=80:
        print("You achieved B Grade with avg of :", avg)
    else:
        print("You achieved C Grade with avg of :", avg)

avg = calculate_average([85,90,78,92])
print("The avg marks are:",avg)
grade = calculate_grade(avg)

