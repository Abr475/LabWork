def instructions():
    """Display game instructions."""
    print(
        """

        Welcome to the greatest intellectual challenege of all time: Tic-Tac.Toe.
        This will be a showdown between your human brain and my silicon processor.

        You will make your move known by entering a number. 0 - 8. The number
        wil; correspond to the board position as illustrated:
        
    """)

def display(message):
    print(message)

def give_me_five():
    five = 5
    return 5
def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question). lower()
        return response
    display("Here's a message for you.\n")
