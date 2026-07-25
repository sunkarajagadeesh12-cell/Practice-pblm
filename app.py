

def calculate_average(marks):
    if not marks:
        return 0;
    return sum(marks) / len(marks)

avg = calculate_average([85,90,78,92])
print("The avg marks are:",avg)
