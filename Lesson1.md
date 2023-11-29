# Lesson 1 : Creating virtual environments and how to use pip.


#### How to create virtual environments
---
1-Create a virtual environment

```shell
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

2- Activate the environment 

```shell
> .venv\Scripts\activate
```

Note:if you are using visual studio code editor you may follow this [tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) to setup your virtual environment and activate it in windows.


#### How to use pip: Python Package Manager 
---

1- example of how to install "numpy" package

```shell
> python -m pip install numpy
```

2- example of how to uninstall "numpy" package

```shell
>python -m pip uninstall numpy
```

3- example of how to install all packages in a text file called "requirements.txt"
    the text file can be named as you want.

```shell
> pip install -r requirements.txt
```



4- example of how to uninstall all packages in a text file called "uninstall.txt"

first you need to generate the "uninstall.txt" file. To do so enter the following
commands in the terminal:

```shell
pip freeze
pip freeze > uninstall.txt
```
please note that the first pip freeze is to generate the list of the installed packages by pip. then "pip freeze > [filename.txt]" generates the textfile that will be used to uninstall the packages at once. Prior to run the uninstall command you can edit the text file to only leave in the list the packages you want to uninstall.

Now that you are ready run the following command :

```shell
> pip uninstall --yes -r uninstall.txt
```