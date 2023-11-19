class CallRateCalculator:
    def __init__(self):
        self.call_rate = 10 

    def set_call_rate(self, start_time):
        if 9.0 <= start_time < 11.0:
            self.call_rate = 9  

    def calculate_charges(self, start_time, duration_minutes):
        self.set_call_rate(start_time)
        total_charge = self.call_rate * duration_minutes
        return total_charge

def get_start_time_input():
    while True:
        try:
            start_time = float(input("Enter the start time (HH.MM): "))
            if 0.0 <= start_time <= 23.59:
                return start_time
            else:
                print("Invalid input. Please enter a valid start time.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for start time.")

def get_duration_input():
    while True:
        try:
            duration_minutes = int(input("Enter the total duration of the call (in minutes): "))
            if duration_minutes >= 0:
                return duration_minutes
            else:
                print("Invalid input. Duration must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for duration.")

    
if __name__ == "__main__":
    start_time = get_start_time_input()
    duration_minutes = get_duration_input()

    calculator = CallRateCalculator()
    total_charge = calculator.calculate_charges(start_time, duration_minutes)
    print(f"Call charges: Rs. {total_charge:.2f}")
