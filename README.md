# Watermark Batch Processor

Este script de Python permite agregar una marca de agua a múltiples imágenes de forma automática. Está diseñado para funcionar con una estructura de carpetas relativa al script, por lo que es fácil de mover y ejecutar en cualquier lugar.

## Características

- **Procesamiento en lote**: Procesa todas las imágenes (`.jpg`, `.jpeg`, `.png`) de la carpeta `inicial`.
- **Ajuste inteligente de tamaño**:
  - Imágenes **Horizontales**: La marca de agua se escala al **20%** del ancho de la imagen.
  - Imágenes **Verticales**: La marca de agua se escala al **50%** del ancho de la imagen.
- **Corrección de orientación**: Utiliza `ImageOps.exif_transpose` para asegurar que las fotos verticales se procesen con la orientación correcta.
- **Posicionamiento**: La marca de agua se coloca centrada en la parte inferior con un margen.

## Estructura de Carpetas

Para que el script funcione, asegúrate de tener la siguiente estructura de archivos y carpetas:

```
proyecto/
├── createImage.py        # El script principal
├── watermark/            # Carpeta para la marca de agua
│   └── sample.png        # La imagen de la marca de agua
├── inicial/              # Carpeta donde pones las fotos originales
└── result/               # Carpeta donde aparecerán las fotos editadas (se crea sola)
```

## Requisitos

- Python 3.x
- [Pillow](https://python-pillow.org/)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install Pillow
```

## Uso

1. Coloca tus fotos originales en la carpeta `inicial`.
2. Asegúrate de que el archivo de marca de agua `sample.png` esté dentro de la carpeta `watermark`.
3. Ejecuta el script:

```bash
python createImage.py
```

Las imágenes procesadas se guardarán automáticamente en la carpeta `result`.
