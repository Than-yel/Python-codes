# travel planner
def travel_planner():
    """
    Interactive travel planning tool that helps users create a basic trip plan.
    
    This function guides users through selecting three key travel components:
    destination, transportation mode, and accommodation type. It presents
    predefined options for each category and validates user input to ensure
    valid selections.
    
    The function operates through a command-line interface with the following
    workflow:
    1. Displays destination options (Lagos, Accra, Milan, Johannesburg)
    2. Prompts user to select a destination using A-D options
    3. Displays transportation options (Flight, Train, Car, Bus)
    4. Prompts user to select transportation using A-D options  
    5. Displays accommodation options (Hotel, Hostel, Airbnb, Camping)
    6. Prompts user to select accommodation using A-D options
    7. Summarizes the complete trip plan
    
    Features:
    - Input validation with error handling for invalid choices
    - Persistent prompting until valid input is received
    - Case-insensitive input handling
    - Clear confirmation messages for each selection
    - Final summary of all choices
    
    Parameters:
        None
    
    Returns:
        None (prints results to console)
    
    Example:
        travel_planner()
        Choose a destination:
        A: Lagos
        B: Accra  
        C: Milan
        D: Johannesburg
        Enter your choice (A, B, C, D): A
        You have chosen Lagos
        ...
        Your trip plan:
        Destination: Lagos
        Transportation: Flight
        Accommodation: Hotel
    """
    # Using a dictionary
    # Destination options
    destinations = {
        "A": "Lagos",
        "B": "Accra",
        "C": "Milan",
        "D": "Johannesburg"
    }

    # Transportation options
    transportation = {
        "A": "Flight",
        "B": "Train",
        "C": "Car",
        "D": "Bus"
    }

    # Accommodation options
    accommodation = {
        "A": "Hotel",
        "B": "Hostel",
        "C": "Airbnb",
        "D": "Camping"
    }

    # Initialize user choices
    user_choices = {}

    # Prompt user to choose destination
    print("Choose a destination:")
    for option, destination in destinations.items():
        print(f"{option}: {destination}")
    chosen_destination = None
    while chosen_destination is None:
        user_input = input("Enter your choice (A, B, C, D): ")
        if user_input.upper() in ['A', 'B', 'C', 'D']:
            chosen_destination = user_input.upper()
            user_choices['destination'] = destinations[chosen_destination]
            print(f"You have chosen {destinations[chosen_destination]}")
        else:
            print("Invalid option. Please try again")

    # Prompt user to choose transportation
    print("Choose a mode of transportation:")
    for option, transport in transportation.items():
        print(f"{option}: {transport}")
    chosen_transportation = None
    while chosen_transportation is None:
        user_input = input("Enter your choice (A, B, C, D): ")
        if user_input.upper() in ['A', 'B', 'C', 'D']:
            chosen_transportation = user_input.upper()
            user_choices['transportation'] = transportation[chosen_transportation]
            print(f"You have chosen {transportation[chosen_transportation]}")
        else:
            print("Invalid option. Please try again")

    # Prompt user to choose accommodation
    print("Choose an accommodation type:")
    for option, accomm in accommodation.items():
        print(f"{option}: {accomm}")
    chosen_accommodation = None
    while chosen_accommodation is None:
        user_input = input("Enter your choice (A, B, C, D): ")
        if user_input.upper() in ['A', 'B', 'C', 'D']:
            chosen_accommodation = user_input.upper()
            user_choices['accommodation'] = accommodation[chosen_accommodation]
            print(f"You have chosen {accommodation[chosen_accommodation]}")
        else:
            print("Invalid option. Please try again")

    # Print user's choices
    print("\nYour trip plan:")
    for category, choice in user_choices.items():
        print(f"{category.capitalize()}: {choice}")

travel_planner()