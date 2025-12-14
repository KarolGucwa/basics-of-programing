import statistics as stats

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print("Numbers:", *self.numbers)

    def get_max(self):
        return max(self.numbers) if self.numbers else None

    def get_min(self):
        return min(self.numbers) if self.numbers else None

    def get_arithmetic_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else None

    def get_median(self):
        if not self.numbers:
            return None
        return stats.median(self.numbers)

    def print_statistics(self):
        print(f"Max: {self.get_max()}")
        print(f"Min: {self.get_min()}")
        print(f"Arithmetic Mean: {self.get_arithmetic_mean():.2f}")
        print(f"Median: {self.get_median()}")
