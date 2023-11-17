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

```shell
> pip uninstall --yes -r uninstall.txt
```

