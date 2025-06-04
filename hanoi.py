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

def print_poles(poles: list[PoleStack]):
    for i, pole in enumerate(poles):
        print(f"Pole {i + 1}:", end=' ')
        print_pole(pole)
        print() # New line
    print("============================================================================")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
### Below function are to be implemented by the student ###

def initalize_poles(poles: list[PoleStack], n: int = 3):
    """
    Initialize the poles with n disks on the first pole.

    Function requirement:
    - Clear any existing disks on the poles.
    - Place disks numbered from n down to 1 on the first pole. (The largest disk is at the bottom and the smallest disk is at the top.)

    Example usage:
    >>> poles = [PoleStack() for _ in range(3)]
    >>> initalize_poles(poles, 5)
    >>> print_poles(poles)
    Pole 1: 5 4 3 2 1
    Pole 2:
    Pole 3:

    Args:
        poles (list): A list of PoleStack objects.
        n (int): The number of disks to place on the first pole.
    """
    pass # TODO: Implement this function

def move_disk(origin: PoleStack, target: PoleStack):
    """
    Move the top disk from one pole to another.

    Function requirement:
    - Ensure that the origin pole is not empty before moving.
    - Ensure that the target pole is either empty or the top disk on the target pole is larger than the disk being moved.

    Example usage:
    >>> print_poles(poles)
    Pole 1: 3 2 1
    Pole 2:
    Pole 3:
    >>> move_disk(poles[0], poles[1])
    >>> print_poles(poles)
    Pole 1: 3 2
    Pole 2: 1
    Pole 3:

    Args:
        origin (PoleStack): The pole to move the disk from.
        target (PoleStack): The pole to move the disk to.
    """
    pass #  TODO: Implement this function

def check_win(poles: list[PoleStack]) -> bool:
    """
    Check if the game is won, i.e., all disks are on the last pole.
    (There are check performed to ensure the order of the disks, so no extra checks are needed here)

    Example usage:
    >>> print_poles(poles)
    Pole 1:
    Pole 2:
    Pole 3: 4 3 2 1
    >>> check_win(poles)
    True

    Args:
        poles (list): A list of PoleStack objects.
    Returns:
        bool: True if the game is won, False otherwise.
    """
    pass # TODO: Implement this function

### Chanllenging (optional), Please explain the logic behind ###
def auto_solver(n: int, origin: int, target: int, auxiliary: int):
    """
    Automatically solve the Tower of Hanoi problem using recursion.

    Function requirement:
    - Use recursion to move disks from the first pole to the last pole.
    - The function should not take any user input.
    - The function should print the moves made during the solution.

    Example usage:
    >>> x = input("Enter the number of disks to solve: ")
    >>> auto_solver(x, 1, 3, 2)
    Move disk from Pole 1 to Pole 3
    Move disk from Pole 1 to Pole 2
    Move disk from Pole 3 to Pole 2
    ...

    Tips:
    What will be the step needed to move n disks from pole 1 to pole 3?
    What will be the step needed to move n-1 disks from pole 1 to pole 2?

    Args:
        n (int): The number of disks to move.
        origin (int): The index of the origin pole (0, 1, or 2).
        target (int): The index of the target pole (0, 1, or 2).
        auxiliary (int): The index of the auxiliary pole (0, 1, or 2).
    """
    pass # TODO: Implement this function

### Extra Points (optional) ###
# The function below are not required, but if finished, it will help you later on.

def reverse(stack: PoleStack):
    """
    Reverse the order of disks in a pole.

    Function requirement:
    - Use a temporary stack to reverse the order of disks in the given pole.
    - The content in the original pole should be reversed, i.e., the largest disk should be at the top after reversal.

    Think carefully before implementing this function, there is a carveat to it.

    Example usage:
    >>> pole = PoleStack()
    >>> pole.push(3)
    >>> pole.push(2)
    >>> pole.push(1)
    >>> print_pole(pole)
    3 2 1
    >>> reverse(pole)
    >>> print_pole(pole)
    1 2 3

    Args:
        pole (PoleStack): The pole to reverse.
    """
    pass # TODO: Implement this function

def stack_insertion(stack: PoleStack, disk: int, location: int = 0):
    """
    Insert an item (disk) into a stack at a specific location.
    0 means the head of the stack (where the top item is),
    and 1 means the second item from the top, and so on.

    Function requirement:
    - Use a temporary stack to insert the disk into the correct position in the original stack.
    - The original stack should maintain its order after insertion.

    Example usage:
    >>> pole = PoleStack()
    >>> pole.push(1)
    >>> pole.push(2)
    >>> pole.push(3)
    >>> print_pole(pole)
    1 2 3
    >>> stack_insertion(pole, 4, 1)
    >>> print_pole(pole)
    1 2 4 3

    Args:
        stack (PoleStack): The stack to insert the disk into.
        disk (int): The disk to insert.
        location (int): The index of the pole where the disk should be inserted (default is 0 (the head)).
    """
    pass # TODO: Implement this function

### DO NOT MODIFY THIS FUNCTION ###
def hanoi_game(poles: list[PoleStack], n: int):

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
    