from datetime import datetime, timedelta

class Boat:
    def __init__(self, boat_id):
        self.boat_id = boat_id
        self.hours_hired = 0
        self.return_time = None

def calculate_money_taken(boat):
    try:
        current_time = datetime.now().replace(second=0, microsecond=0)
        if 10 <= current_time.hour < 17:
            print(f"\nBoat {boat.boat_id}:")
            hours = float(input("Enter the number of hours to hire: "))
            if 0.5 <= hours <= 8:
                cost = 20 * hours if hours > 1 else 12
                boat.hours_hired += hours
                boat.return_time = current_time + timedelta(hours=hours)
                print(f"Boat hired for {hours} hours. Cost: ${cost}")
                return cost
            else:
                print("Invalid hours. Must be between 0.5 and 8.")
        else:
            print("Boats can only be hired between 10:00 and 17:00.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def find_next_available(boats):
    current_time = datetime.now().replace(second=0, microsecond=0)
    available_boats = [boat for boat in boats if boat.return_time is None or boat.return_time <= current_time]
    if available_boats:
        print(f"\nAvailable Boats: {[boat.boat_id for boat in available_boats]}")
    else:
        next_available_time = min(boat.return_time for boat in boats)
        print(f"No boats available. Next available time: {next_available_time.strftime('%H:%M')}")

def calculate_total_money_taken(boats):
    total_money = sum(boat.hours_hired * 20 if boat.hours_hired > 1 else 12 for boat in boats)
    total_hours = sum(boat.hours_hired for boat in boats)
    unused_boats = [boat.boat_id for boat in boats if boat.hours_hired == 0]
    most_used_boat = max(boats, key=lambda boat: boat.hours_hired).boat_id

    print("\nEnd of Day Report:")
    print(f"Total Money Taken: ${total_money}")
    print(f"Total Hours Boats Hired: {total_hours}")
    print(f"Unused Boats: {unused_boats}")
    print(f"Most Used Boat: {most_used_boat}")

def main():
    boats = [Boat(boat_id) for boat_id in range(1, 11)]

    # Task 1: Calculate money taken for one boat1
    for boat in boats:
        calculate_money_taken(boat)

    # Task 2: Find the next boat available
    find_next_available(boats)

    # Task 3: Calculate total money taken for all boats at the end of the day
    calculate_total_money_taken(boats)

if __name__ == "__main__":
    main()
