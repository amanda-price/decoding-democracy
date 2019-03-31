import os
rootdir = '/Users/obsidian/Documents/GitHub/decoding-democracy/decoding-democracy'

dirs = os.listdir(rootdir)

for d in dirs:
	if d.startswith("20"):
		files = os.listdir(rootdir+"/"+d)
		for f in files:
			if f.endswith(".csv"):
				date = f[:4]+"-"+f[4:6]+"-"+f[6:8]
				dateFile = open(rootdir+"/"+d+"/"+f[:-4]+"_wDate.csv","w")
				with open(rootdir+"/"+d+"/"+f) as originFile:
					for line in originFile:
						if line.startswith("ward"):
							dateFile.write("date,{}".format(line))
						else:
							dateFile.write("{},{}".format(date,line))

				dateFile.close()
				originFile.close()

