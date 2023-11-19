class CallChargesCalculator:
    def __init__(self):
        self.call_rate = 10  

    def set_call_rate(self, start_time):
        if 9.0 <= start_time < 11.0:
            self.call_rate = 9  

    def calculate_charges(self, start_time, duration_minutes):
        self.set_call_rate(start_time)
        total_charge = self.call_rate * duration_minutes
        return total_charge

if __name__ == "__main__":
    try:
        start_time = float(input("Enter the start time (HH.MM): "))
        duration_minutes = int(input("Enter the total duration of the call (in minutes): "))

        if 0.0 <= start_time <= 23.59 and duration_minutes >= 0:
            calculator = CallChargesCalculator()
            total_charge = calculator.calculate_charges(start_time, duration_minutes)
            print(f"Call charges: Rs. {total_charge:.2f}")
        else:
            print("Invalid input. Please enter a valid start time and duration.")
    except ValueError:
        print("Invalid input. Please enter numeric values for start time and duration.")
