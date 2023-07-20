'''
class Counter
'''

class Counter:
    '''
    class Counter is used to count the swap moves
    '''
    def __init__(self, moves=0):
        self.moves = moves

    def get_moves(self):
        return self.moves

    def increment(self):
        self.moves += 1
