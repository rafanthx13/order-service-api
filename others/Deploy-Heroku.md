# Deploy Heroku Flask App

## Índice

[TOC]



## Links

## Heroku Deploy Flask App


### `Procfile`
ter na raiz o arquivo `Procfile` que vai determinar qual arquivo executar

`Procfile`

````
web: python server_txt.py
````

### `runtime.txt`

Especificar qual a versão do python usar.

O heroku aceita as versões a seguir:
````
python-3.8.3
python-3.7.7
python-3.6.10
python-2.7.18
````

Escolha uma e coloque no `runtime.txt`

Para ter a lista completa veja no [aqui](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)

as dependências podem ser colocadas de duas formas:
+ pip com `requirements.txt`
+ pipenv com `Pipfile` e `Pip.lock`

### Dependências com `pip` e `requirements.txt`

É recomendável criar um um ambiente virtual para cada projeto, para assim pode conseguir gerar para cada um `requirements.txt` que é como o `package.json` do node. Esse ambiente já vem com pip instalado.

#### Ambiente virtual com `venv`

**Instalar `venv` no python**

````sh
$ sudo apt install python3-venv
````
**Criar virtual env**

````sh
# criar
$ python3 -m venv venv
# ativar
$ source venv/bin/activate
# instalar dependencias
(venv) $ pip install flask
(venv) $ pip install flask_cors
# executar app falsk
(venv) $ export FLASK_APP=server_txt.py
(venv) $ flask run
# sair do `venv`
(venv) $ deactivate
# sair do terminal
$ exit
```

OBS:
+ As dependências instaladas ficam na pasta `venv/` que não deve ser mandada ao git.

**Criar `requirements.txt` com as dependências do projeto**

````sh
$ (venv) pip freeze > requirements.txt
````
**Instalar dependências de `requirements.txt`**

````sh
$ (venv)  install -r requirements.txt
````

**Atualizar pip**

````sh
$ pip install --upgrade pip
````

#### `requirements.txt`

o arquivo `requirements.txt` é da seguinte forma

````
click==7.1.2
Flask==1.1.2
Flask-Cors==3.0.8
future==0.18.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
numpy==1.18.5
pandas==1.0.5
Pillow==7.1.2
python-dateutil==2.8.1
pytz==2020.1
six==1.15.0
Werkzeug==1.0.1
````
Você também pode adicionar dependências apartir de seu link, terminando com a extensão `whl`

Exemplo do pytorch que usa cpu (lightweight)

`requirements.txt`

````
https://download.pytorch.org/whl/cpu/torch-1.5.1%2Bcpu-cp37-cp37m-linux_x86_64.whl
click==7.1.2
Flask==1.1.2
````

#### Deploy no heroku

````sh
$ git push heroku master
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 276 bytes | 276.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.7.4
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting flask (from -r /tmp/build_c2c067ef79ff14c9bf1aed6796f9ed1f/requirements.txt (line 1))
remote:          Downloading ...
remote:        Installing collected packages: Werkzeug, click, MarkupSafe, Jinja2, itsdangerous, flask
remote:        Successfully installed Jinja2-2.10 MarkupSafe-1.1.0 Werkzeug-0.14.1 click-7.0 flask-1.0.2 itsdangerous-1.1.0
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> (none)
remote:
````
Se não aparecer que está instalando as suas dependências, tente fazer denovo. De qualquer forma, o heroku está apto a ler o `requirements.txt`


### Dependências com ambiente virtual `pipenv`

#### Instalar 

Just use pip:
````sh
$ pip install pipenv
````

Or, if you’re using Ubuntu 17.10:

````sh
$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv
````

**Atualizar**

```sh
$ pip install --user --upgrade pipenv
```




#### Uso do `pipenv`

##### Start
Start using pipenv is easy, in your project folder type...

```sh
$ pipenv install
```

... and if it already has a requirements.txt file, it will generate a Pipfile file with the requirements and a virtual environment folder, otherwise, it will generate an empty Pipfile file. If you disliked or changed your mind about something that you have installed, just type...

##### Desinstalar pacotes

```sh
$ pipenv uninstall <package>
```

... and you're good to go. To activate the virtual environment that pipenv already generated, go with...

##### Abrir Shell para ativar ambiente `pipenv`

```sh
$ pipenv shell
```


... and your virtual environment will be activated. To leave the environment...

```sh
$ exit
```


... and you will be back to your original terminal session.

##### Pipfile
The Pipfile file is intended to specify packages requirements for your Python application or library, both to development and execution. You can install a package by simply using...

```sh
$ pipenv install flask
```


... and it will be added as a dependency for deployment and execution or by using ...

```sh
$ pipenv install --dev pytest
```


... and it will be used as a depencency for development time. The file syntax is pretty straight forward, as follows.

```
[[source]] # Here goes your package sources (where you are downloading your packages from).
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages] # Here goes your package requirements for running the application and its versions (which packages you will use when running the application).
requests = "*"
flask = "*"
pandas = "*"

[dev-packages] # Here goes your package requirements for developing the application and its versions (which packaes you will use when developing the application)
pylint = "*"
wheel = "*"

[requires] # Here goes your required Python version.
python_version = "3.6"
```

#### `Pipfile.lock`
The Pipfile.lock is intended to specify, based on the packages present in Pipfile, which specific version of those should be used, avoiding the risks of automatically upgrading packages that depend upon each other and breaking your project dependency tree.

You can lock your currently installed packages using...

```sh
$ pipenv lock
```

... and the tool will lookup your virtual environment folder to generate the lock file for you automatically, based on the currently installed versions. The file syntax is not as obvious as is for Pipfile , so for the sake of conciseness, it will not be displayed here.

##### Ver pacotes instalado no `pipenv`

```sh
$ pipenv graph
```

##### Desinstalar todo o ambiente

```sh
$ pipenv uninstall --all
```

Pois ...

`$ pipenv uninstall` supports all of the parameters in pipenv install, as well as two additional options, --all and --all-dev.

--all — This parameter will purge all files from the virtual environment, but leave the Pipfile untouched.
--all-dev — This parameter will remove all of the development packages from the virtual environment, and remove them from the Pipfile.

##### Onde localizar os pacaotes baixados pelo `pipenv`

Difernete do `venv` os pacaotes baixados ficam num lugar bem distante da pasta onde você instlaou o ambiente virutak `pipenv`.

No linux, costuman ficar em `~/.local/share/virtualenvs/`

Caso nâo aparece use o comando a seugir que mostra o direitorio de onde pega os pacaotes
````sh
$ pipenv --venv
````
/home/rhavel/.local/share/virtualenvs/rating-comments-server-JE1nrH0G

### Dúvidas

````sh
$ pipenv -h
````

````h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
````





## Instalar `pytorch (cpu only - lightweight)` no heroku 

Colocamos

```
https://download.pytorch.org/whl/cpu/torch-1.5.1%2Bcpu-cp37-cp37m-linux_x86_64.whl
```

em `requirements.txt` e mandamos dessa forma até que no build sejam feita a instalação desse pacote.

### OBS

+ O heroku tem 512 MB (free tier), então, instalar a versão completa do `pythoch`  não dá certo
+ Não consegui de maneira alguma instalar pytorch cpu com `pipenv`
