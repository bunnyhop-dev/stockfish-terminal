import chess
import chess.engine

engine_path = "/usr/games/stockfish" # sudo apt install stockfish && pip install python-chess
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def get_best_move(board):
    # วิเคราะห์การเดินที่ดีที่สุดจาก Stockfish
    result = engine.play(board, chess.engine.Limit(time=2.0))
    return board.san(result.move)

def main():
    # ถามผู้ใช้ว่าจะเล่นฝั่งขาวหรือดำ
    player_side = input("Do you want to play as White or Black? (w/b): ").strip().lower()
    
    if player_side not in ['w', 'b']:
        print("Invalid choice. Please choose 'w' for White or 'b' for Black.")
        return

    board = chess.Board()
    
    # Loop
    while not board.is_game_over():
        print("\nCurrent board position:")
        print(board)

        if (player_side == 'w' and board.turn == chess.WHITE) or (player_side == 'b' and board.turn == chess.BLACK):
            # ถามการเดินของผู้ใช้
            player_move = input("Your move: ").strip()
            
            try:
                board.push_san(player_move)
            except ValueError:
                print("Invalid move. Try again.")
                continue

            # วิเคราะห์การเดินของผู้ใช้
            best_move = get_best_move(board)
            print(f"Best move for you would have been: {best_move}")

        else:
            # ถามการเดินของฝั่งตรงข้าม
            opponent_move = input("Opponent's move: ").strip()
            
            try:
                board.push_san(opponent_move)
            except ValueError:
                print("Invalid move. Try again.")
                continue
            
            # วิเคราะห์ตาถัดไปของผู้ใช้
            if not board.is_game_over():
                best_move = get_best_move(board)
                print(f"Stockfish suggests you to play: {best_move}")
        
    print("Game over")

if __name__ == "__main__":
    main()

engine.quit()

