def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


# Function to calculate averages for all students and find top performer
def classroom_performance(students):
    averages = {}
    
    # Calculate average for each student
    for student, marks in students.items():
        avg = calculate_average(marks)
        averages[student] = round(avg, 2)
    
    # Find top performer
    top_performer = max(averages, key=averages.get)
    
    return averages, top_performer


# Input example
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

# Call function
average_marks, top_student = classroom_performance(students)

# Output
print("Average Marks:", average_marks)
print("Top Performer:", top_student)
