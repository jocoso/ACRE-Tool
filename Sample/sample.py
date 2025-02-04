class Board:
    #`boardsize_param takes a (x, y)  tuple`
    def __init__(self, boardsize_param):
        self.board_width = boardsize_param[0]
        self.board_height = boardsize_param[1]
        self.is_running = False
    def play(self):
        self.is_running = True
        while self.is_running:
            print("Board is running...")
            user_input = str(input(">"))
            if(user_input == 'quit'):
                self.is_running = False
            else:
                print("Unknown")


