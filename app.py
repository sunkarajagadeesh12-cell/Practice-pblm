

def calculate_average(marks):
    if not marks:
        return 0;
    return sum(marks) / len(marks)

avg = calculate_average([85,90,78,92])
print("The avg marks are:",avg)

if(avg>90):
    print("You achieved A Grade with avg of :", avg)
if(avg>80 and avg<90 ):
    print("You achieved B Grade with avg of :", avg)
if(avg>70 and avg<80):
    print("You achieved C Grade with avg of :", avg)

