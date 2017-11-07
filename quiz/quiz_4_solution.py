ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        if winning_states is None:
            self.winning_states = []
        else:
            self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        if len(self.winning_states) == 0:
            return self.name + ' has not won any state yet.'
        
        return self.name + ' has won ' + ', '.join(self.winning_states)+'.'

    def win_state(self, state):
        """Adds a tate to winning_states and update votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS.get(state,0)

    def __gt__(self, other):
        return self.votes > other.votes

def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes=55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    # trump.win_state('PR')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()
