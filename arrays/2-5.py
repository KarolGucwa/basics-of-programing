# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for row in seats:
       total += len(row)
   return total

def seats_available(seats):
   available = 0
   for row in seats:
       available += row.count('A')
   return available

def seats_booked(seats):
   booked = 0
   for row in seats:
       booked += row.count('B')
   return booked

def seat_status(seats, row, place):
   if seats[row][place] == 'A':
       return 'Available'
   else:
       return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 0, 0))  # First row, first seat (index 0)
print('Seat in row 5, place 5:', seat_status(cinema_seats, 4, 4))  # Last row, last seat (index 4)
print('Seat in row 3, place 5:', seat_status(cinema_seats, 2, 4))  # Row 3, last seat (index 4)
