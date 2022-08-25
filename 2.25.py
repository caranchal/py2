K = "K"
Q = "Q"
R = "R"
N = "N"
B = "B"
P = "P"
box = "*"#создание шахматной доски
board = []
for i in range(8):
	row = [box for i in range(8)]
	board.append((row))
	print(board)
board = [[box for i in range(8)]for j in range(8)]
for i in  range(len(board)):
	print("\t".join(board[i]))
for i in range(8):
	row = [Q for i in range(8)]
	board.append((row))
	print(board)