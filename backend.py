cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "rental_price": 50, "available": True},
    {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 55, "available": True},
    {"id": 3, "brand": "Ford", "model": "Focus", "rental_price": 60, "available": True},
    {"id": 4, "brand": "Tesla", "model": "Model 3", "rental_price": 120, "available": True},
]

# Dictionary to store the rental status: {car_id: (days_rented, total_cost)}
rental_status = {}


def view_available_cars():
    print("Available Cars:")
    for car in cars:
        if car['available']:
            print(f"ID: {car['id']}, {car['brand']} {car['model']}, Price: ${car['rental_price']} per day")


def rent_car(car_id, days_rented):
    car = next((car for car in cars if car["id"] == car_id), None)

    if car is None:
        print(f"Car with ID {car_id} does not exist.")
        return

    if not car['available']:
        print(f"Car with ID {car_id} is currently not available.")
        return

    total_cost = car['rental_price'] * days_rented
    rental_status[car_id] = (days_rented, total_cost)
    car['available'] = False

    print(f"You've rented {car['brand']} {car['model']} for {days_rented} days. Total cost: ${total_cost}.")


def return_car(car_id):
    car = next((car for car in cars if car["id"] == car_id), None)

    if car is None:
        print(f"Car with ID {car_id} does not exist.")
        return

    if car['available']:
        print(f"Car with ID {car_id} has not been rented.")
        return

    if car_id in rental_status:
        days_rented, total_cost = rental_status[car_id]
        print(f"You are returning {car['brand']} {car['model']}.")
        print(f"Total rental duration: {days_rented} days.")
        print(f"Total rental cost: ${total_cost}.")

        car['available'] = True
        del rental_status[car_id]
    else:
        print("Error: No rental record found for this car.")


def main():
    while True:
        print("\n1. View available cars\n2. Rent a car\n3. Return a car\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_available_cars()
        elif choice == "2":
            try:
                car_id = int(input("Enter the car ID you want to rent: "))
                days_rented = int(input("Enter the number of days you want to rent the car: "))
                rent_car(car_id, days_rented)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "3":
            try:
                car_id = int(input("Enter the car ID you want to return: "))
                return_car(car_id)
            except ValueError:
                print("Invalid input. Please enter a valid car ID.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
