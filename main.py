from pet import Pet

def main():
    print("Welcome to Digital Pet!")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"\nMeet your new pet, {pet_name}!")
    my_pet.get_status()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Teach your pet a trick")
        print("6. See learned tricks")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            if my_pet.energy >= 1:
                trick = input("What trick would you like to teach? ")
                my_pet.train(trick)
            else:
                print("Your pet is too tired to learn right now.")
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! {pet_name} will miss you!")
            break
        else:
            print("Invalid choice. Please try again.")
            
        # After each action, show status
        my_pet.get_status()

if __name__ == "__main__":
    main()