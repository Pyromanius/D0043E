"""
LTU AIRPORT FLIGHT MANAGER
A program used to keep and review the status of the flights for LTU Airport.
"""

# flight_list = {
#     "SK137": {"destination": "Stockholm", "status": "Scheduled"},
#     "LH120": {"destination": "Munich", "status": "Boarding"},
#     "LH005": {"destination": "Manchester", "status": "Boarding"}
# }

flight_list = {}

def main_menu():
    """
    Docstring for main_menu
    Runs the main menu and let's the user choose what operation to perform.
    """
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
        elif choice == '2':
            update_status()
        elif choice == '3':
            remove_flight()
        elif choice == '4':
            view_flights()
        elif choice == '5':
            find_by_status()
        elif choice == '6':
            count_flights()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-6 or q.")


def is_valid_flight_no(flight_no):
    """
    Docstring for is_valid_flight_no
    Check whether the input flight number is valid and does not exist already.
    """
    if len(flight_no) < 3:
        print("Error: Flight number must be at least 3 characters long.")
        return False
    elif is_active_flight_number(flight_no):
        print("Error: Flight number already exists.")
        return False
    else:
        return True


def is_valid_destination(destination):
    """
    Docstring for is_valid_destination
    Check that destination is not empty.
    """
    if not destination:
        print("Error: Destination cannot be empty.")
        return False
    else:
        return True


def is_valid_status(status):
    """
    Docstring for is_valid_status
    Check if status is one of the valid options.
    """
    if status in ["Boarding", "Departed", "Scheduled"]:
        return True
    else:
        print("Error: Invalid status! Choose Scheduled, Boarding, or Departed.")
        return False


def add_flight():
    """
    Docstring for add_flight
    Add a new flight to the system and perform the necessary checks to see if input is valid.
    """
    while True:
        # Go through inputs one-by-one and validate each input before moving on.
        flight_no = input("Enter flight number: ").strip()
        if not is_valid_flight_no(flight_no):
            continue
        else:
            break
    while True:
        destination = input("Enter destination: ")
        if not is_valid_destination(destination):
            continue
        else:
            break
    while True:
        status = input("Enter status (Scheduled/Boarding/Departed): ")
        if not is_valid_status(status):
            continue
        else:
            break

    print(f"Flight {flight_no} to {destination} added successfully!")
    flight_list[flight_no] = {"destination": destination, "status": status}

def view_flights():
    """
    Docstring for view_flights
    Sorts and prints out a list of all currnet flights in the system.
    TODO: Should have a helper function that takes flight_list as a parameter and sorts it, returning the sorted list. !!
    """
    bubble_sort(flight_list) # Was not inplemented correctly due to the AutoTest causing confusion, when asking for the wrong function.
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
    """
    Docstring for is_active_flight_number
    Check if entered flight number already exists in the system.
    """
    if flight_no in flight_list:
        return True
    else:
        return False


def update_status():
    """
    Docstring for update_status
    Update the status of an exisiting flight.
    # TODO: Repeat while-loop after flight_no was input correctly. Should repeat and ONLY ASK FOR status again if input is incorrect.
    """
    while True:
        flight_no = input("Enter flight number: ").strip()
        if not is_active_flight_number(flight_no):
            print("Error: Flight not found.")
            continue
        print(f"Current status: {flight_list[flight_no]["status"]}")
    
    # Should repeat while loop here
        status = input("Enter new status (Scheduled/Boarding/Departed) or press Enter to keep the current status: ")
        if not status:
            # If status is left empty then keep current status.
            print(f"Flight {flight_no} status updated successfully!")
            break
        if not is_valid_status(status):
            continue
        else:
            flight_list[flight_no]["status"] = status
            print(f"Flight {flight_no} status updated successfully!")
            break


def remove_flight():
    """
    Docstring for remove_flight
    Remove a flight from the system by enetering a flight number.
    """
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
    """
    Docstring for count_flights
    Count the total amount of flights in the system.
    """
    print(f"Total flights registered: {len(flight_list)}")


def bubble_sort(flight_list):
    """
    Docstring for bubble_sort
    Sort the list of flights alphabetically. Takes a flight_list parameter for reuseable purposes.
    """
    flight_numbers = list(flight_list.keys())
    for i in range(len(flight_numbers)):
        for j in range(0, len(flight_numbers) - i - 1):
            if flight_numbers[j] > flight_numbers[j + 1]:
                flight_numbers[j], flight_numbers[j + 1] = flight_numbers[j + 1], flight_numbers[j]
    sorted_list = {k: flight_list[k] for k in flight_numbers}
    return sorted_list


def find_by_status():
    """
    Docstring for find_by_status
    Search for all flights that has a ceratin status.
    """
    while True:
        status = input("Enter status to search for (Scheduled/Boarding/Departed): ")
        if not is_valid_status(status):
            continue
        else:
            # Create a new list with all the flights matching the input status. 
            # This keeps the list of all flights intact.
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
    """
    Docstring for list_status_matches
    Puts all status matches in a new list and returns that list.
    """
    flight_numbers = list(flight_list.keys())
    status_list = {}
    for i in range(len(flight_numbers)):
        if flight_list[flight_numbers[i]]["status"] == status:
            status_list[flight_numbers[i]] = {"destination": flight_list[flight_numbers[i]]["destination"],
                                              "status": flight_list[flight_numbers[i]]["status"]}
    status_list = bubble_sort(status_list)
    return status_list


def main():
    """
    Docstring for main
    Main function. Used to start up the main menu.
    """
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        exit()
