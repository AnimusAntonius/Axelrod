Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

Name = 'Schnitzel'
    classifier = {
        'memory_depth': float('inf'),
        'stochastic': False,
        'makes_use_of': {'length'},
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def __init__(self, lookup_table): 
        self.lookup_table = lookup_table

 def strategy(self, opponent):
	# If there isn't enough history to lookup an action, cooperate.
        if len(self.history) < 2:
            return C

        # Get my own last two actions
        my_history = ''.join(self.history[-2:])

        # Do the same for the opponent.
        opponent_history = ''.join(opponent.history[-2:])

        # Get the opponents first two actions.
        opponent_start = ''.join(opponent.history[:2])

        # Put these three strings together in a tuple.
        key = (opponent_start, my_history, opponent_history)

        # Look up the action associated with that tuple in the lookup table.
        action = self.lookup_table[key]

        return action

    # Keys for the lookup table with (opponent's starting actions, the opponent's recent actions, and my recent actions) : 'My action'
    # I'm not exactly sure how to edit this to make it work. 

	lookup_table = {
	    ...
	    ('CC', 'CC', 'DD') : 'C',
	    ('DD', 'CC', 'DD') : 'D',
	    ('CD', 'CC', 'DD') : 'C',
	    ('DC', 'CC', 'DD') : 'C',
	    ('CC', 'DC', 'DD') : 'C',
	    ('DD', 'DC', 'DD') : 'D',
	    ('CD', 'DC', 'DD') : 'D',
	    ('DC', 'DC', 'DD') : 'C',
	    ('CC', 'CD', 'DD') : 'D',
	    ('DD', 'CD', 'DD') : 'C',
	    ('CD', 'CD', 'DD') : 'C',
	    ('DC', 'CD', 'DD') : 'C',
	    ('CC', 'DD', 'DD') : 'D',
	    ('DD', 'DD', 'DD') : 'D',
	    ('CD', 'DD', 'DD') : 'D',
	    ('DC', 'DD', 'DD') : 'D',
	    ...
	    ('CC', 'CC', 'DC') : 'D',
	    ('DD', 'CC', 'DC') : 'C',
	    ('CD', 'CC', 'DC') : 'C',
	    ('DC', 'CC', 'DC') : 'C',
	    ('CC', 'DC', 'DC') : 'C',
	    ('DD', 'DC', 'DC') : 'C',
	    ('CD', 'DC', 'DC') : 'C',
	    ('DC', 'DC', 'DC') : 'C',
	    ('CC', 'CD', 'DC') : 'C',
	    ('DD', 'CD', 'DC') : 'C',
	    ('CD', 'CD', 'DC') : 'C',
	    ('DC', 'CD', 'DC') : 'C',
	    ('CC', 'DD', 'DC') : 'D',
	    ('DD', 'DD', 'DC') : 'D',
	    ('CD', 'DD', 'DC') : 'D',
	    ('DC', 'DD', 'DC') : 'D',
	    ...
	    ('CC', 'CC', 'CD') : 'C',
	    ('DD', 'CC', 'CD') : 'D',
	    ('CD', 'CC', 'CD') : 'C',
	    ('DC', 'CC', 'CD') : 'C',
	    ('CC', 'DC', 'CD') : 'C',
	    ('DD', 'DC', 'CD') : 'D',
	    ('CD', 'DC', 'CD') : 'C',
	    ('DC', 'DC', 'CD') : 'D',
	    ('CC', 'CD', 'CD') : 'D',
	    ('DD', 'CD', 'CD') : 'D',
	    ('CD', 'CD', 'CD') : 'C',
	    ('DC', 'CD', 'CD') : 'D',
	    ('CC', 'DD', 'CD') : 'D',
	    ('DD', 'DD', 'CD') : 'D',
	    ('CD', 'DD', 'CD') : 'D',
	    ('DC', 'DD', 'CD') : 'D',
	    ...
	    ('CC', 'CC', 'CC') : 'D',
	    ('DD', 'CC', 'CC') : 'C',
	    ('CD', 'CC', 'CC') : 'C',
	    ('DC', 'CC', 'CC') : 'C',
	    ('CC', 'DC', 'CC') : 'C',
	    ('DD', 'DC', 'CC') : 'D',
	    ('CD', 'DC', 'CC') : 'C',
	    ('DC', 'DC', 'CC') : 'C',
	    ('CC', 'CD', 'CC') : 'D',
	    ('DD', 'CD', 'CC') : 'D',
	    ('CD', 'CD', 'CC') : 'D',
	    ('DC', 'CD', 'CC') : 'D',
	    ('CC', 'DD', 'CC') : 'D',
	    ('DD', 'DD', 'CC') : 'D',
	    ('CD', 'DD', 'CC') : 'D',
	    ('DC', 'DD', 'CC') : 'D',
	    ...
	}
## EVERYTHING BELOW THIS LINE I WROTE BEFORE I TRIED USING THE LOOKUP FUNCTION
    # First two moves
    if len(self.history) < 2:
	return C

    # Get the opponent's last two actions
    opponent_actions = opponent.history [-2:]
    # Use it to look up my action
    my_action = looup_table[opponent_actions]
    return my_action

    # if this is either the last or second-to-last turn, defect
    if len(opponent.history) > (self.tournament_attributes['length'] - 3):
        return D

    # if the opponent did not defect on any of the first six turns,
    # and we are not in the last 20 turns, cooperate
    if len(opponent.history) < 80:
        if len(opponent.history) > 6:
            if D not in opponent.history[:7]:
                 return C

    # if the total number of defections by the opponent is 
    # greater than four, always defect (This would make use of the "not nice" punishment" strategy"
    # However, if there is noise I should look at putting in a % error forgiveness
    if opponent.defections > 4:
        return D

    # failsafe; if none of the other conditions are true,
    # cooperate
    return C
