Opinion_Bot
=======================

a n-gram markov chatbot that can keep track of it's internal probability transition table

Manifest
--------
	/planning- contains files illustrating the outline of the program and future design ideas/issues


Requirements
------------
nltk
pymongo
bs4 (BeautifulSoup)
MongoHQ instance


Plan
---------
Use MongoDB to store Markov chain data/political speeches (done)
Each time we analyze a new political speech, update the transition probabilities in Mongo and add a new "Speech" document (done)
Put each politician/radio host bot on a spectrum based on their opinions 
Uses (potential final products):
	-Rush Limbot (generate new speeches in the style of a politician/radio host)
	-Have the bots complete a sentence (e.g. Rush Limbot: "I think Obama is ___")
	-Edit existing speeches in the style of a certain politician (e.g. make "Mitt Romney" version of an Obama speech)
	-Arguer that retorts things you say (or agrees with you) based on their opinions
	-Have each bot generate new words (combinations of other words) that have negative connotations of their opponents, explaining what their new word means (e.g. "sounds like ____")
	-Rate opinions/sayings of bots (like or dislike)