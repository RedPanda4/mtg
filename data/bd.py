import mtgsdk, json, os
import django.db as db

card = mtgsdk.Card.where(set="2ED").all()
# print(json.dumps(card[0].__dict__))
# card = mtgsdk.Card.where(name="Hoarding Dragon").all()
# a = json.dumps(card[0].__dict__)

# a = json.loads(open("AllSets.json").read())
# cards = a.get("AKH").get("cards")
# print(next(card for card in cards if card["number"] == "264"))

# for e in range(7):
# 	file1 = open("cards"+str(e)+".json", "w")
# 	file1.write('{"Cards":[')
# 	print(e)
# 	for i in range(e*50, e*50 + 50):
# 		print(i)
# 		cards1 = mtgsdk.Card.where(page=i).all()
# 		if len(cards1) == 0:
# 			break
# 		for card in cards1:
# 			file1.write(str(json.dumps(card.__dict__) +", "))
#
# 	file1.write("]}")
# 	file1.close()


# l = {}
# for i in range(100):
# 	sets = mtgsdk.Set.where(page=i).all()
# 	if len(sets) == 0:
# 		break
# 	for set in sets:
# 		set = json.loads(json.dumps(set.__dict__))
# 		set["cards"] = []
# 		l[set["code"]] = set
#
# cards = []
#
# for i in range(0, 7):
# 	file = open("cards" + str(i) + ".json", "r")
# 	cards.extend(json.loads(file.read())["Cards"])
# 	file.close()
#
# for card in cards:
# 	l[card["set"]]["cards"].append(card)
#

"""
Get set and cards
"""
ED2 = (mtgsdk.Set.where(code="2ED").all())[-2]
ED3 = (mtgsdk.Set.where(code="2ED").all())[-3]
ED4 = (mtgsdk.Set.where(code="2ED").all())[-4]
E10 = (mtgsdk.Set.where(code="2ED").all())[-1]

for set in [ED2, ED3, ED4, E10]:
	set = json.loads(json.dumps(set.__dict__))
	set["cards"] = []
	for i in range(10):
		cards = mtgsdk.Card.where(set=set["code"], page=i).all()
		if len(cards) == 0:
			break
		for card in cards:
			set["cards"].append(json.loads(json.dumps(card.__dict__)))
	print(set["code"] + ".json")
	file1 = open("cards/" + set["code"] + ".json", "w")
	file1.write(json.dumps(set))
	file1.close()

# for file1 in sorted(os.listdir("cards/")):
# 	filein = open("cards/"+file1, "r")
# 	text1 = json.loads(filein.read())
# 	filein.close()
# 	print(text1["code"], text1["name"], len(text1["cards"]))
