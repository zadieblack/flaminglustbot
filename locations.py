#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Locations module

import bodyparts

from random import *
from enum import * 
from util import *

class Location():
	Name = ""
	NamePrep = ""
	Loc = LocInOutType.Indoors
	BeginDesc = ""
	EndDesc = ""
	BentOver = ""
	KneelingOn = ""
	SittingOn = ""
	LyingOn = ""
	Ground = "ground"
	Despite = ""
	MaleTopClothing = "tshirt"
	MaleBottomClothing = "jeans"
	FemaleTopClothing = "dress"
	FemaleBottomClothing = "panties"
	
	def RemoveMaleClothing(self):
		Penis = bodyparts.Penis()
		sTakeItOff = ""
		
		if not self.MaleTopClothing == "":
			sTakeItOff = "stripped off his " + self.MaleTopClothing + " and pulled down his " + self.MaleBottomClothing  + " exposing his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False)
		elif not self.MaleBottomClothing == "":
			sTakeItOff = "pulled down his " + self.MaleBottomClothing + " exposing his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False)
		else: 
			sTakeItOff = "was naked, his " + bodyparts.Penis.RandomDescription(bAllowLongDesc = False) + " on full display"

		sTakeItOff += bodyparts.Penis.RandomDescription(bAllowLongDesc = False)	
		
		return sTakeItOff
			
	def RemoveFemaleClothing(self):
		Vagina = bodyparts.Vagina()
		Breasts = bodyparts.Breasts()

		sTakeItOff = ""
		
		if not self.FemaleTopClothing == "":
			if CoinFlip():
				sTakeItOff += "slipped out of her " + self.FemaleTopClothing + " and pulled down her " + self.FemaleBottomClothing + ", revealing her " + Vagina.RandomDescription(bAllowLongDesc = False)
			else:
				sTakeItOff += "pulled down her " + self.FemaleBottomClothing + " and slipped out of her " + self.FemaleTopClothing + ", revealing her " + Breasts.RandomDescription(bAllowLongDesc = False)
		elif not FemaleBottomClothing == "":
			sTakeItOff = "pulled down her " + self.FemaleBottomClothing + ", revealing her " + Vagina.RandomDescription(bAllowLongDesc = False)
		else:
			sTakeItOff += "was naked, her " 
			if CoinFlip():
				sTakeItOff += Breasts.RandomDescription(bAllowLongDesc = False) 
			else:
				sTakeItOff += Vagina.RandomDescription(bAllowLongDesc = False)
			sTakeItOff += " on full display"
			
		return sTakeItOff
			
	def PutOnMaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not self.MaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up"
			else:
				sPutItOn = "pulled his " + self.MaleBottomClothing + " up and put on his " + self.MaleTopClothing
		else:
			sPutItOn = "pulled up his " + self.MaleBottomClothing
			
		return sPutItOn
		
	def PutOnFemaleClothing(self, bBottomOnly = False):
		sPutItOn = ""
		
		if not self.FemaleTopClothing == "":
			if bBottomOnly:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			else:
				sPutItOn = "wiggled into her " + self.FemaleBottomClothing + " and then he helped her into her " + self.FemaleTopClothing
		else:
			sPutItOn = "wiggled into her " + self.FemaleBottomClothing
			
		return sPutItOn
		
class PublicLocation(Location):
	HurryReason = ""
	Caught = ""
	Excuse = ""
	Consequence = ""
	AuthorityFigure = ""
	
class PrivateLocation(Location):
	pass
	
class Alley(PublicLocation):
	Name = "the alley behind the bar"
	NamePrep = "in the alley behind the bar"
	BeginDesc = "A dim yellow light over the back door of the bar was the only illumination in the alley."
	Despite = "their unsavory surroundings"
	BentOver = "a stack of pallets"
	KneelingOn = "a stack of pallets"
	SittingOn = "a stack of pallets"
	LyingOn = "a strip of cardboard"
	HurryReason = "Someone might see us"
	Caught = "'Hey! What's going on over there?' yelled the bartender."
	Excuse = "'Don't come back here!' he yelled back."
	AuthorityFigure = "the bartender"
	Consequence = "as the bartender watched them"
	Ground = "the pavement"

class Balcony(PublicLocation):
	Name = "the hotel balcony"
	NamePrep = "on the hotel balcony"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The city spread out below them and the horizon was blue ocean."
	Despite = "the fact that they were exposed to anyone who looked up"
	BentOver = "the balcony rail"
	KneelingOn = "on a patio chair"
	SittingOn = "the broad ledge of the balcony"
	LyingOn = "the reclining patio chair"
	HurryReason = "What if someone is watching?"
	Caught = "'I think those people down there are videoing us with their iPhones!"
	Excuse = "'Let's give them a show, baby!' he replied."
	AuthorityFigure = "a crowd"
	Consequence = "a small crowd gathered to watch them"
	Ground = "ground"
	MaleTopClothing = ""
	MaleBottomClothing = "boxer briefs"
	FemaleTopClothing = "bra"
	FemaleBottomClothing = "panties"

class Beach(PublicLocation):
	Name = "the beach"
	NamePrep = "at the beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "A hot sun shone down as blue waves lapped at the sand."
	Despite = "the sand that got into every crack"
	BentOver = "the sand dune"
	KneelingOn = "on the beach towel"
	SittingOn = "on the beach towel"
	LyingOn = "on the beach towel"
	HurryReason = "The lifeguard will be here any minute"
	Caught = "'What are you doing?' shouted the lifeguard."
	Excuse = "'We're just putting on lotion!' he replied."
	AuthorityFigure = "the lifeguard"
	Consequence = "the lifeguard watched"
	Ground = "tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "swim trunks"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "bikini bottoms"
	
class Boat(PrivateLocation):
	Name = "the boat"
	NamePrep = "on a boat"
	BeginDesc = "The boat rocked gently in the open water. It was a perfect day."
	Despite = "the sun beating down on them"
	BentOver = "the side rail"
	KneelingOn = "on the stern of the boat"
	SittingOn = "on the stern of the boat"
	LyingOn = "the deck"
	Ground = "deck"
	
class Bedroom(PrivateLocation):
	Name = "the bedroom"
	NamePrep = "in the bedroom"
	Despite = "some fumbling awkwardness"
	BeginDesc = "Candles were lit all around the four-poster king-sized bed."
	BentOver = "the end of the bed"
	KneelingOn = "the bed"
	SittingOn = "a stack of cushions"
	LyingOn = "the king-sized bed"
	Ground = "the thick comforter"
	FemaleBottomClothing = "sheer panties"
	
class CampingTent(PrivateLocation):
	Name = "a tent"
	NamePrep = "in a tent"
	Loc = LocInOutType.Indoors
	Despite = "the thin canvas walls of the tent"
	BeginDesc = "The tent was just big enough for two."
	BentOver = "her heavy backpack"
	KneelingOn = "a bedroll"
	SittingOn = "a bedroll"
	LyingOn = "a sleeping bag"
	Ground = "the thick sleeping bag"
	
class CarBackseat(PublicLocation):
	Name = "the backseat of the car"
	NamePrep = "in the backseat of the car"
	BeginDesc = "The couple scrambled into the backseat of the car."
	Despite = "the extremely tight space"
	BentOver = "the back seat"
	KneelingOn = "on the back seat"
	SittingOn = "on the back seat"
	LyingOn = "on the back seat"
	HurryReason = "I hear someone pulling up"
	Caught = "'There was a knock on the steamed-up window. 'Everything OK in there?' asked a cop."
	Excuse = "'Just a little engine trouble,' he replied."
	AuthorityFigure = "a policeman"
	Consequence = "the cop shone his flashlight through the window"
	Ground = "leather upholstery"
	
class Church(PublicLocation):
	Name = "the church"
	NamePrep = "in the church"
	BeginDesc = "Colored light flooded through a stained glass window."
	Despite = "the sacred atmosphere"
	BentOver = "the pulpit"
	KneelingOn = "on the altar steps"
	SittingOn = "on a pew"
	LyingOn = "on a pew"
	HurryReason = "someone will catch us in our sin"
	Caught = "'Whis is the meaning of this?' shouted the minister."
	AuthorityFigure = "the minister"
	Excuse = "'We were just praying!' he replied."
	Consequence = "as the minister looked on in horror"
	Ground = "soft carpet"
	
class Classroom(PublicLocation):
	Name = "the classroom"
	NamePrep = "in the classroom"
	BeginDesc = "The blackboard was covered in notes and the rows of student desks were straight and orderly."
	Despite = "the threat of being caught"
	BentOver = "the teacher's desk"
	KneelingOn = "on a student desk"
	SittingOn = "the teacher's desk"
	LyingOn = "the teacher's desk"
	HurryReason = "someone will catch us"
	AuthorityFigure = "someone"
	Caught = "Suddenly the door opened. A male student carrying a textbook walked in."
	Excuse = "'This isn't what it looks like!' he said."
	Consequence = "the student tugged feverishly at his crotch"
	Ground = "the floor"
	
class ClubParkingLot(PublicLocation):
	Name = "the club parking lot"
	NamePrep = "on the hood of the car in the club parking lot"
	BeginDesc = "The night was tinged with neon light and there was a distant sound of thumping bass."
	Despite = "the fact that they were in a parking lot"
	BentOver = "the hood of a car"
	KneelingOn = "the hood of a car"
	SittingOn = "the hood of a car"
	LyingOn = "the hood of the car"
	HurryReason = "Someone might see us"
	Caught = "'Hey! What's going on over there?' yelled the bouncer."
	Excuse = "'Just a little engine trouble,' he replied."
	AuthorityFigure = "a bouncer"
	Consequence = "as the bouncer watched them"
	Ground = "the hood of the car"
	
class Den(PrivateLocation):
	Name = "the den"
	NamePrep = "in the den"
	Loc = LocInOutType.Indoors
	Despite = "a little shyness"
	BeginDesc = "A fire was crackling in the fireplace of the cozy den."
	BentOver = "the arm of the couch"
	KneelingOn = "the sofa"
	SittingOn = "a thick cushion"
	LyingOn = "the sofa"
	Ground = "the thick fur rug"
	FemaleBottomClothing = "lacy silk panties"
	
class DoctorsOffice(PublicLocation):
	Name = "the doctor's office"
	NamePrep = "in the doctor's office"
	BeginDesc = "The examination table in the doctor's office had a clean sheet of paper on it."
	Despite = "the danger of being heard"
	BentOver = "the examination table"
	KneelingOn = "the examination table"
	LyingOn = "the examination table"
	SittingOn = "the examination table"
	HurryReason = "a nurse will hear us"
	Caught = "'Is everyone OK in there?' called a nurse through the door. 'I'm coming in!'"
	Excuse = "'It's alright!' he yelled."
	AuthorityFigure = "the nurse"
	Consequence = "a cute nurse in scrubs looked on in shock"
	Ground = "the floor"
	
class DormRoom(PrivateLocation):
	Name = "the dorm room"
	NamePrep = "in the dorm room"
	BeginDesc = "The narrow bed took up half the dorm room."
	Despite = "the cramped space"
	BentOver = "the desk"
	KneelingOn = "on the edge of the bed"
	SittingOn = "on the edge of the bed"
	LyingOn = "on the tiny bed"
	Ground = "the thin carpet"
	
class DressingRoom(PublicLocation):
	Name = "the dressing room"
	NamePrep = "in the dressing room"
	BeginDesc = "Whispering and giggling, they locked themselves in the dressing room."
	Despite = "the danger of being heard"
	BentOver = "the bench in the dressing room"
	KneelingOn = "on the bench in the dressing room"
	LyingOn = "on the floor"
	SittingOn = "on the dressing room bench"
	HurryReason = "they'll hear us"
	Caught = "'Excuse me? Do you need help in there?' called a store clerk."
	Excuse = "'Don't come in!' he yelled."
	AuthorityFigure = "the store clerk"
	Consequence = "the clerk shouted 'I'm calling security'"
	Ground = "the carpet"
	
class Farm(PrivateLocation):	
	Name = "the farm"
	NamePrep = "on a farm"
	Loc = LocInOutType.Outdoors
	Despite = "the mooing of nearby cows"
	BeginDesc = "A rambling wood fence encircled a field dotted with hay bales."
	BentOver = "a wood fence"
	KneelingOn = "a square hay bale"
	SittingOn = "a square hay bale" 
	LyingOn = "the lush green grass"
	Ground = "the grass"
	FemaleTopClothing = "overalls"
	FemaleBottomClothing = "panties"
	MaleTopClothing = "tshirt"
	MaleBottomClothing = "jeans"
	
class Hottub(PrivateLocation):
	Name = "the hot tub"
	NamePrep = "in the hot tub"
	Loc = LocInOutType.Outdoors
	Despite = "the heat"
	BeginDesc = "They slipped into the warm water of the hot tub."
	BentOver = "the side of the tub"
	KneelingOn = "the seat in the tub"
	SittingOn = "a seat in the tub" 
	LyingOn = "the side of the tub"
	Ground = "steaming water"
	FemaleTopClothing = "bikini"
	FemaleBottomClothing = "bikini bottoms"
	MaleTopClothing = ""
	MaleBottomClothing = "swimming trunks"
	
class Gym(PublicLocation):
	Name = "the gym"
	NamePrep = "at the gym"
	BeginDesc = "The mirrors on the wall of the gym reflected their bodies back at them."
	Despite = "the sweat which covered their bodies"
	BentOver = "a weight bench"
	KneelingOn = "on an exercise machine"
	SittingOn = "a weight bench"
	LyingOn = "a weight bench"
	HurryReason = "someone will catch us"
	Caught = "A girl wearing a leotard walked in. 'Holy fuck!' the girl said."
	Excuse = "'We are just stretching!' he yelled."
	Consequence = "the girl with the leotard watched open-mouthed"
	AuthorityFigure = "someone"
	Ground = "rubber mat"
	
class HikingTrail(PublicLocation):
	Name = "the hiking trail"
	NamePrep = "on the side of a mountain"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The hike up the mountain had been exhausting, but the stunning view was worth it."
	Despite = "the dirt and mosquitos"
	BentOver = "a large boulder"
	KneelingOn = "on a large boulder"
	SittingOn = "on a broad, smooth boulder"
	LyingOn = "a broad, smooth boulder"
	HurryReason = "someone might come up the trail"
	Caught = "They heard the crunch of heavy boots and saw that a hiker was rounding the bend of the trail."
	Excuse = "'Don't come up here, there's bears!' he called out."
	Consequence = "a bearded hiker looked on in surprise"
	AuthorityFigure = "a park ranger"
	Ground = "the rocky mountainside"
	FemaleBottomClothing = "spandex shorts"
	
class Kitchen(PrivateLocation):
	Name = "the kitchen"
	NamePrep = "in the kitchen"
	BeginDesc = "A pan of bacon was frying on the kitchen stove."
	Despite = "the crackling of cooking bacon"
	BentOver = "the counter"
	KneelingOn = "on a kitchen chair"
	SittingOn = "on the kitchen table"
	LyingOn = "on the kitchen table"
	Ground = "black and white tiled floor"
	MaleTopClothing = ""
	MaleBottomClothing = "briefs"
	FemaleTopClothing = "oversized tshirt"
	FemaleBottomClothing = "panties"
	
class Library(PublicLocation):
	Name = "the library"
	NamePrep = "in the library"
	BeginDesc = "It was quiet and stuffy amongst the stacks."
	Despite = "the need for silence"
	BentOver = "a stack of books"
	KneelingOn = "on a table strewn with books"
	SittingOn = "on a study desk"
	LyingOn = "a table strewn with books"
	HurryReason = "someone will hear us"
	Caught = "'Please, you must be quiet!' called out a librarian."
	Consequence = "the librarian listened"
	Excuse = "'We are just about to check out!' he called back."
	AuthorityFigure = "the librarian"
	Ground = "soft carpet"
	FemaleBottomClothing = "thong"
	
class MassageRoom(PrivateLocation):
	Name = "a massage room"
	NamePrep = "in a massage room"
	BeginDesc = "Ambient ocean sounds and the smell of incense filled the massage room."
	Despite = "the danger of being caught"
	BentOver = "the massage table"
	KneelingOn = "on the massage table"
	SittingOn = "on the massage table"
	LyingOn = "on the massage table"
	Ground = "soft carpet"
	FemaleTopClothing = ""
	FemaleBottomClothing = "towel"
	MaleTopClothing = ""
	MaleBottomClothing = "towel"
	
class MensRoom(PublicLocation):
	Name = "men's restroom"
	NamePrep = "in the men's restroom"
	BeginDesc = "Crude graffiti was scrawled on the walls of the cramped stall."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	LyingOn = "on the tiled floor"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Consequence = "someone called out 'Fuck her good, man'"
	AuthorityFigure = "some strange man"
	Excuse = "'Busy!' he shouted back."
	Ground = "tiled floor"
	FemaleBottomClothing = "thong"

class Office(PublicLocation):
	Name = "the office"
	NamePrep = "in the office"
	BeginDesc = "A large oak desk stood in the center of the corner office."
	Despite = "the danger of being caught"
	BentOver = "the massive desk"
	KneelingOn = "on the boss's desk"
	SittingOn = "on the surface of the desk"
	LyingOn = "on the boss's desk"
	HurryReason = "Someone will catch us!"
	Caught = "The door opened and a tall man walked in. 'Fuck, its my boss!' she said."
	Consequence = "her boss watched, open-mouthed"
	Excuse = "'This isn't what it looks like!' he shouted."
	AuthorityFigure = "your boss"
	Ground = "carpet"
	FemaleTopClothing = "gray pencil dress"
	FemaleBottomClothing = "thong panties"
	MaleTopClothing = "dress shirt"
	MaleBottomClothing = "slacks"
	
class OpenWindow(PublicLocation):
	Name = "the open window"
	NamePrep = "in front of an open window"
	BeginDesc = "Sunlight flooded through the large open window that looked down on the street."
	Despite = "the open window"
	BentOver = "the window sill"
	KneelingOn = "on the wide window sill"
	SittingOn = "on sofa in front of the window"
	LyingOn = "on the the wide window sill"
	HurryReason = "the neighbors will see us"
	Caught = "'I think the neighbors are watching us!' she said."
	AuthorityFigure = "the neighbors"
	Excuse = "'Let them,' he replied."
	Consequence = "the people next door looked on"
	Ground = "thick carpet"
	
class ParkAfterDark(PublicLocation):
	Name = "the park"
	NamePrep = "in the park after dark"
	BeginDesc = "The lush green park was transformed into a place of shadows and secrets in the moonlight."
	Despite = "being hidden only by the shadows"
	BentOver = "a park bench"
	KneelingOn = "the edge of a stone fountain"
	SittingOn = "a park bench"
	LyingOn = "on the end of a playground slide"
	HurryReason = "we'll get caught"
	Caught = "A beam of light flicked on. A night watchman was pointing it right at them."
	AuthorityFigure = "a night watchman"
	Excuse = "'This isn't what it looks like!' he shouted."
	Consequence = "the watchman enjoyed the view"
	Ground = "the ground"
	
class PoolPatio(PrivateLocation):
	Name = "the pool patio"
	NamePrep = "beside the pool"
	Loc = LocInOutType.Outdoors
	Despite = "some fumbling awkwardness"
	BeginDesc = "The sun was high in the sky and the pool water looked cool and inviting."
	BentOver = "the pool steps"
	KneelingOn = "the edge of the pool"
	SittingOn = "a deck chair"
	LyingOn = "a patio chair"
	Ground = "the pool deck"
	FemaleBottomClothing = "bikin bottoms"
	
class PrivateBeach(PrivateLocation):
	Name = "a private beach"
	NamePrep = "on a private beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The beach was lovely, and so private that she felt free to go topless."
	Despite = "the sand that got into every crack"
	BentOver = "a sand dune"
	KneelingOn = "on the beach towel"
	SittingOn = "a beach chair"
	LyingOn = "on the beach towel"
	Ground = "sand"
	MaleTopClothing = ""
	MaleBottomClothing = "speedo"
	FemaleTopClothing = ""
	FemaleBottomClothing = "g-string"
	
class Shower(PrivateLocation):
	Name = "the shower"
	NamePrep = "in the shower"
	Loc = LocInOutType.Indoors
	Despite = "the slippery floor"
	BeginDesc = "The hot shower water rained down on them."
	BentOver = "against the wall"
	KneelingOn = "the floor of the shower stall"
	SittingOn = "on a seat in the shower stall"
	LyingOn = "on the floor of the shower stall"
	Ground = "wet floor"
	FemaleTopClothing = ""
	FemaleBottomClothing = ""
	MaleTopClothing = ""
	MaleBottomClothing = ""
	
class StarbucksBathroom(PublicLocation):
	Name = "Starbucks bathroom"
	NamePrep = "in the bathroom at Starbucks"
	BeginDesc = "The bathroom at Starbucks was small and smelled of coffee."
	Despite = "the extremely cramped quarters"
	BentOver = "the toilet"
	KneelingOn = "on the toilet seat"
	SittingOn = "on the toilet"
	LyingOn = "on the tiled floor"
	HurryReason = "Someone might hear us!"
	Caught = "Someone pounded on the door and shouted 'Hurry up!'"
	Excuse = "'Busy!' he shouted back."
	Consequence = "someone called, 'I think they're having sex in the Starbucks bathroom'"
	AuthorityFigure = "a Starbucks barista"
	Ground = "tiled floor"
	
class Surf(PublicLocation):
	Name = "the surf"
	NamePrep = "in the water at the beach"
	Loc = LocInOutType.Outdoors
	BeginDesc = "A hot sun shone down as the waves crested against their bodies."
	Despite = "the breaking waves"
	BentOver = "in the water"
	KneelingOn = "in the shallow water"
	SittingOn = "in the shallow water"
	LyingOn = "the wet sand"
	HurryReason = "People will notice us!"
	Caught = "'That lifeguard is coming towards us!' she said."
	Excuse = "'Let them enjoy it, baby,' he said."
	Consequence = "the lifeguard watched"
	AuthorityFigure = "the lifeguard"
	Ground = "the dark green water"
	MaleTopClothing = ""
	MaleBottomClothing = "speedos"
	FemaleTopClothing = "skimpy bikini top"
	FemaleBottomClothing = "g-string"
	
class Woods(PublicLocation):
	Name = "the woods"
	NamePrep = "out in the woods"
	Loc = LocInOutType.Outdoors
	BeginDesc = "The leafy trees were thick in every direction."
	Despite = "the dirt and mosquitos"
	BentOver = "a mossy log"
	KneelingOn = "on a large smooth rock"
	SittingOn = "on a tree stump"
	LyingOn = "a broad, smooth boulder"
	HurryReason = "someone might see us"
	Caught = "'Oh my god, there is a homeless guy watching us,' she whispered."
	Excuse = "'Fuck off!' he yelled at the man."
	Consequence = "the homeless man watched them and masturbated"
	AuthorityFigure = "someone"
	Ground = "thick carpet of leaves"
	FemaleBottomClothing = "thong"
	
class YogaStudio(PrivateLocation):
	Name = "a yoga studio"
	NamePrep = "in a yoga studio"
	Loc = LocInOutType.Indoors
	BeginDesc = "The relaxing drone of zen meditation music filled the warm studio."
	Despite = "not having stretched properly"
	BentOver = "a large yoga ball"
	KneelingOn = "a yoga mat"
	SittingOn = "a balance ball"
	LyingOn = "a yoga mat"
	Ground = "the purple yoga mat"
	FemaleBottomClothing = "tight yoga pants"

	
class LocationSelector():
	Locations = []
	
	def __init__(self):
		for sub in PublicLocation.__subclasses__():
			self.Locations.append(sub())
			
		for sub in PrivateLocation.__subclasses__():
			self.Locations.append(sub())
	
	def Location(self, InOut = LocInOutType.Either, PubPrivType = LocPubPrivType.Either):
		ThisLoc = Location()
		MatchingLocations = []
		
		if InOut == None:
			InOut = LocInOutType.Either
		if PubPrivType == None:
			PubPrivType = LocPubPrivType.Either
		
		#print("Getting a " + str(PubPrivType) + "location and .")
		#print("Length of self.Locations[] is " + str(len(self.Locations)))
		
		if not self.Locations is None and len(self.Locations) > 0:
			for loc in self.Locations:
				#print("Loc [" + loc.Name + "] is " + str(loc.Loc) + " and " + loc.__class__.__name__)
				if InOut == LocInOutType.Either or loc.Loc == InOut:
					if PubPrivType == LocPubPrivType.Public and isinstance(loc, PublicLocation):
						MatchingLocations.append(loc)
						#print("Public location added to list.")
					elif PubPrivType == LocPubPrivType.Private and isinstance(loc, PrivateLocation):
						MatchingLocations.append(loc)
						#print("Private location added to list.")
					elif PubPrivType == LocPubPrivType.Either:
						MatchingLocations.append(loc)
						#print("Any type location added to list.")
			
			#print("Length of MatchingLocations[] is " + str(len(MatchingLocations)))
			if len(MatchingLocations) > 0:
				iRand = randint(0, len(MatchingLocations) - 1)
				ThisLoc = MatchingLocations[iRand]
		
		return ThisLoc
		
	
	