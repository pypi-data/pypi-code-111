from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pyqtlet2',
    version='0.6.1',
    description='Bringing leaflet maps to PyQt',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Leon Friedmann',
    author_email='leon.friedmann@tum.de',
    url='https://github.com/JaWeilBaum/pyqtlet2',
    keywords='leaflet, pyqt, maps, python, python3',
    classifiers=[],
    packages=[
        'pyqtlet2',
        'pyqtlet2.leaflet',
        'pyqtlet2.leaflet.control',
        'pyqtlet2.leaflet.core',
        'pyqtlet2.leaflet.layer',
        'pyqtlet2.leaflet.layer.marker',
        'pyqtlet2.leaflet.layer.tile',
        'pyqtlet2.leaflet.layer.vector',
        'pyqtlet2.leaflet.layer.icon',
        'pyqtlet2.leaflet.map',
    ],
    package_data={
        'pyqtlet2': [
            'web/map.html',
            'web/custom.js',
            'web/modules/*/*',
            'web/modules/*/images/*',
        ],
    },
    install_requires=[
        'PyQt5==5.15.5',
        'PyQtWebEngine==5.15.5'
    ]
)


