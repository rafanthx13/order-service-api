# API do Order Service

**Objetivo:** Prover API REST para disponibilizar sistema preditivo de ordem de serviço. Contem também 200 cliente anonimados da base



## Como fazer deploy



### Instalar Python Env

```
$ sudo apt install python3-venv
$ python3 -m venv venv # cria pasta chamada venv
$ source venv/bin/activate
(venv) $ pip install flask
(venv) $ pip install flask_cors
(venv) $ pip install pandas
(venv) $ pip install scikit-learn
(venv) $ export FLASK_APP=main.py
(venv) $ flask run
(venv) $ deactivate
$ exit
```

### Gerar dependências: pip freeze e requirements

Vai gerar os arquivos com as nossa dependências atuais

```bash
# Salvar libs de python-env
pip freeze > requirements.txt
```

Instalar do `requirements.txt`

```bash
# Instalar dependencias que estão em requirements.txt
pip install -r requirements.txt
```



