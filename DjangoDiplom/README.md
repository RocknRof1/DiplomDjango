﻿## Проект Django Diplom
Веб приложение предназначенное для управления постами о выпечках. 

## Содержание
Оно предлагает интуитивно понятный интерфейс для создания, редактирования, удаления и обновления записей используя архитектуру MVT(Model-View-Templates)
Модели обрабатывают данные, представления управляют логикой, а шаблоны отражают информацию пользователя
Django Form для обработки форм и добавления записей в базу данных
Пользовательские функции регистрации и входа в систему
## Архитектура проекта
![image](https://github.com/user-attachments/assets/f4dd6919-25a7-4e7a-b7b0-409aa8587a77)


## Использование
Django может быть (и был) использован для создания практически любого типа веб-сайтов — от систем управления контентом и wiki до социальных сетей и новостных сайтов. Он может работать с любой клиентской средой и может доставлять контент практически в любом формате (включая HTML, RSS-каналы, JSON, XML и т. д.). Сайт, который вы сейчас читаете, создан с помощью Django!

## Разработка
Установите django  с помощью команды:
```
pip install django 
```
Создаем проект 
```
django-admin startproject diplom
```
Переходим в директиву проекта
```
cd diplom
```
Запуск сервера осуществляется по команде:
```
 python manage.py startapp app
```
Для обработка изображений нужно скачать библиотеку Pillow
```
python -m pip install Pillow 
```
Создаем admina для управления веб приложением :
```
python manage.py createsuperuser  
```

##Для миграции таблиц базы данных пишем команы:
```
python manage.py migrate  
```
```
python manage.py makemigrations  
```

## URL использованные в проекте
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
```

## Зачем вы разработали этот проект?
Для защиты дипломной работы

## Команда проекта
Андрей Румянцев
## Источники
Изучения курса Urban University

## Выводы создания приложения на Django
1. Хорошая документация: Документация по Django написана понятно и подробно, что помогает новичкам обучаться и развивать свои навыки, а опытным разработчикам — проще находить нужную информацию. В целом, создание приложения на Django оказалось удачным решением. Фреймворк предлагает много возможностей для разработки современных и надежных веб-приложений, что делает его отличным выбором для будущих проектов.
2. Быстрая разработка: С Django можно быстро создавать приложения, потому что он уже включает много готовых инструментов и функций, например для работы с базами данных и аутентификацией пользователей. 
3. Гибкость: Приложения на Django могут работать как на локальных серверах, так и в облаке, что делает их универсальными и подходящими для разных ситуаций.
4. Поддержка сообщества: У Django есть большое и активное сообщество, которое делится полезными материалами, такими как руководства и примеры. Это упрощает решение проблем и обучение. 
5. Высокий уровень безопасности: Django предлагает множество встроенных средств для защиты приложения от распространенных угроз, таких как взлом или утечка данных. Это позволяет разработчикам меньше беспокоиться о безопасности. 
6. Простота архитектуры: Django помогает организовать структуру приложения так, чтобы было удобно работать. Благодаря этому разработчики могут фокусироваться на логике приложения, не заботясь о том, как реализовать базовые вещи. 
7. Легкость в масштабировании: Если ваше приложение станет популярным и нагрузка на него возрастет, Django позволяет легко добавить новые функции и расширить его, чтобы справиться с большим количеством пользователей.
8. Удобные инструменты для тестирования: Django предоставляет функции для тестирования и отладки приложения, что позволяет находить ошибки и улучшать качество проекта. 

