import chess

# إنشاء رقعة شطرنج جديدة
board = chess.Board()

print("--- مرحباً بك في مشروع بوت الشطرنج ---")
print("الرقعة الابتدائية:")
print(board)

# تجربة لعب نقلة افتتاحية (مثلاً e4)
board.push_san("e4")
print("\nبعد نقلة e4:")
print(board)
