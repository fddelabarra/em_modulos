from setuptools import setup, find_packages

setup(
    name="em_modulos",  # Nombre del paquete
    version="0.1",
    packages=find_packages(),  # Busca automáticamente todos los módulos en el paquete
    install_requires=[],  # Lista de dependencias (si tienes alguna)
    author="fddelabarra",
    author_email="fddelabarra@uc.cl",
    description="Paquete de módulos para ejercicios en Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/fddelabarra/em_modulos",  # URL del repositorio en GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versión mínima de Python
)
