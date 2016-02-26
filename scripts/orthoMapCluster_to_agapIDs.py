#
# Imports
#
from os.path import relpath as rp 
import pickle
import os.path
import csv
import getopt
import sys 



def get_agap(xCoord,yCoord):

	""" Returns AGAPIDs associated with a orthomap cluster 

	"""
	#
	# File system
	#
	if not os.path.isdir("../data/"):
		os.makedirs("../data/")

	pickle_name = 'oc_to_agap'

	if (os.path.isfile("../data/"+pickle_name+'.p') and os.path.isfile("../data/"+pickle_name+'.tsv')):
		# print('WARNING: unpickling old data...')
		oc_to_agap = pickle.load(open("../data/"+pickle_name+'.p','rb'))
	else:
		# print ("Mapping OrthoCluster Coordinates to AGAP IDs...")
		
		#
		# OG-to-AGAP file
		#
		try:
			path_og_to_agap = rp("/home/nho/maps/AnOrthoMap/output/OGs_AGAP.txt")
			fi = open(path_og_to_agap,"r")
		except IOError:
			path_og_to_agap = "../data/OGs_AGAP.txt"
			fi = open(path_og_to_agap,"r")

		#
		# OG-to-AGAP dict
		#
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
		# OrthoCluster-to-OG file
		#
		try:
			path_og_to_agap = rp("/home/nho/maps/AnOrthoMap/output/OG-coords.csv")
			fi = open(path_og_to_agap,"r")
		except IOError:
			path_og_to_agap = "../data/OG-coords.csv"
			fi = open(path_og_to_agap,"r")

		#
		# OrthoClusterCoords-to-OG dict
		#
		oc_to_og = {}

		fi.readline() # headers

		while True: 

			line = fi.readline()

			if line=="":
				break

			line_split = line.split(",")

			og 	= line_split[0]
			x 	= int(line_split[1])
			y 	= int(line_split[2].rstrip())

			try:
				oc_to_og[x,y].append(og)
			except KeyError:
				oc_to_og[x,y] = [og]

		fi.close()

		#
		# Join: OrthoClusterCoords-to-AGAP
		#
		oc_to_agap = {}

		for oc in oc_to_og.keys():

			ogs = oc_to_og[oc]

			for og in ogs:

				agaps = og_to_agap[og]	

				try:
					oc_to_agap[oc] += agaps
				except KeyError:
					oc_to_agap[oc] = agaps

		#
		# write dict to file 
		#
		fo = open("../data/oc_to_agap.tsv","w")

		## print "writing to file..."

		fo.write("X\tY\tAgapIDs"+"\n")

		for oc in oc_to_agap.keys():
			x = oc[0]
			y = oc[1]
			fo.write(str(x)+"\t"+str(y)+"\t"+"\t".join(oc_to_agap[oc])+"\n")

		fo.close()

		#
		# dump the dict into pickle file
		# 
		pickle.dump(oc_to_agap,open("../data/"+pickle_name+'.p','wb'))

	## print "Complete!"

	agapOut = "\t".join(oc_to_agap[xCoord,yCoord])

	print agapOut

	return agapOut


#
# Ask for input
#

def main(argv):
	xCoord = ''
	yCoord = ''
	try:
		opts, args = getopt.getopt(argv,"hx:y:",["xCoord=","yCoord="])
	except getopt.GetoptError:
		# print 'orthoMapCluster_to_agapIDs.py -x <X_coordinate> -y <Y_coordinate>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			# print 'orthoMapCluster_to_agapIDs.py -x <X_coordinate> -y <Y_coordinate>'
			sys.exit()
		elif opt in ("-x", "--xCoord"):
			xCoord = int(arg)
		elif opt in ("-y", "--yCoord"):
			yCoord = int(arg)

	get_agap(xCoord,yCoord)
	
if __name__ == "__main__":
   main(sys.argv[1:])










