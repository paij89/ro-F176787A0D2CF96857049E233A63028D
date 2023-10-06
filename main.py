
class Player:
    def play(self):
        print("Player is playing cricket")

class Batsman(Player):
    def play(self):
        print("Batsman is batting")

class Bowler(Player):
    def play(self):
        print("Bowler is bowling")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play method for each object
batsman.play()
bowler.play()