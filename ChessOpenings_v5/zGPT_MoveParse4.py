# In more simpler terms, can you describe what MoveParse and Move do?

# Certainly! Here's a simplified description of the `MoveParser` and `Move` classes:

# `MoveParser` class:
# - The `MoveParser` class is responsible for parsing the notation of a chess move and extracting the various details of the move.
# - It takes the notation as input and provides a method called `parse()` to perform the parsing.
# - Inside the `parse()` method, the notation is analyzed, and different elements of the move (such as the color, piece, castling, capture, etc.) are extracted.
# - Previously, the `parse()` method returned a dictionary with the move details, but we've updated it to create and return an instance of the `Move` class instead.

# `Move` class:
# - The `Move` class represents a single chess move and encapsulates the details of that move.
# - It has various attributes such as `notation`, `colour`, `piece`, `castling`, etc., which store the specific information about the move.
# - The `Move` class is instantiated with these details, and the object represents a single move in the game.
# - By using the `Move` class, we can create move objects that hold all the necessary information in a structured and organized manner.

# In summary, the `MoveParser` class handles the parsing of the notation and extracting move details, while the `Move` class represents a single move and holds the specific details of that move in its attributes.