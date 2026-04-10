import os
import shutil
import logging
import time
from pathlib import Path

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_watermark():
    """Marca de agua MFL4bs"""
    watermark = r"""
    #########################################
    #                                       #
    #        ANALIZADOR DE ARCHIVOS         #
    #           By: MFL4bs                  #
    #                                       #
    #########################################
    """
    print(watermark)

# Definición de categorías y extensiones
CATEGORIES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Código": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".ts", ".json", ".xml", ".yaml", ".yml"],
    "Archivos_Comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Ejecutables": [".exe", ".msi", ".bat", ".sh"]
}

def get_category(extension):
    """Devuelve la categoría basada en la extensión del archivo."""
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Otros"

def organize_files(source_dir):
    """Organiza los archivos del directorio fuente en carpetas según su categoría."""
    source_path = Path(source_dir)
    
    if not source_path.exists():
        logging.error(f"El directorio '{source_dir}' no existe.")
        return

    logging.info(f"Escaneando y organizando archivos en: {source_path.absolute()}")

    # Obtener lista de archivos antes de empezar para evitar problemas al mover
    files = [f for f in source_path.iterdir() if f.is_file()]

    for item in files:
        # Ignorar el script propio
        if item.name == "analyzer.py" or item.name == os.path.basename(__file__):
            continue

        extension = item.suffix
        category = get_category(extension)
        
        # Crear la carpeta de categoría si no existe
        category_path = source_path / category
        if not category_path.exists():
            category_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Creada nueva carpeta de categoría: {category}")

        # Mover el archivo a su nueva ubicación
        target_path = category_path / item.name
        
        # Manejar colisiones de nombres
        if target_path.exists():
            count = 1
            while target_path.exists():
                new_name = f"{item.stem}_{count}{item.suffix}"
                target_path = category_path / new_name
                count += 1
        
        try:
            shutil.move(str(item), str(target_path))
            logging.info(f"Movido: {item.name} -> {category}/{target_path.name}")
        except Exception as e:
            logging.error(f"Error al mover {item.name}: {e}")

def watch_directory(source_dir):
    """Observa el directorio en busca de nuevos archivos y los organiza."""
    logging.info(f"Modo observador activado en: {source_dir}")
    logging.info("Presiona Ctrl+C para detener.")
    
    try:
        while True:
            organize_files(source_dir)
            time.sleep(5)  # Escanear cada 5 segundos
    except KeyboardInterrupt:
        logging.info("Modo observador detenido.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Analizador y organizador de archivos por categoría.")
    parser.add_argument("path", nargs="?", default=os.getcwd(), help="Ruta del directorio a organizar (por defecto el actual).")
    parser.add_argument("--watch", action="store_true", help="Mantener el programa ejecutándose y observar cambios.")
    
    args = parser.parse_args()
    
    print_watermark()
    
    if args.watch:
        watch_directory(args.path)
    else:
        organize_files(args.path)
