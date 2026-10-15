import random

def vacuum_cleaner_agent():
    rooms = {
        'A': random.choice(['Dirty', 'Clean']),
        'B': random.choice(['Dirty', 'Clean'])
    }

    print("Initial Environment State:")
    print(rooms)

    current_room = 'A'
    cost = 0  

    print("\nAgent starts at room:", current_room)

    while rooms['A'] == 'Dirty' or rooms['B'] == 'Dirty':
        print(f"\nAgent is in room {current_room}. Status: {rooms[current_room]}")

        if rooms[current_room] == 'Dirty':
            print(f"Room {current_room} is dirty. Cleaning...")
            rooms[current_room] = 'Clean'
            cost += 1
        else:
            print(f"Room {current_room} is already clean. Moving to the other room.")
            current_room = 'B' if current_room == 'A' else 'A'
            cost += 1

        print("Current Environment State:", rooms)

    print("\nBoth rooms are clean!")
    print("Final Environment State:", rooms)
    print("Total cost (actions taken):", cost)

if __name__ == "__main__":
    vacuum_cleaner_agent()

def vacuum_cleaner(location, status):
    
    print(f"Current Location: {location}, Status: {status}")
    
    
    if status == 'Dirty':
        print("Action: Suck (Cleaning room )")
        status = 'Clean'
        print("Room  is now Clean.\n")
        
    
    elif location == 'A':
        print("Action: Move Right to Room B\n")
        location = 'B'
        
        status_b = 'Dirty' 
        vacuum_cleaner(location, status_b)
        

    elif location == 'B':
        print("Action: Move Left to Room A")
        print("Both rooms are checked and clean! Stopping.\n")


if __name__ == "__main__":
    initial_location = input("room name")
    initial_status = input("state")
    
    print("--- Start Vacuum Cleaner Simulation ---")
    vacuum_cleaner(initial_location, initial_status)
