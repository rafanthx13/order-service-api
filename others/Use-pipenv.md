#### Instalar 
#  `pipenv`

## Install

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



