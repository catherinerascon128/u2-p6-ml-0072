import pandas as pd 
import numpy as np

serie_amigos = ["pedrini","mati","alonsini","andresini","michelin","caleb","cath"]
print("----series listado de amigos NC = 0072----")
amigo=pd.Series(serie_amigos)
print(amigo)

serie_billetes= [20,50,100,200,500,1000]
print("----series listado de billetes MX NC = 0072----")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes= [20,50,100,200,500,1000]
serie_bletras= ["veinte","cincuenta","cien","doscientos","quiñientos","mil"]
print("----series listado nombre y valor de billetes MX NC = 0072----")
tabla_billete=pd.Series(serie_billetes,serie_bletras)
print(tabla_billete)

# diccionario data frame
# diccionario de valor de monedas y nombre
print("datos de diccionario a dataframe en pandas NC = 0072")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras": ["veinte","cincuenta","cien","doscientos","quiñientos","mil"],
}
tabla_cath=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tabla_cath)

print("casa de cambio de catherine eileen huerta rascon NC = 0072")