#!/usr/bin/env python

import os
import sys
import random
import card
import itertools
import time

class deck:
	def __init__(self, cardsPerSuit = 13, suitCount = 4, deckCount = 1):
		self.verbose = True
		self.acesHigh = False
		self.indexDeck = [] # Lists every card possible in the deck. 
		self.withdrawlPile = []
		self.hand = []
		self.discardPile = []
		for i in range(0,deckCount):
			for j in range(0,suitCount):
				for k in range(0,cardsPerSuit):
					self.indexDeck.append(card.card(k,j,1))
					print self.indexDeck[len(self.indexDeck)-1].getFullCard()
		print len(self.indexDeck)
		
		self.withdrawlPile = self.indexDeck
		print len(self.hand)
	
	def ifVerbose(self,statement,localVerbose = True):
		if self.verbose == True and localVerbose == True:
			print statement
			return 0
		else:
			return 1
		
	def addCardToDeck(self, cardProfile, locVer = True):
		if isinstance(cardProfile,card.card):
			cardProfile = self.convertAces(cardProfile)
			self.indexDeck.append(cardProfile)
		elif type(cardProfile) == list:
			cardProfile = card.card(cardProfile[0],cardProfile[1],locVer)
			cardProfile = self.convertAces(cardProfile)
			self.indexDeck.append(cardProfile)
		else:
			return 0
		return cardProfile
			
		
	def convertAces(self, cardProfile, locVer = True):
		if self.getAcesHigh() == True and cardProfile.getCardValue() == 0:
			self.ifVerbose("Ace set to high", locVer)
			cardProfile.setCardValue(13)
		elif self.getAcesHigh() == False and cardProfile.getCardValue() == 13:
			self.ifVerbose("Ace set to low", locVer)
			cardProfile.setCardValue(0)
		else:
			self.ifVerbose("Ace was not converted", locVer)
		return cardProfile
		
	def getIndexDeck(self, locVer = False):
		self.ifVerbose("Full Deck: " + self.stackString(self.indexDeck),locVer)
		return self.indexDeck
	
	def setIndexDeck(self, locVer = False):
		newIndexDeck = []
		for i in range(0,len(self.withdrawlPile)):
			newIndexDeck.append(self.withdrawlPile[i])
		for i in range(0,len(self.hand)):
			newIndexDeck.append(self.hand[i])
		for i in range(0,len(self.discardPile)):
			newIndexDeck.append(self.discardPile[i])	
		self.indexDeck = newIndexDeck
		self.indexDeck = self.sortByCardValueThenSuit(self.indexDeck,locVer)
		self.toggleAcesHigh(self.getAcesHigh())
		self.ifVerbose("The index deck consists of " + str(len(self.indexDeck)) + " cards\n\n" + self.stackString(self.indexDeck), False)
			
	def getHand(self, locVer = False):
		self.ifVerbose("Hand: " + self.stackString(self.hand), locVer)
		return self.hand
	
	def setHand(self,stack):
		if type(stack) == list:
			self.hand = stack
			self.ifVerbose("Hand has been reset to a new configuration")
			self.setIndexDeck()
			return 0
		else:
			self.ifVerbose("Hand has not been reset")
			return 1
	
	def getDiscardPile(self, locVer = False):
		self.ifVerbose("Discard Pile: " + self.stackString(self.discardPile), locVer)
		return self.discardPile
		
	def getWithdrawlPile(self, locVer = False):
		self.ifVerbose("Withdrawl Pile: " + self.stackString(self.withdrawlPile), locVer)
		return self.withdrawlPile
	
	def setWithdrawlPile(self,stack):
		if type(stack) == list:
			self.withdrawlPile = stack
			self.ifVerbose("Hand has been reset to a new configuration")
			self.setIndexDeck()
			return 0
		else:
			self.ifVerbose("Hand has not been reset")
			return 1
	
	def setDiscardPile(self,stack):
		if type(stack) == list:
			self.hand = stack
			self.ifVerbose("Discard pile has been reset to a new configuration")
			self.setIndexDeck()
			return 0
		else:
			self.ifVerbose("Discard Pile has not been changed.")
			return 1
	
	def getAcesHigh(self, locVer = False):
		if self.acesHigh == True:
			self.ifVerbose("Aces are high!", locVer)
		else:
			self.ifVerbose("Aces are low!", locVer)
		return self.acesHigh
	
	def toggleAcesHigh(self,toggleOnOff=-1):
		if toggleOnOff == -1:
			if self.acesHigh == True:
				self.acesHigh = False
				self.ifVerbose("Aces are now low!")
			else:
				self.acesHigh = True
				self.ifVerbose("Aces are now high!")
		elif toggleOnOff == 0:
			self.acesHigh = False
			self.ifVerbose("Aces are set to low!")
		else:
			if self.acesHigh == True:
				return 0
			self.acesHigh = True
			self.ifVerbose("Aces are set to high!")
		
		if self.acesHigh == True:
			for i in range(0,len(self.indexDeck)):
				self.indexDeck[i] = self.convertAces(self.indexDeck[i])
			for i in range(0,len(self.withdrawlPile)):
				self.withdrawlPile[i] = self.convertAces(self.withdrawlPile[i])
			for i in range(0,len(self.hand)):
				self.hand[i] = self.convertAces(self.hand[i])
			for i in range(0,len(self.discardPile)):	
				self.discardPile[i] = self.convertAces(self.discardPile[i])

		return 0
	
	def tossCard(self, stack = [], drawlPosition = 0):
		stack.pop(drawlPosition)
		return stack
		
	def removeCardFromAll(self, cardType, instances = 0):		
		if type(cardType) == list:
			cardType = self.convertAces(card.card(cardType[0],cardType[1]))
		
		# Holds the card IDs for searching
		popList = self.findCardIDByStats(cardType.returnStatList(),self.indexDeck)
		returnedCard = []
		
		if instances == 0:
			instances = len(popList)
		else:
			newPopList = []
			for i in range(0,instances):
				newPopList.append(popList[i])
			popList = newPopList
		
		for i in range(0,len(popList)):
			for j in range(0,len(self.indexDeck)):
				if self.indexDeck[j].getCardID() == popList[i]:
					returnedCard.append(self.indexDeck[j])
		
		if len(popList) > 0:	
			for i in range(0,len(popList)):
				if self.withdrawlPile != self.removeCardFromStackByID(popList[i],self.withdrawlPile):
					popList.pop(i)
					if i+1 >= len(popList):
						break
			
		if len(popList) > 0:	
			for i in range(0,len(popList)):
				if self.discardPile != self.removeCardFromStackByID(popList[i],self.discardPile):
					popList.pop(i)
					if i+1 >= len(popList):
						break
			
		if len(popList) > 0:	
			for i in range(0,len(popList)):
				if self.hand != self.removeCardFromStackByID(popList[i],self.hand):
					popList.pop(i)
					if i+1 >= len(popList):
						break
						
		return returnedCard
		
	
	def removeCardFromStackByID(self,cardProfile,stack):
		if isinstance(cardProfile,card.card):
			cardProfile = cardProfile.getCardID()
	
		for i in range(0,len(stack)):
			if stack[i].getCardID() == cardProfile:
				stack.pop(i)
				self.ifVerbose("Card was removed from the stack!")
				self.setIndexDeck()
				return stack
		
		self.ifVerbose("Card does not exist in the stack!")
		return 1
				
	
	def findCardIDByStats(self, cardStats = [], stack = []):
		tempCard = card.card(cardStats[0],cardStats[1])
		tempList = []
		for i in range(0,len(self.indexDeck)):
			if self.indexDeck[i].returnStatList() == tempCard.returnStatList():
				tempList.append(self.indexDeck[i].getCardID())
		return tempList
		
	
	def withdrawlByCardStats(self, stats = [-1,-1]):
		if self.getAcesHigh() and stats[0] == 0:
			stats[0] = 13
		elif not self.getAcesHigh()and stats[0] == 13:
			stats[0] = 0
		
		for i in range(0,len(self.hand)):
			if self.hand[i].returnStatList() == stats:
				self.ifVerbose(self.discardPile[i].getFullCard() + " was withdrawn from position " + str(i) + " of the discard pile")
				self.withdrawl(i)
				i = len(self.hand)
				return 0
		self.ifVerbose("There was no " + card.card(stats[0],stats[1]).getFullCard() + " available in the discard pile!")	
	
	def withdrawl(self,drawlPosition = 0):
		selected_card = self.hand.pop(drawlPosition)
		self.ifVerbose(str(selected_card.getFullCard()) + " has been withdrawn!")
		return selected_card
		
	def discardByCardStats(self, stats = [-1,-1]):
		if self.getAcesHigh() == True and stats[0] == 0:
			stats[0] = 13
		elif self.getAcesHigh() == False and stats[0] == 13:
			stats[0] = 0
		
		for i in range(0,len(self.hand)):
			if self.hand[i].returnStatList() == stats:
				self.ifVerbose(self.hand[i].getFullCard() + " was discarded from position " + str(i) + " of the hand")
				self.discard(i)
				i = len(self.hand)
				return 0
		self.ifVerbose("There was no " + card.card(stats[0],stats[1]).getFullCard() + " available in the hand!")		
		return 1

	def discard(self, drawlPosition = 0):
		self.ifVerbose(str(self.hand[drawlPosition].getFullCard()) + " has been discarded!")
		self.discardPile.append(self.hand.pop(drawlPosition))		
				
	def findCardByID(self, cardProfile, stack = [], locVer = True):
		if isinstance(cardProfile,card.card):
			cardProfile = cardProfile.getCardID()
		
		for i in range(0,len(stack)):
			if cardProfile == stack[i].getCardID():
				return i
			
		return 0
			
		
	def sortByCardValue(self, stack = [], locVer = True):
		stack = sorted(stack,key=lambda x: (x.getCardValue()))
		self.ifVerbose("Sorted by card value: " + self.stackString(stack), locVer)
		return stack
		
	def sortByCardID(self, stack = [], locVer = True):
		stack = sorted(stack,key=lambda x: (x.getCardID()))
		self.ifVerbose("Sorted by card ID: " + self.stackString(stack), locVer)
		return stack
		
	def sortBySuit(self, stack = [],locVer = True):
		stack = sorted(stack,key=lambda x: (x.getSuit()))
		self.ifVerbose("Sorted by card suit: " + self.stackString(stack), locVer)
		return stack
		
	def sortByCardValueThenSuit(self, stack = [],locVer = False):
		stack = self.sortByCardValue(stack,locVer)
		stack = self.sortBySuit(stack,locVer)
		return stack
			
	def sortBySuitThenCardValue(self, stack = [], locVer = False):
		stack = self.sortBySuit(stack,locVer)
		stack = self.sortByCardValue(stack,locVer)
		return stack
		
	def ofAKind(self,similarCards=2,stack = [], byCardValueOrSuit = 0):
		if len(stack) >= similarCards:
			if byCardValueOrSuit == 0:
				stack = list(itertools.combinations(self.sortByCardValue(stack),similarCards))
				combinations = []
				for i in range(0,len(stack)):
					for j in range(1,similarCards):
						if stack[i][j-1].getCardValue() != stack[i][j].getCardValue():
							break
						if j == similarCards-1:
							combinations.append(stack[i])			
				return combinations	
						
			else:
				if byCardValueOrSuit == 1:
					stack = list(itertools.combinations(self.sortBySuit(stack),similarCards))
					combinations = []
					for i in range(0,len(stack)):
						for j in range(1,similarCards):
							if stack[i][j-1].getSuit() != stack[i][j].getSuit():
								break
							if j == similarCards-1:
								combinations.append(stack[i])			
					return combinations			
						
	def stackString(self, stack = []):
		temp_string = "["
		
		for i in range(0,len(stack)):
			indiv_card_stat = stack[i].getFullCard()
			temp_string += indiv_card_stat
			if i < len(stack)-1:
				temp_string += ','
		return temp_string + "]" 
		
	def shuffle(self):	
		random.shuffle(self.hand)
		self.ifVerbose("Deck has been shuffled!: " + self.stackString(self.hand))
		

deck2 = deck(13,4,2)
print deck2.stackString(deck2.getIndexDeck())
deck2.toggleAcesHigh(1)
deck2.addCardToDeck([0,0])
print deck2.removeCardFromAll(['10','c'],1)
print deck2.stackString(deck2.getIndexDeck())
print deck2.stackString(deck2.sortByCardValueThenSuit(deck2.getWithdrawlPile()))
print deck2.stackString(deck2.getWithdrawlPile())
cardIden = deck2.getWithdrawlPile()[random.randrange(0,len(deck2.getWithdrawlPile()))]

newTime = time.time()
stack = deck2.sortByCardID(deck2.getWithdrawlPile())
deck2.findCardByID(cardIden,deck2.getWithdrawlPile())
print time.time()-newTime

