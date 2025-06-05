import os
class PoleStack:
    """
    A simple, pre-determined stack implementation for the Tower of Hanoi problem.
    Student can ONLY uses the functions defined in the class to complete the problem.
    """

    def __init__(self):
        self.__stack = []

    def push(self, pole):
        self.__stack.append(pole)

    def pop(self):
        if not self.__stack:
            raise IndexError("pop from empty stack")
        return self.__stack.pop()

    def peek(self):
        if not self.__stack:
            return None
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

### DO NOT MODIFY THE FUNCTIONS IN THIS SECTION ###
def print_pole(pole: PoleStack):
    string = ""

    if pole.is_empty():
        return string
    
    item = pole.pop()
    string += str(item) + " "
    print_pole(pole)
    pole.push(item)  # Push the item back to maintain the original stack order
    print(string, end=' ')

def print_poles(poles):
    for i, pole in enumerate(poles):
        print(f"Pole {i + 1}:", end=' ')
        print_pole(pole)
        print() # New line
    print("============================================================================")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
### Below function are to be implemented by the student ###

def initalize_poles(poles, n: int = 3):
    pass # TODO: Implement this function

def move_disk(origin: PoleStack, target: PoleStack):
    pass # TODO: Implement this function

def check_win(poles) -> bool:
    pass # TODO: Implement this function

### Extra Points (optional) ###
# The function below are not required, but if finished, it will help you later on.

def reverse(stack: PoleStack):
    pass # TODO: Implement this function

def stack_insertion(stack: PoleStack, disk: int, location: int = 0):
    pass # TODO: Implement this function

### Chanllenging (optional), Please explain the logic behind ###
def auto_solver(n: int, origin: int, target: int, auxiliary: int):
    pass # TODO: Implement this function

### DO NOT MODIFY THIS FUNCTION ###
def hanoi_game(poles, n: int):

    ### Initialization block ###
    # Requirement: Initialize the poles with n disks on the first pole.
    clear_screen()
    print(f"Starting the game with {n} disks...")
    initalize_poles(poles, n)

    num_moves = 0
    while True:
        print_poles(poles)
        print("How would you like to move the disks?")

        ### User input prompt block ###
        # Requirement: Ask the user to input the origin and target poles.
        # Ensure the input is valid (1, 2, 3 e.t.c.) and not the same pole.
        try:
            origin = int(input("Enter the origin pole (1, 2, or 3...): ")) - 1
            target = int(input("Enter the target pole (1, 2, or 3...): ")) - 1
            if origin < 0 or origin >= len(poles) or target < 0 or target >= len(poles) or origin == target:
                clear_screen()
                print("Invalid pole number. Please try again.")
                continue
        except ValueError:
            clear_screen()
            print("Invalid input. Please enter numbers only.")
            continue

        ### Hanoi logic block ###
        # Requirement: Move the disk from the origin pole to the target pole.
        try:
            move_disk(poles[origin], poles[target])
            clear_screen()
            print(f"Moved disk from Pole {origin + 1} to Pole {target + 1}.")
        except ValueError as e:
            clear_screen()
            print(f"Error: {e}")
            continue

        num_moves += 1
        
        ### Final Display block ###
        # Requirement: Check if the game is finished, and display the number of moves took.
        if check_win(poles):
            print("Congratulations! You solved the Tower of Hanoi!")
            print("You solve the puzzle in {} moves.".format(num_moves))
            input("Press Enter to continue...")
            break

if __name__ == "__main__":
    poles = [PoleStack() for _ in range(3)]

    while True:
        print("Welcome to the Tower of Hanoi!")
        print("The rules are simple:")
        print("1. Only one disk can be moved at a time.")
        print("2. A disk can only be placed on top of a larger disk or on an empty pole.")
        print("3. The goal is to move all disks from the first pole to the last pole (Pole 3).")
        print("Can you solve it with the least number of moves?")
        print("============================================================================")
        print("1. Start the game (Easy)")
        print("2. Start the game (Intermediate)")
        print("3. Auto solver")
        print("4. Extra Points (Useful for later problems)")
        print("5. Exit")
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            hanoi_game(poles, 3)
        elif choice == 2:
            hanoi_game(poles, 4)
        elif choice == 3:
            clear_screen()
            n = int(input("Enter the number of disks to solve: "))
            auto_solver(n, 1, 3, 2)
            input("Press Enter to continue...")
            clear_screen()

        elif choice == 4:
            clear_screen()
            print("Testing extra functions...") # Reversing test
            test_pole = PoleStack()
            test_pole.push(3)
            test_pole.push(2)
            test_pole.push(1)
            print("Original Pole:")
            print_pole(test_pole)
            print()
            reverse(test_pole)
            print("Reversed Pole:")
            print_pole(test_pole)
            print()

            test_pole = PoleStack()             # Insertion test
            test_pole.push(1)
            test_pole.push(2)
            test_pole.push(3)
            print("Original Pole:")
            print_pole(test_pole)
            print()
            stack_insertion(test_pole, 4, 1)
            print("After Insertion:")
            print_pole(test_pole)
            print()

            input("Press Enter to continue...")
            clear_screen()
        elif choice == 5:
            print("Thank you for playing!")
            break
    