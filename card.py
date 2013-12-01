#!/usr/bin/env python

import os
import sys
import random
import datetime

class card:
	def __init__(self,cardValue=0,suit=0, verbosity = 0):
		self.verbose = verbosity
		self.setSuit(suit)
		self.setCardValue(cardValue)
		self.setCardID(-1,1)
		
	def ifVerbose(self,statement,localVerbose = True):
		if self.verbose == True and localVerbose == True:
			print statement
			return 0
		else:
			return 1
	
	## This determines if a given string for input "cardValue" is valid 
	def validCardValueStr(self,cardValue):
		validStrs = ["ACE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","JACK","QUEEN","KING",
					 "A","2","3","4","5","6","7","8","9","10","J","Q","K","JOKER", "WILD", "JO", "W"]
		for i in range(0,len(validStrs)):
			if cardValue.upper() == validStrs[i]:
				if i < 26:
					return True, i%13
				else:
					return True, 14
		return False,-1
	
	## Allows card's numerical value to be changed initially and after the 
	## initial value has been assigned
	def setCardValue(self,cardValue):
		if type(cardValue) == int and cardValue >= 0 and cardValue < 15:
			self.ifVerbose("Card value set to " + str(cardValue))
			self.cardValue = cardValue
			return True 
		elif (type(cardValue) == str or type(cardValue)==chr) and self.validCardValueStr(cardValue):
			null,cardNum = self.validCardValueStr(cardValue)
			if cardNum != -1:
				self.cardValue = cardNum
				self.ifVerbose("Card value set to " + str(cardNum))
				return True
			else:
				self.ifVerbose("Card value could not be set")
				return False
	
	## Returns the cards value in a variety of ways 
	def getCardValue(self,outputType=0):
		if outputType <= 0 or outputType > 4:
			return self.cardValue
		elif outputType == 1:
			valueList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','W']
			return valueList[self.cardValue]
		elif outputType == 2:
			valueList = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace', 'Wild']
			return valueList[self.cardValue]
		elif outputType == 3:
			valueList = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace','Wild']
			return valueList[self.cardValue]	
	
	## Returns if a suit was given a valid string for a name and also the suit value
	def validSuitStr(self,suit):
		validStrs = ["C","D","H","S","W","CLUBS", "DIAMONDS","HEARTS","SPADES", "WILD", "CLUB", "DIAMOND","HEART","SPADE"]
		for i in range(0,len(validStrs)):
			if suit.upper() == validStrs[i]:
			
				return True, i%5
		return False,-1
	
	## Sets the card suit initially and can be used after initialization
	def setSuit(self,suit):
		if type(suit) == int and suit >= 0 and suit < 5:
			self.ifVerbose("Suit set to " + str(suit))
			self.suit = suit
			return True
		elif (type(suit) == str or type(suit)==chr) and self.validSuitStr(suit):
			null,suitNum = self.validSuitStr(suit)
			if suitNum != -1:
				self.suit = suitNum
				self.ifVerbose("Suit set to " + str(suitNum))
				return True
			else:
				self.ifVerbose("Suit could not be set")
				return False
		else:
			self.ifVerbose("Suit could not be set")
			return False
	
	# Gets the suit value for the card an returns it in a variety of ways
	def getSuit(self,outputType=0, noWild = 1):
		if outputType <= 0 or outputType > 4:
			return self.suit
		elif outputType == 1:
			valueList = ['C','D','H','S','W']
		elif outputType == 2:
			valueList = ['Clubs', 'Diamonds', 'Hearts', 'Spades','Wild']
		elif outputType == 3:
			valueList = ['Club', 'Diamond', 'Heart', 'Spade', 'Wild']
		
		if self.suit == 4 and noWild == 1:
			return ''
		else:
			return valueList[self.suit]

	## Returns "full card" string (ie, Ace of Spades = AS, Ten of Diamonds = 10D) 
	## This can be used to display full names like "Ace of Spades" through setting
	## function variables.
	def getFullCard(self,cardValueOutputType = 1, suitOutputType = 1, dividerStr = ""):
		return str(self.getCardValue(cardValueOutputType)) + str(dividerStr) + str(self.getSuit(suitOutputType))
		
	def setCardID(self, newID = -1, locVer = 0):
		if int(newID) > 0:
			self.cardID = newID
			self.ifVerbose("Card ID set to: " + str(self.cardID))
			return 0
		else:	
			self.cardID = ((datetime.datetime.now().microsecond)*random.randrange(1,100))**5+random.randrange(0,10)
			self.ifVerbose("Card ID set to: " + str(self.cardID))
			return 0
		self.ifVerbose("Card ID could not be set!")
		return 1
		
	def getCardID(self, locVer = 0):
		self.ifVerbose("Card ID set to: " + str(self.cardID), locVer)
		return self.cardID
		
	## Returns a list that can be used for sorting purposes
	def returnStatList(self):
		return [self.getCardValue(), self.getSuit()]
