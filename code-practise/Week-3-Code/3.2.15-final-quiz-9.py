# How does this function need to be called to print yes, no, and maybe as possible options to vote for?

def votes(params):
	for vote in params:
	    print("Possible option: " + vote)

votes (['yes', 'no', 'maybe'])