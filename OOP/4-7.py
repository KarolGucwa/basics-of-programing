from statistics_class import Statistics

def main():
    stats = Statistics()

    numbers = [12, 37, 6, 9, 17]
    
    for num in numbers:
        stats.add_number(num)

    stats.display_numbers()
    stats.print_statistics()

if __name__ == "__main__":
    main()
