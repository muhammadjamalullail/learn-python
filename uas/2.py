emails1 = open("emails1.txt", "r")
emails2 = open("emails2.txt", "w")
for x in emails1 :
    x = x.strip("\n")
    x.replace("@fti.uniska-bjm.ac.id", "")
    print(x, file = emails2)

emails1.close()
emails2.close()