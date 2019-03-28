#Django Webpack Integration

### Описание

Итак у вас есть проект на django куда прикручен django-rest и еще 100500
модулей с которых вы собирает статику collectstatic на production 
и у вас есть куча компилируемого js для фронтэнеда который на es7 и его
надо собирать. Смысл этого чтоб джанга была отдельно а webpack  и js отдельно: 
но управлять конечно из джанги и небыло проблем со static из приложений django

### Установка
pip install git+https://github.com/saintbyte/django_webpack_integration

### Настройка

1. Добавляем в INSTALLED_APPS ( settings.py ) 'django_webpack_integration'

2. В settings.py добавляем FRONTEND_DIR - где указываем путь до вашего 
 проект на js
 
3. Теперь в массив scripts который в package.json который в свою очередь где-то 
в директории которая прописана в FRONTEND_DIR добавлем "webpack-dev-server":"./node_modules/.bin/webpack-dev-server"
 предварительно установие npm install --save-dev webpack-dev-server

4. В webpack.config.js webpack-dev-server настраиваем примерно так:
4.1 в начале добавлем 
```
const fs = require('fs');
var rawdata = fs.readFileSync('django.json');
var django = JSON.parse(rawdata);
```
не волнуйтесь за django.json - он будет создан автоматическии 
4.2 в основном конфиге webpack добавляем примерно такое:
```
    devServer: {
        contentBase: [path.join(__dirname, 'dist')].concat(django['static_dirs']),
        compress: true,
        clientLogLevel: 'info',
        port: 9000,
        before: function (app, server) {}
    }
```
 
4. settings.py STATIC_URL меняем на 'http://localhost:9000/' ( webpack-dev-server 
   запускается на 9000 по конфигу выше )

5. В директории с проектом django запускаем  ./manage.py npm webpack-dev-server
     
6. Добавить django.json в .gitignore     