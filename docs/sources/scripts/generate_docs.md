#


### get_mkgendocs_config
```python
.get_mkgendocs_config()
```

---
Get the mkgendocs configuration file.


**Raises**

* **FileNotFoundError**  : If mkgendocs.yaml is not found
* **YAMLError**  : If there is an error parsing mkgendocs.yaml


**Returns**

mkgendocs configuration

----


### get_python_files
```python
.get_python_files(
   directory
)
```

---
Get a list of python files in a directory.


**Args**

* **directory**  : Directory to search


**Returns**

List of python files

----


### get_file_functions
```python
.get_file_functions(
   filename
)
```

---
Get the functions in a file.


**Args**

* **filename**  : The name of the file to parse for functions.


**Returns**

List of functions

----


### main
```python
.main()
```

---
Generate configuration for mkgendocs to build documentation.
