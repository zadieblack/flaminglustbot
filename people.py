# People module

from random import *
from util import *

class Person(WordList):
	def GetPerson(self):
		sPerson = ""
		
		sPerson = self.GetWord()
		
		return sPerson
		
class MaleSO(Person):
	List = ['boyfriend',
			'fiancé',
			'hubby',
			'husband',
			'man',
			'partner']
			
class FemaleSO(Person):
	List = ['bride',
			'girlfriend',
			'fiancé',
			'wife',
			'partner',
			'woman']
		
class FemaleFWB(Person):
	List = ['aunt',
		'babysitter',
		'barista',
		'boss',
		'boss\'s wife',
		'CEO',
		'co-ed student',
		'cousin',
		'cute roommate',
		'dad\'s girlfriend',
		'daughter',
		'daughter\'s best friend',
		'daughter-in-law',
		'dominatrix',
		'eighth-grade teacher',
		'English teacher',
		'ex',
		'fashion model',
		'flight attendant',
		'French maid',
		'girlfriend',
		'girlfriend\'s mom',
		'girlfriend\'s sister',
		'guidance counselor',
		'hot best friend',
		'intern',
		'land lady',
		'librarian',
		'life drawing model',
		'English lit student',
		'maid',
		'marriage counselor',
		'masseuse',
		'math tutor',
		'mom\'s best friend',
		'mother-in-law',
		'next-door neighbor',
		'niece',
		'nurse',
		'parole officer',
		'pastor\'s wife',
		'personal trainer',
		'roommate\'s girlfriend',
		'secretary',
		'sister',
		'sister-in-law',
		'sister\'s hot friend',
		'soccer mom',
		'son\'s principal',
		'step-daughter',
		'step-mom',
		'step-sister',
		'Sunday School teacher',
		'teacher',
		'twin sister',
		'wedding planner',
		'wife',
		'wife\'s Avon Lady',
		'wife\'s pregnancy surrogate']
		
class MaleFWB(Person):
	List = ['attorney',
			'attractive male masseuse',
			'baby daddy',
			'bank teller',
			'barista',
			'best friend\'s fiancé',
			'billionaire fiancé',
			'bodyguard',
			'boss',
			'boy toy',
			'boyfriend',
			'brother',
			'brother-in-law',
			'celebrity crush',
			'co-worker',
			'contractor',
			'daddy',
			'daddy dom',
			'daughter\'s boyfriend',
			'dentist',
			'dom',
			'driver',
			'drug dealer',
			'ex-boyfriend',
			'father',
			'father-in-law',
			'fiancé',
			'friend-with-benefits',
			'geography teacher',
			'girlfriend',
			'guidance counselor',
			'gynecologist',
			'hubby',
			'husband',
			'landlord',
			'life coach',
			'lifeguard',
			'lord',
			'mailman',
			'manager',
			'master',
			'minister',
			'one true love',
			'pastor',
			'pediatrician',
			'personal trainer',
			'photographer',
			'pizza delivery boy',
			'pool boy',
			'priest',
			'prince',
			'proctologist',
			'professor',
			'psychiatrist',
			'shift supervisor',
			'sister\'s boyfriend',
			'son-in-law',
			'step-son',
			'tennis coach',
			'twin brother',
			'uber driver',
			'vice-principal',
			'volleyball coach',
			'yoga teacher']
			
class JobBlueCollar(Person):
	List = ['bag boy',
		'ball boy',
		'bellhop',
		'Starbucks barista',
		'beat cop',
		'blogger',
		'bus driver',
		'cattle wrangler',
		'civil servant',
		'club bouncer',
		'Comcast technician',
		'dog walker',
		'dog groomer',
		'farm hand',
		'farmer',
		'food court worker',
		'fry cook',
		'garbage man',
		'gas station attendant',
		'golf caddy',
		'gym coach',
		'home theater installer',
		'hot dog vendor',
		'high school history teacher',
		'janitor',
		'lawn maintenance man',
		'Lyft driver',
		'manager at Arby\'s',
		'masseur',
		'male nurse',
		'mall santa',
		'mechanic',
		'meter maid',
		'page boy',
		'paige',
		'peasant',
		'pest control technician',
		'pet store clerk',
		'Pizza Hut delivery guy',
		'plumber',
		'pool boy',
		'porn set fluffer',
		'postal clerk',
		'private in the army',
		'public restroom attendant',
		'rent-a-cop',
		'roadie',
		'roadkill disposal worker',
		'sea man',
		'self-published author',
		'serf',
		'server at Applebee\'s',
		'shift supervisor',
		'short-order cook',
		'stable boy',
		'stand-up comedian',
		'Whole Foods stock boy',
		'tax payer',
		'third-grade teacher',
		'ticket stub collector',
		'tow-truck driver',
		'tour guide',
		'truck driver',
		'used car salesman',
		'waiter',
		'Wal-Mart greeter',
		'wedding DJ',
		'writer of erotic romances',
		'zoo keeper']
		
class JobWhiteCollar(Person):
	List = ['accountant',
		'actuary',
		'airline pilot',
		'Apple Store genius',
		'architect',
		'banker',
		'bee keeper',
		'cakery owner',
		'city councilman',
		'civil engineer',
		'classical violinist',
		'club DJ',
		'crossword puzzle writer',
		'database developer',
		'detective',
		'executive producer',
		'guru',
		'gynecologist',
		'fashion photographer',
		'flight attendant',
		'house flipper',
		'insurance adjuster',
		'lieutenant colonel',
		'merchant',
		'middle manager',
		'motivational speaker',
		'opthamologist',
		'orthodonist',
		'pharmacist',
		'photographer',
		'podiatrist',
		'porn star',
		'principal',
		'proctologist',
		'project manager',
		'public radio host',
		'published author',
		'radio DJ',
		'rancher',
		'realtor',
		'regional manager',
		'romance novelist',
		'sex therapist',
		'sex toy designer',
		'sherriff',
		'stay-at-home dad',
		'surgeon',
		'tax attorney',
		'tenured professor',
		'urologist',
		'veterinarian',
		'web designer',
		'Wendy\'s franchise owner',
		'yoga teacher',
		'YouTube personality']
		
class JobWealthyMale(Person):
	List = ['archduke',
		'baron',
		'Bitcoin billionaire',
		'billionaire',
		'celebrity chef',
		'CEO',
		'count',
		'duke',
		'earl',
		'emperor',
		'film mogul',
		'general',
		'king',
		'knight',
		'marquess',
		'marquis',
		'movie star',
		'Nobel Prize winner',
		'Dalai Lama',
		'pope',
		'porn star',
		'president',
		'prime minister',
		'prince',
		'pro football quarterback',
		'rock star',
		'senator',
		'shah',
		'sheikh',
		'sheriff',
		'sultan',
		'surgeon general',
		'titan of industry',
		'viscount']

class JobWealthyFemale(Person): 
	List = ['actress',
		'archduchess',
		'baroness',
		'heiress',
		'CEO',
		'countess',
		'duchess',
		'empress',
		'fasion designer',
		'first lady',
		'high-born lady',
		'marchioness',
		'mother superior',
		'Nobel Prize winner',
		'porn star',
		'president',
		'princess',
		'prime minister',
		'queen',
		'queen mother',
		'pop star',
		'senator',
		'social media influencer',
		'supermodel',
		'surgeon general',
		'viscountess',
		'wealthy MILF']