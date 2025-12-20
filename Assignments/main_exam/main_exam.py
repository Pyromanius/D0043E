"""A program for managing current cars in the system for a rental company."""
# LTU Rent-a-Car


# Only used for testing
#
# cars = {
#     "CYW426": {
#         "model": "BMW 330i xDrive",
#         "status": "Available"   # or "Rented"
#     },
#     "DWW341": {
#         "model": "Skoda Enyaq iv 80x",
#         "status": "Rented"
#     }
# }

cars = {}
rentals = []


def bubble_sort(items):
    """Return a new list which is a sorted copy of items using bubble sort."""
    lst = items.copy()
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def add_car():
    """Adds a new car to the sytem"""
    reg = input("Enter registration number: ").strip()
    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.")
        return
    if " " in reg:
        print("Error: Registration number cannot contain spaces.")
        return
    if reg in cars:
        print("Error: Registration number already exists.")
        return
    model = input("Enter make and model: ").strip()
    if model == "":
        print("Error: Make and model cannot be empty.")
        return
    cars[reg] = {"model": model, "status": "Available"}
    print(f"{model} with registration number {reg} was added to car fleet.")


def rent_car():
    """Rent out a car to a costumer"""
    reg = input("Enter car's registration number: ").strip()
    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.")
        return
    if " " in reg:
        print("Error: Registration number cannot contain spaces.")
        return
    if reg not in cars:
        print("Error: Car not found.")
        return
    if cars[reg]["status"] != "Available":
        print("Error: Car is not available.")
        return
    hour_str = input("Enter pickup hour (0-23): ").strip()
    try:
        hour = int(hour_str)
    except ValueError:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.")
        return
    if hour < 0 or hour > 23:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.")
        return
    renter = input("Enter renter's name: ").strip()
    if renter == "":
        print("Error: Renter name cannot be empty.")
        return
    cars[reg]["status"] = "Rented"
    rentals.append({
        "reg": reg,
        "renter": renter,
        "start_hour": hour,
        "end_hour": None,
        "hours": None,
        "cost": None
    })
    print(f"Car with registration number {reg} was rented by {renter} at {hour}.")


def return_car():
    """Return a car a costumer has had"""
    reg = input("Enter registration number: ").strip()
    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.")
        return
    if " " in reg:
        print("Error: Registration number cannot contain spaces.")
        return
    if reg not in cars:
        print("Error: Car not found.")
        return
    if cars[reg]["status"] != "Rented":
        print("Error: Car is not rented.")
        return
    hour_str = input("Enter return hour (0-23): ").strip()
    try:
        hour = int(hour_str)
    except ValueError:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.")
        return
    if hour < 0 or hour > 23:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.")
        return
    active_rental = None
    for r in rentals:
        if r["reg"] == reg and r["end_hour"] is None:
            active_rental = r
            break
    if active_rental is None:
        print("Error: Active rental not found for this car.")
        return
    start = active_rental["start_hour"]
    if hour <= start:
        print("Error: Return hour must be later than pickup hour.")
        return
    active_rental["end_hour"] = hour
    active_rental["hours"] = hour - start
    active_rental["cost"] = active_rental["hours"] * 120
    cars[reg]["status"] = "Available"
    print("===================================")
    print("LTU Rent-a-Car")
    print("===================================")
    print(f"Name: {active_rental['renter']}")
    print(f"Car: {cars[reg]['model']} ({reg})")
    print(f"Time: {start}-{hour} ({active_rental['hours']} hours)")
    print(f"Total cost: {int(active_rental['cost'])} SEK")


def view_fleet():
    """List all cars currently in the systme"""
    if not cars:
        print("No cars in fleet.")
        return
    print("LTU Rent-a-Car car fleet:")
    print("Fleet:")
    print(f"{'Model':18} {'Registration':12} {'Status'}")
    regs = list(cars.keys())
    regs = bubble_sort(regs)
    total_available = 0
    for reg in regs:
        model = cars[reg]['model']
        status = cars[reg]['status']
        if status == 'Available':
            total_available += 1
        print(f"{model:18} {reg:12} {status}")
    print(f"Total number of cars: {len(regs)}")
    print(f"Total number of available cars: {total_available}")


def view_rentals():
    """View all upcoming rentals"""
    if not rentals:
        print("No rentals for today.")
        return
    print("LTU Rent-a-Car rental summary:")
    print("Rentals:")
    print(f"{'Name':18} {'Registration':12} {'Pickup':6} {'Return':6} {'Cost'}")
    names = [r['renter'] for r in rentals]
    sorted_names = bubble_sort(names)
    printed = set()
    total_revenue = 0
    for name in sorted_names:
        for idx, r in enumerate(rentals):
            if idx in printed:
                continue
            if r['renter'] == name:
                printed.add(idx)
                reg = r['reg']
                pickup = r['start_hour']
                ret = '' if r['end_hour'] is None else str(r['end_hour'])
                cost = '' if r['cost'] is None else f"{int(r['cost'])} SEK"
                if r['cost'] is not None:
                    total_revenue += r['cost']
                print(f"{name:18} {reg:12} {str(pickup):6} {ret:6} {cost}")
    print(f"Total number of rentals: {len(rentals)}")
    print(f"Total revenue: {int(total_revenue)} SEK")


def print_menu():
    """Print out the main menu"""
    print("# LTU Rent-a-Car")
    print("1. Add car to fleet")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. View car fleet")
    print("5. View rental summary")
    print("q. Exit program")


def main_menu():
    """Prints the main menu and lets the user chooose operation"""
    while True:
        print_menu()
        choice = input("Enter your option: ").strip()
        if choice == '1':
            add_car()
        elif choice == '2':
            rent_car()
        elif choice == '3':
            return_car()
        elif choice == '4':
            view_fleet()
        elif choice == '5':
            view_rentals()
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-5 or q.")


def main():
    """Main function. Used to start the main menu()"""
    main_menu()


if __name__ == '__main__':
    """Guarder for main function"""
    main()
