El script ya viene preconfigurado con las siguientes categorías:

- Imágenes : .jpg , .png , .gif , .svg , etc.
- Documentos : .pdf , .docx , .txt , .xlsx , .md , etc.
- Código : .py , .js , .html , .cpp , .json , etc.
- Otros : Cualquier extensión no reconocida se moverá a una carpeta llamada Otros .
He dejado algunos archivos de prueba ( test_image.jpg , test_doc.docx , etc.) en el directorio para que puedas probar el funcionamiento de inmediato.

### Cómo utilizarlo
Puedes ejecutar el script desde tu terminal de las siguientes maneras:

1. Organización de una sola vez :
   
   ```
   python analyzer.py
   ```
   Esto organizará todos los archivos que se encuentren actualmente en la carpeta del script.
2. Organizar una carpeta específica :
   
   ```
   python analyzer.py 
   "C:\Ruta\A\Tu\Carpeta"
   ```
3. Modo Observador (Tiempo Real) :
   
   ```
   python analyzer.py --watch
   ```
   El script se quedará escuchando y organizará cualquier archivo nuevo que aparezca cada 5 segundos.



   <img width="814" height="568" alt="image" src="https://github.com/user-attachments/assets/63610afd-b9aa-47ca-bc53-3c5b46d27f36" />
