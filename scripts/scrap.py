




fi = open("./MZtoAGAMP.txt","r")


mz_to_ag = {}

while True: 

	line = fi.readline()

	if line=="":
		break

	line_split = line.split("\t")

	mz = line_split[0]
	ag = line_split[1].rstrip()

	mz_to_ag[mz]=ag

fi.close()


fi = open("./AGAMPtoAGAP.txt","r")


agm_to_agp = {}

while True: 

	line = fi.readline()

	if line=="":
		break

	line_split = line.split("\t")

	agm = line_split[0]
	agp = line_split[1].rstrip()

	agm_to_agp[agm]=agp

fi.close()


fo = open("MZtoAGAP.txt","w")

mz_to_agp = {}

for mz in mz_to_ag.keys():


	agm = mz_to_ag[mz]

	agp = agm_to_agp[agm]

	mz_to_agp[mz] = agp

	fo.write(mz+"\t"+agp)

fo.close()

a=['MZ20100861', 'MZ20103897', 'MZ20105479', 'MZ20107276', 'MZ20109627', 'MZ20119479', 'MZ20126692', 'MZ20126833', 'MZ20127612', 'MZ20129095', 'MZ20129591', 'MZ20131792', 'MZ20140329', 'MZ20141602', 'MZ20143775', 'MZ20147558', 'MZ20148261', 'MZ20148936', 'MZ20156040', 'MZ20156458', 'MZ20158558']


for i in a:

	print mz_to_agp[i]

