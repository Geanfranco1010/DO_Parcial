import json
import zipfile
import os

api_token = {"username":"geanfrancochvez","key":"4ff7964ab3c9909a9612f996dfb4d00a"}

#conectar a Kaggle
with open('C:/Users/GIANFRANCO/.kaggle/kaggle.json','w') as file:
    json.dump(api_token,file)

location = 'C:/Users/GIANFRANCO/Documents/proyecto_parcialdataset'

#Validar que la carpeta existe
if not os.path.exists(location):
    #Si no existe la carpeta, crearla
    os.mkdir(location)
else:
    #Si la carpeta existe, borrar su contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files: os.remove(os.path.join(root,name))#elimino todos los archivos
        for name in dirs:
            os.remove(os.path.join(root,name))#elimino todas las carpetas

#Descargar dataset
os.system("kaggle datasets download -d henryshan/starbucks -p C:/Users/GIANFRANCO/Documents/proyecto_parcial/dataset")

#Descomprimir el archivo de kaggle
os.chdir(location)                
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r") #lee el archivo zip
    zip_ref.extractall()#Extrae el contenido
    zip_ref.close() #cierra el archivo

