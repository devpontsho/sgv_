# SVG_TO_QT
Converting SVG files to PNG with color manipulations. Generating qt resource files from svgs.

#### Note : This code will only work for ``Python 3.5+`` because of ``cairosvg`` and only tested on MacOS, but the ```svg to png``` functionality does not work on windows yet.

### Requirements [Install]
```sh
pip install cairosvg
pip install pyside2
```

### PIP Install
```sh
git clone https://github.com/devpontsho/svg_to_qt.git
cd svg_to_qt
pip install .
```

### Usage
```python
from svg_to_qt.core import converter
path = "/path/to/file.svg"
converter.covert(path, color="#00000")
```

#### Converter Functions
```python 
def convert(path, color: str, replace: bool = True, output : str = '') -> None:

"""
Changes the color of the svg and converts to png.
@param path: The path to svg image.
@param color: Hex code for the color to change to. 
@param output: The output path of the new png.
@return: None.
"""
```

```python 
def generate_rcc(svgs: list, out_folder: str, color: str = '#000000', rcc_type: str = 'python') -> str:

"""
Will generate a rcc file for resources from svgs
:param svgs: The list of svgs.
:param out_folder: The output folder for the new png icons and resource file.
:param color: The color to conver the svg file to, default is black.
:param rcc_type: The language rcc to build for.
:return: str.
"""
```

```python
def add_file_to_rcc(qrc_file: str, file: str, rcc_type: str = 'python') -> None:

"""
Add file to a resource file
:param qrc_file: The resource file.
:param file: The file to add to the resource file.
:return : None.
"""
```

```python
def create_svg(data: str) -> None:

"""
Create svg from data given.
:param data: Dictionary with instructions to build svg.
:return: None.
"""
```