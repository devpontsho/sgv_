# SVG_TO_QT
Converting SVG files to PNG with color manipulations. Generating qt resource files from svgs.

#### Note : This code will only work for ``Python 3.5+`` because of ``cairosvg``

### Requirements [Install]
```sh
pip install cairosvg
pip install pyside2
```

### Install
```sh
git clone https://github.com/devpontsho/svg_.git
export PYTHONPATH="$PYTHONPATH:/path/to/svg_"
```

### Usage
```python
from svg_ import svg_
path = "/path/to/file.svg"
sgv_.covert(path, color="#00000")
```

#### Functions
```python
generate_py_rcc(path, output=''): #returns None
```

* Generate python resource file for qt.
	- path: the path the qrc file.
	- output: The output path for python resource file.
	- return: None.

```python 
convert(path, color, replace=True, output='') # Returns None
```

* Changes the color of the svg and converts to png.
	- path: The path to svg image.
	- color: Hex code for the color to change to. 
	- output: The output path of the new png.
	- return: None.

```python 
generate_rcc(svgs, out_folder, color='#000000'): # Returns the new resource.py file
```

* Will generate a rcc file for resources from svgs
	- svg: The list of svgs.
	- out_folder: The output folder for the new png icons and resource file.
	- color: The color to conver the svg file to, default is black.
	- return: Str.
