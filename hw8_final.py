import requests
import feedparser

#PART 1
slate = feedparser.parse("http://www.slate.com/all.fulltext.all.rss")
number = 0
for article in range(len(slate.entries)):
	number+=1
	print(" *"+str(number))
	print(" \t Title: "+ slate.entries[article].title)
	print(" \t Description: " +slate.entries[article].description+"\n")


userRequest = int(input("Choose an article number to read: "))
print("\n You can see that article at http://www.slate.com/all.fulltext.all.rss")
keyInput = input("\nHit Enter to continue...")

#PART 2
number = 0
for article in range(len(slate.entries)):
	number+=1
	if number == userRequest:
		print("  " +str(number))
		print(" \t Title: "+ slate.entries[article].title)
		print(" \t Description: " +slate.entries[article].description)
		continue
	print(" *"+str(number))
	print(" \t Title: "+ slate.entries[article].title)
	print(" \t Description: " +slate.entries[article].description+"\n")



