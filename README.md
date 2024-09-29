# CAi: The Chess AI
## A Generative Chess Bot created using Stockfish
### Overview
Consider a scenario where two players are playing chess Player A and Player B,  Player A is a very proficient player while Player B is kind of a new to this game. Player A takes the advantage by choosing white letting Player B to forcefully choose black. As we know white opens the game so Player A moves his piece to E5. 
As player B is new to the game he don't know any of the chess conventions so he randomly plays his game and at the end of the game Player A wins by a checkmate. What we see here is  Player B needed a coach, a guide that can help him to improve his game. 
So here we present **CAi** You're personalised chess AI that can effectively help you win any game by just letting the AI bot know what move your opponent has played. So in continuation with our above scenario, Player B asks for a rematch.
This time the Player B is fully prepared with our Ai bot *CAi* Player B uses *Cai* in the following ways:
1. Player B uses CAi by launching it.
2. The AI bot ask for which colour is the player B playing.
3. Player B response that he is playing black colour, On getting this response CAi waits for the opponent to move so that player B can provide the opponents move to CAi.
4. On getting the Player A move CAi responds with the most effective move Player B should play so that he can win the game.
5. This process continues until a checkmate is happened.
6. While Player A was playing aggressively he played a blunder which resulted victory of Player B depicting how strongly *CAi* was monitoring the gameplay of Player A and B.

While this function that CAi is doing can also be done using Chat GPT or other generative bots but the problem is that most of the player cannot give an efficient prompt leading to misdirection in game and response of AI models, While other models that are present in the market require for a high payment subscription for guiding and coaching and individual to be better at chess CAi provides this facility at no cost.
Below is the representation of how actually the response looks like
<p align="center">
   <img src="https://github.com/user-attachments/assets/58aa0510-885f-4992-afea-3231538b58ca" alt="image">
</p>


Let's deep dive into what CAi is and how an individual can use it in his own machine.


### Features
1. CAi Move Suggestions: CAi suggests the best move based on the current board state, utilizing the Stockfish engine.
2. User Input: Users can input their move using Standard Algebraic Notation (SAN), such as Be7 or Nh3.
3. Captured Pieces Tracking: The program tracks and displays captured pieces after each move.
4. Error Handling for Invalid Moves: If the user enters an invalid move, the program prompts them to try again.
5. Game End Detection: The program detects the end of the game (checkmate, stalemate) and notifies the user.

### Setup and Requirements
#### Prerequisites
* Python 3.x
* Stockfish Chess Engine (v12 or higher)

#### Installing Stockfish
* Linux (Debian/Ubuntu):
`sudo apt install stockfish`

* Windows or macOS: Download Stockfish from the official site. Unzip the executable and place it in a known path.

#### Python Prerequisites
* python-chess: This library is required to handle chess logic and board management.
`pip install chess`

* transformers: This library from Hugging Face is necessary for loading and using the conversational model.
`pip install transformers`

*torch: If you're using models from Hugging Face that require PyTorch, you'll need to install it. You can install it using the command below, but make sure to follow the instructions on the official PyTorch installation page for your system configuration.
`pip install torch`

You can install all dependencies at once using:
`pip install chess transformers torch`

#### Setting the Stockfish Path
In the script, ensure the Stockfish path is correctly set:

`engine = chess.engine.SimpleEngine.popen_uci("/path/to/your/stockfish")`

For Linux, the default location is `usually /usr/games/stockfish`.

#### Running the Game
Run the script in the terminal or in your IDE:

`python CAi-finalx.py`

### Example Usage

<p align="center">
   <img src="https://github.com/user-attachments/assets/b2cadc0d-d6e6-44a1-8ff4-a672cd6b3781">
</p>

<p align="center">
   <img src="https://github.com/user-attachments/assets/5fac0ffc-c08a-442f-8115-887e3505d15c">
</p>

<p align="center">
   <img src="https://github.com/user-attachments/assets/d238d9d6-c8df-4d11-abd1-db267467d4f4">
</p>

<p align="center">
   <img src="https://github.com/user-attachments/assets/832815f8-07f5-4b91-b6cb-3950fc7a17d0">
</p>

### Ethical Use of CAi

While some may view the use of CAi: The Chess AI as a form of cheating, it's essential to consider its role as a powerful educational tool rather than just a competitive advantage. By providing real-time move suggestions and strategic insights, this AI fosters a deeper understanding of chess principles and tactics, allowing players to learn and grow their skills effectively. Instead of merely winning through external assistance, users can engage in meaningful practice, analyze their gameplay, and refine their strategies, ultimately enhancing their overall performance and enjoyment of the game. 
Embracing CAi can transform the perception of "cheating" into a collaborative learning experience that empowers players to elevate their chess abilities.

## Credits
For layout creation 
https://gist.github.com/rsheldiii/2993225

## Licence
This project is open-source and free to use.

For any issues or contributions, feel free to raise issues or make pull requests on the project repository. Also this is in the development stage so there maybe errors and flaws.
