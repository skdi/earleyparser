

articulos=["la","el","las","ellos","lo","un","unos","una","unas"]
verbos=["haber","ser","estar","tener","ir","hacer","comer","poder","decir"
        ,"saber","ver","querer","vivir","venir","amar","salir","dar","cantar",
        "poner","hablar","jugar","coger","escribir","dormir","leer","volver",
        "traer","pedir","empezar","conocer"]
sustantivos={"vez","año","tiempo","dia","cosa","hombre","mujer","nicolas","parte",
             "vida","momento","forma","casa","mundo","caso","pais","lugar","persona",
             "hora","trabajo","punto","mano","manera","fin","tipo","gente","ejemplo",
             "lado","hijo","problema","cuenta","medio","palabra","niño","padre","madre",
             "cambio","historia","idea","agua","noche","ciudad","modo","nombre","familia",
             "realidad","obra","verdad","mes","razon","grupo","relacion","cuerpo","hecho"}

def comparar_articulos(palabra):
 	if(palabra=="la" or palabra=="el" or palabra == "las" or palabra == "los" or palabra =="lo" or palabra == "un" or palabra == "unos" or palabra == "una" or palabra == "unas"):
 		return 1
 	else :
 		return 0
def diccionario(palabra):
	f=o

def leerarticu():
	contador=0
	f= open("libro","r")
	informacion = f.readlines()
 	f.close()
	for linea in informacion:
		for palabra in linea.split(' '):
			if(comparar_articulos(palabra)):
				contador+=1
				print '%s) %s'%(str(contador),palabra)

			
		


leerarticu()
