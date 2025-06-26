import subprocess

class ChessBotUCI:
    def __init__(self, engine_path):
        self.engine = subprocess.Popen(engine_path, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.send_uci_command("uci")  # Start UCI communication

    def send_uci_command(self, command):
        """Send command to the UCI engine and print the response."""
        self.engine.stdin.write(command + '\n')
        self.engine.stdin.flush()
        while True:
            output = self.engine.stdout.readline().strip()
            if output == 'uciok':
                break
            print(output)

    def set_position(self, fen):
        """Set the board position using FEN notation."""
        self.send_uci_command(f"position fen {fen}")

    def get_best_move(self, time_limit=2000):
        """Request the best move from the engine."""
        self.send_uci_command(f"go movetime {time_limit}")  # Set thinking time
        while True:
            output = self.engine.stdout.readline().strip()
            if output.startswith('bestmove'):
                best_move = output.split()[1]
                return best_move

    def stop(self):
        """Stop the engine."""
        self.send_uci_command("quit")
        self.engine.stdin.close()
        self.engine.stdout.close()
        self.engine.stderr.close()
        self.engine.wait()

if __name__ == "__main__":
    # Path to the Stockfish engine (update this path according to your installation)
    engine_path = "./stockfish"  # Example for Linux/MacOS, for Windows use the full path to Stockfish
    bot = ChessBotUCI(engine_path)

    # Set the position (for example, starting position)
    bot.set_position("startpos")

    # Ask the engine for the best move within a 2-second time limit
    best_move = bot.get_best_move(time_limit=2000)
    print(f"Best move: {best_move}")

    # Stop the engine
    bot.stop()
