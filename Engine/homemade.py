
import chess
import chess.engine
import sys

# ruff: noqa: ARG002

platform = sys.platform
file_extension = ".exe" if platform == "win32" else ""


class Stockfish(ExampleEngine):
    """A homemade engine that uses Stockfish."""

    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(f"stockfish{file_extension}")

    def search(self, board: chess.Board, time_limit: chess.engine.Limit, ponder: bool, draw_offered: bool,
               root_moves: MOVE) -> chess.engine.PlayResult:
        """Get a move using Stockfish."""
        return self.engine.play(board, time_limit)