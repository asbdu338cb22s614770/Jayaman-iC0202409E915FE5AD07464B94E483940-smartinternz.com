class player:
   def play (selp):
     print("The player is playing cricket.")
class Batsman(player):
   def play (selp):
       print("The batsman is batting.")
class Bowler(player):
   def play(selp):
      print("The bowler is batting.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()