#
# Imports
#
from os.path import relpath as rp 

#
# OG-to-AGAP
#
path_og_to_agap = rp("/home/nho/maps/AnOrthoMap/output/OGs_AGAP.txt")

fi = open(path_og_to_agap,"r")

og_to_agap = {}

while True: 

	line = fi.readline()

	if line=="":
		break

	line_split = line.split("\t")

	og 	= line_split[0]
	agap= line_split[1].rstrip()

	try:
		og_to_agap[og].append(agap)
	except KeyError:
		og_to_agap[og] = [agap]

fi.close()

#
#
#