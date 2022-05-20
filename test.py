def intro():
	noffiles = ""
	archivos = []
	while noffiles != 'quit':
		noffiles = input("\n\nCuántos archivos se van a analizar?: ")
		noffiles = int(noffiles)
	
		for i in range(1,noffiles+1):
			print(i)
			if noffiles == 1:
				filenm = "JAFRANET.html"
				archivos.append(filenm)
			else:
				filenm = "JAFRANET" + str(i) + ".html"
				archivos.append(filenm)
	
		print(f"Los archivos están nombrados {str(archivos)}?")
		qt = input("Correcto?: (yes/no)")
		if qt == "yes":
			return archivos
