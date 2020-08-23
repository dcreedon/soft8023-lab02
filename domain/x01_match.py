from service.match_service import MatchVisitTemplate
from service.match_service import MatchManager


def get_value_of(dart):
    multiplier = 1
    if dart[0] == 'D':
        multiplier = 2
    elif dart[0] == 'T':
        multiplier = 3

    dart_segment = dart[1:]
    total = multiplier * int(dart_segment)

    return total


class X01Match(MatchManager, MatchVisitTemplate):

    def __init__(self):
        super().__init__()
        self.p1_total = self.p2_total = 501  # switch to a dictionary

    def validate_visit(self, player, visit):
        if self.last_player is player:
            return False, "Player " + player + " is not in the correct sequence. Visit ignored."

        self.last_player = player
        return True, None

    def check_winning_condition(self, visit):
        # Loop through each dart to see if it wins the game
        for dart in visit:
            # switch this to something like a dictionary
            if self.match.player1 is self.last_player:
                self.p1_total -= get_value_of(dart)
            else:
                self.p2_total -= get_value_of(dart)
            print(dart)

    def record_statistics(self):
        pass

    def format_summary(self):
        return "Last player was " + self.last_player + "; scores remaining, P1: "\
               + str(self.p1_total) + ", P2: " + str(self.p2_total)


class X01MatchBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = X01Match()
        return self._instance
