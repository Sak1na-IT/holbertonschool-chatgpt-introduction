def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break
            revealed_count = sum(sum(1 for cell in row if cell) for row in self.revealed)
            if revealed_count == self.width * self.height - len(self.mines):
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
