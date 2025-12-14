flight_list = {
    "SK137": {"destination": "Stockholm", "status": "Scheduled"},
    "LH120": {"destination": "Munich", "status": "Boarding"},
    "LH005": {"destination": "Manchester", "status": "Boarding"}
}

# Not actually needed.
# def is_valid_choice(choice):
#     if choice in ['1', '2', '3', '4', '5', '6', 'q']:
#         return True
#     else:
#         print("Invalid choice. Choose 1-6 or q.")
#         return False


def main_menu():
    while True:
        print("""# LTU Airport Flight Manager
1. Register a new flight
2. Update flight status
3. Remove a flight
4. View all flights
5. Find flights by status 
6. Count total flights
q. Exit program""")
        choice = input("Enter your option: ")
        if choice == '1':
            add_flight()
            continue
        elif choice == '2':
            update_status()
            continue
        elif choice == '3':
            remove_flight()
            continue
        elif choice == '4':
            view_flights(flight_list)
            continue
        elif choice == '5':
            get_by_status()
            continue
        elif choice == '6':
            count_flights()
            continue
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            continue


def is_valid_flight_no(flight_no):
    if len(flight_no) < 3:
        print("Error: Flight number must be at least 3 characters long.")
        return False
    elif is_active_flight_number(flight_no):
        print("Error: Flight number already exists.")
        return False
    else:
        return True


def is_valid_destination(destination):
    if not destination:
        print("Error. Desination cannot be empty.")
        return False
    else:
        return True
    

def is_valid_status(status):
    if status in ["Boarding", "Departed", "Scheduled"]:
        return True
    else:
        print("Invalid status! Choose Scheduled, Boarding, or Departed.")
        return False


def add_flight():
    flight_no = input("Enter flight number: ").strip()
    if not is_valid_flight_no(flight_no):
        return
    destination = input(f"Enter destination: ")
    if not is_valid_destination(destination):
        return
    status = input(f"Enter status (Scheduled/Boarding/Departed): ")
    if not is_valid_status(status):
        return
    else:
        print(f"Flight number {flight_no} to {destination} added succesfully!")
        flight_list[flight_no] = {"destination": destination, "status": status}


def view_flights(flight_list):
    flight_list = bubble_sort(flight_list)
    if len(flight_list) == 0:
        print("No flights registered.")
    else:
        print("Current Flights:") 
        print("-" * 48)
        print("Flight   Destination        Status")
        print("-" * 48)
        for flight_no, flight_info in flight_list.items():
            print(f"{flight_no:<8} {flight_info['destination']:<18} {flight_info['status']}")
        print("-" * 48)


def is_active_flight_number(flight_no):
    if flight_no in flight_list:
        return True
    else:
        return False


def update_status():
    while True:
        flight_no = input("Enter flight number: ").strip()
        if not is_active_flight_number(flight_no):
            print("Error: Flight not found.")
            continue
        print(f"Current status: {flight_list[flight_no]["status"]}")
        status = input(f"Enter new status (Scheduled/Boarding/Departed) or press Enter to keep the current status: ")
        if not status:
            print(f"{flight_no} status updated succesfully!")
            break
        if not is_valid_status(status):
            print("Invalid status! Choose Scheduled, Boarding, or Departed.")
            continue
        else:
            print(f"{flight_no} status updated succesfully!")
            flight_list[flight_no]["status"] = status
            break


def remove_flight():
    while True:
        flight_no = input("Enter flight number: ").strip()
        if not is_active_flight_number(flight_no):
            print("Error: Flight not found.")
            continue
        else:
            break
    del flight_list[flight_no]
    print(f"Flight {flight_no} removed successfully!")


def count_flights():
    print(f"Total flights registered: {len(flight_list)}")


def bubble_sort(flight_list):
    flight_numbers = list(flight_list.keys())
    for i in range(len(flight_numbers)):
        for j in range(0, len(flight_numbers) - i - 1):
            if flight_numbers[j] > flight_numbers[j + 1]:
                flight_numbers[j], flight_numbers[j + 1] = flight_numbers[j + 1], flight_numbers[j]
    sorted_list = {k : flight_list[k] for k in flight_numbers}
    return sorted_list


def get_by_status():
    while True:
        status = "Boarding" # input("Enter status to search for (Scheduled/Boarding/Departed): ").strip()
        if not is_valid_status(status):
            continue
        else:
            status_list = list_status_matches(status)
            break
    if len(status_list) > 0:
        print(f"Flights with status {status}")
        print("-" * 40)
        print("Flight   Destination")
        print("-" * 40)
        for flight_no, flight_info in status_list.items():
            print(f"{flight_no:<8} {flight_info["destination"]}")
        print("-" * 40)
    else:
        print(f"No flights found with status {status}.")


def list_status_matches(status):
    flight_numbers = list(flight_list.keys())
    status_list = {}
    for i in range(len(flight_numbers)):
        if flight_list[flight_numbers[i]]["status"] == status:
            status_list[flight_numbers[i]] = {"destination": flight_list[flight_numbers[i]]["destination"], 
                                            "status": flight_list[flight_numbers[i]]["status"]}
    status_list = bubble_sort(status_list)
    return status_list


def main():
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")