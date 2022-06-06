from pathlib import Path
import pandas as pd

def create_file_list():
	noffiles = ""
	for i in range(1):
		noffiles = input("\n\nCuántos archivos se van a analizar?: ")
		noffiles = int(noffiles)

		archivos = []
		status = []
		for i in range(1, noffiles+1):
			if i == 1:
				filenm = "JAFRANET.html"
				archivos.append(filenm)
				ff = Path(filenm).exists()
				if ff == True:
					status.append("OK")
					err = False
				else:
					status.append("Not Found")
					err = True
			else:
				filenm = "JAFRANET (" + str(i -1) + ").html"
				archivos.append(filenm)
				ff = Path(filenm).exists()
				if ff == True:
					status.append("OK")
					err = False
				else:
					status.append("Not Found")
					err = True

		d = {
			"Archivos": archivos,
			"Status": status,

		}
		d["Archivos"] = archivos

		table = pd.DataFrame(data=d)
		print(table)

		if err is True:
			print("Hay archivos no encontrados")
		else:
			print("Todos los archivos están preparados para analizar")
		
		return d["Archivos"]

create_file_list()
