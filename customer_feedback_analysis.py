def calculate_positive_feedback(ratings):
    # Handle empty ratings
    if not ratings:
        return 0
    
    # Count positive ratings (4 or 5)
    positive_count = 0
    for rating in ratings:
        if rating >= 4:
            positive_count += 1
    
    # Calculate percentage
    percentage = (positive_count / len(ratings)) * 100
    
    return percentage


# Input example
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

# Calculate result
result = calculate_positive_feedback(ratings)

# Output
print(f"Positive Feedback: {result}%")
