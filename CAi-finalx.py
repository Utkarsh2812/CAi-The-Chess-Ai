import chess
import chess.engine
from transformers import AutoModelForCausalLM, AutoTokenizer

WHITE = "white"
BLACK = "black"

class Game:
    def __init__(self):
        self.gameboard = {}
        self.placePieces()
        self.printBoard()

    def placePieces(self):
        for i in range(0, 8):
            self.gameboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
            self.gameboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)

        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.gameboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
            self.gameboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])

    def printBoard(self):
        print("   a   b   c   d   e   f   g   h")
        print("  +---+---+---+---+---+---+---+---+")
        for j in range(7, -1, -1):
            print(f"{j + 1} |", end="")
            for i in range(0, 8):
                item = self.gameboard.get((i, j), " ")
                print(f" {str(item) if item != ' ' else ' '} |", end="")
            print()
            print("  +---+---+---+---+---+---+---+---+")

class Piece:
    def __init__(self, color, name):
        self.name = name
        self.Color = color

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Pawn(Piece):
    def __init__(self, color, name, direction):
        super().__init__(color, name)
        self.direction = direction

class Rook(Piece): pass
class Knight(Piece): pass
class Bishop(Piece): pass
class Queen(Piece): pass
class King(Piece): pass

# Unicode dictionary for representing pieces
uniDict = {
    WHITE: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
    BLACK: {Pawn: "♟", Rook: "♜", Knight: "♞", Bishop: "♝", King: "♚", Queen: "♛"}
}

# Initialize the chess board
board = chess.Board()

# Set up Stockfish engine
engine_path = "Update this with the correct path"  
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

# Load the conversational model from Hugging Face (DialoGPT)
tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')
model = AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')

# Function to generate a response from the model
def generate_response(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

# Function to ask user for color
def ask_user_for_color():
    user_input = input("CAi: Hi! Are you playing as white or black? ")
    return user_input.strip().lower()

# Function to get the opponent's move in SAN format
def get_user_move():
    return input("Enter your move (in SAN, e.g., Be7, Nh3): ")

# Function to reflect the move on the gameboard
def makeMove(move):
    start_square = (move.from_square % 8, move.from_square // 8)  # Convert square to (x, y)
    end_square = (move.to_square % 8, move.to_square // 8)  # Convert square to (x, y)
    
    # Update the gameboard
    game.gameboard[end_square] = game.gameboard.pop(start_square)

# Greet the user and ask for their color
user_color = ask_user_for_color()
if user_color == 'white':
    print("CAi: You will play first as white.")
else:
    print("CAi: The opponent will play first as black.")

# Create an instance of the Game
game = Game()

# Continue to interact and suggest moves based on user inputs
while not board.is_game_over():
    # CAi suggests the next move for the current turn
    if (user_color == 'white' and board.turn == chess.WHITE) or (user_color == 'black' and board.turn == chess.BLACK):
        # CAi suggests the best move based on current board state
        result = engine.play(board, chess.engine.Limit(time=0.1))
        print(f"CAi suggests: {board.san(result.move)}")
        board.push(result.move)

        # Reflect the CAi's move on the gameboard
        makeMove(result.move)

        # Print the updated chessboard after CAi's move
        game.printBoard()

    # Check if the game is over after CAi's move
    if board.is_game_over():
        break

    # Get the opponent's move from the user in SAN format
    user_move = get_user_move()

    try:
        # Use push_san to handle SAN format (e.g., Be7, Nh3)
        move = board.push_san(user_move)  # This will raise ValueError if the move is invalid

        # Reflect the user's move on the gameboard
        makeMove(move)
    except ValueError:
        print("Invalid move. Please try again.")
        continue  # Ask for the user's move again without proceeding further

    # Print the updated chessboard after the user's move
    game.printBoard()

# End the game
print("Game over!")
engine.quit()
