#!/usr/bin/env python3
"""
Setup script para el proyecto Gestor de Tareas con Lista Enlazada.
Este archivo permite instalar el proyecto como un paquete Python.
"""

from setuptools import setup, find_packages
import pathlib

# Directorio actual
HERE = pathlib.Path(__file__).parent

# Leer el README para la descripción larga
README = (HERE / "README.md").read_text(encoding="utf-8")

# Leer requirements.txt para las dependencias
def read_requirements():
    """Lee el archivo requirements.txt y retorna una lista de dependencias."""
    requirements_file = HERE / "requirements.txt"
    if requirements_file.exists():
        with open(requirements_file, 'r', encoding='utf-8') as f:
            return [
                line.strip() 
                for line in f 
                if line.strip() and not line.startswith('#')
            ]
    return []

setup(
    name="gestor-tareas-lista-enlazada",
    version="1.0.0",
    description="Gestor de tareas educativo implementando lista enlazada y patrón MVC",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/usuario/gestor-tareas-lista-enlazada",
    author="Estudiante",
    author_email="estudiante@ejemplo.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-flask>=1.2.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "gestor-consola=main:main",
            "gestor-web=mi_paquete.app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "mi_paquete": ["templates/*.html"],
    },
    project_urls={
        "Bug Reports": "https://github.com/usuario/gestor-tareas-lista-enlazada/issues",
        "Source": "https://github.com/usuario/gestor-tareas-lista-enlazada",
        "Documentation": "https://github.com/usuario/gestor-tareas-lista-enlazada#readme",
    },
)