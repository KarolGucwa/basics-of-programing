def month(n):
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= n <= 12:
        return months[n - 1]  # Month numbers are 1-indexed, list is 0-indexed
    else:
        return "Invalid month number"
