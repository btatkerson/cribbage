#!/usr/bin/env python
import card
import random
import itertools

deck = []
for j in range(0,4):
	for i in range(0,13):
		deck.append(card.card(i,j))
random.shuffle(deck)

print deck[0].returnStatList()

deck2 = []

for i in range(0,5):
	deck2.append(deck[i])

deck2 = [card.card(1,1), card.card(2,0), card.card(1,0), card.card(0,1), card.card(0,0)]
random.shuffle(deck2)

def cardSortByValue(deck = [],verbose = 0):
	print '[' if verbose == True else '',
	deck = sorted(deck,key=lambda x: (x.getCardValue()))
	for i in range(0,len(deck)):
		print (deck[i].getFullCard() + (',' if i < len(deck)-1 else '') if verbose else ''),
	print "]" if verbose else '',	
	return deck

def cardCombinations(deck=[], minimumGroupValue = 2, maximumGroupValue = 2, verbose = 0):
	lis = []
	for i in range(minimumGroupValue,maximumGroupValue+1):
		lis2 = list(itertools.combinations(deck,maximumGroupValue+1-i))
		for j in range(0,len(lis2)):
			lis.append(lis2[j])
	if verbose:
		for i in range(0,len(lis)):
			print "[",
			for j in range (0,len(lis[i])):
				print lis[i][j].getFullCard() + ("," if j != len(lis[i])-1 else ''),
			print "]"
	return lis


def sortDeckCombinations(deck = [], verbose = 0):
	for i in range (0,len(deck)):
		deck[i] = cardSortByValue(deck[i])
		if verbose:
			print "[",
			for j in range(0,len(deck[i])):
				print deck[i][j].getFullCard() + ("," if j != len(deck[i])-1 else ''),
			print "]"
	
	return deck		

deckCombos = []	
deckCombos = sortDeckCombinations(cardCombinations(deck2,1,5,1),1)


	
	
def flush(x = []):
	if len(x) != 5:
		null


	
