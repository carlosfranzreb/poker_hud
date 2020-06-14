"""
Class for the poker player.
"""


class Player:
    def __init__(self, username):
        self.username = username
        self.hands = 0
        self.vpip = 0
        self.pfr = 0

    def play(self, action):
        """The player has played a hand. Possible actions: 
            0 -> Fold, 1 -> Call, 2 -> Raise.
        """
        self.hands += 1
        if action > 0:  # player has either called or raised.
            vpip_total = self.vpip * (self.hands-1)
            self.vpip = (vpip_total+1) / self.hands
        if action > 1:  # player has raised
            pfr_total = self.pfr * (self.hands-1)
            self.pfr = (pfr_total+1) / self.hands

