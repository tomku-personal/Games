# -*- coding: utf-8 -*-
"""
Classes to model a deck of playing cards and related basic functionalities 
Created on Mon Sep 01 11:21:32 2014

@author: Tom
"""
class Card(object):

    # default single-character reprsentation of high rank values.
    # YYY: Assumes only single representation of numerical rank.
    rank_mapping = [(10, 'T'), 
                (11, 'J'), 
                (12, 'Q'),
                (13, 'K'), 
                (14, 'A')]
    rank_val, rank_str = zip(*rank_mapping)
    str_2_rank = dict(zip(rank_str, rank_val))
    rank_2_str = dict(zip(rank_val, rank_str))
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = Card.str_2_rank.get(rank, rank)
        
    def __str__(self):
        
        return '{s}{r}'.format(s = self.suit, 
                               r = Card.rank_2_str.get(self.rank, self.rank))
    
    def __repr__(self):
        return 'Card({s}, {r})'.format(s = self.suit, r = self.rank)

# this only runs if the module was *not* imported
if __name__ == '__main__':
    from random import randrange
    deck = [Card(s, r) for r in range(2, 14) for s in ['S', 'H', 'D', 'C']]
    print deck[randrange(len(deck))]