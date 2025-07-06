
# notes to build this project:

## installing build tools

`pip install build twine`

## building and uploading

make sure to change the version number first

``` bash
python -m build
python -m twine upload dist/*
```