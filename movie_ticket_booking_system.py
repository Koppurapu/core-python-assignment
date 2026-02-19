def book_seat_func(booked_seats, seat_number, total_seats):
    if seat_number < 1 or seat_number > total_seats:
        print(f"Seat {seat_number} does not exist.")
    elif seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} successfully booked.")


# Function to cancel a seat
def cancel_seat_func(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} successfully cancelled.")
    else:
        print(f"Seat {seat_number} is not currently booked.")


# Function to get available seats
def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


# Input example
total_seats = 10
booked_seats = [2, 5, 7]

# Book seat 3
book_seat_func(booked_seats, 3, total_seats)

# Cancel seat 5
cancel_seat_func(booked_seats, 5)

# Get available seats
available_seats = get_available_seats(total_seats, booked_seats)

# Output
print("Available seats:", available_seats)
