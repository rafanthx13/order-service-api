## acessar heroku

heroku login

isntlar `pip install gunicorn` para rodar no heroku

```
heroku apps:create service-order-api
```

O arquivo 'runtime.txt', deve ter o python mais rescente informadao nesse site

https://devcenter.heroku.com/articles/python-support

Uma vez deixe 3.7.7, e ja nao aceitava mais entao, tive que mudar par ao .12

Se nao conseguri faze ro deploy por CLI, pode tentar por git manulamente ou  rodar o deply automaticamente quando fazer push, é só configurara.

https://service-order-api.herokuapp.com/predict

## Fazer deploy

da push; vai no heroku, faça push manual do git lá, ou habilita fazer push automatico