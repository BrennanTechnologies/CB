#import csv


file = open('jobs_in_data.txt', "r")
print(file.read())

# txt = file.read()
# for row in txt:
# 	print("row: " + str(row))
# print(txt)






exit()
with open('jobs_in_data.csv', 'r', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	print(spamreader)
	# for row in spamreader:
	# 	print(row)
	# 	#print(', '.join(row))


# import pandas as pd
# df = pd.read_csv('Practicejobs_in_data.csv')