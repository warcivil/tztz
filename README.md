1. создаем venv pythob3 -m venv venv и входим в него.

2. делаем миграции python3 manage.py migrate

3. генерируем данные(займет время) python3 manage.py generate_data

4. запускаем сервер python3 manage.py runserver

Для раскрытия дерева подразделений надо тыкнуть по названию подразделения. 


ps.
Если не хочется долго ждать, то грузим фикстуру python3 manage.py loaddata tl_api/fixtures/data.json


урл: http://127.0.0.1:8000/employees/department_tree/
