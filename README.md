# TetsLib
оформление собственных библиотек на python'е
1. создать директорию, где намерены хранить библиотеку
2. создать файл setup.py
3. добавить в проект папку, где будет храниться библиотека (mylibrary)
4. в этой папке добавить файл __init__.py
5. здесь же создать файл, в котором будем хранить функции (myfunctions.py)
6. в нём напишем простую функцию сложения двух чисел. писать функции нужно с полной нотацией: указывать тип параметров и тип, который функция возвращает (add)
7. очень желательно писать док-стринги
8. после того, как функция написана, необходимо написать тесты к ней
9. создаём в проекте папку для размещения тестов (tests)
10. в ней создаём __init__.py 
11. ещё создаём файл с именем, совпадающим с тем, который мы собираемся тестировать, но в начале дописать test (test_myfunctions.py)
12. приступаем к написанию тестирующей функции, но сначала импортируем тестируемую (from mylibrary.myfunctions import add)
13. затем создаём функцию test_addd() без параметров, в которой мы сравниваем результат выполнения тестируемой функции с заранее известным результатом
14. тесты пишутся для того, чтоб быть уверенным, что ничего не поломали при добавлении в функцию нового функционала
15. возвращаемся к setup.py и добавляем в него специальный код (в проекте)
16. далее необходимо установить эту библиотеку. это делается просто - переходим в терминал и пишем pip3 install -e .
17. после установки в проекте появятся новые папки и файлы
18. библиотека готова. теперь протестируем её
19. переместимся в папку, где точно наша библиотека отсутствует
20. вызовем интерпретатор питона (python.exe)
21. напишем следующее:
import mylibrary
from mylibrary.myfunctions import add
add(1, 5)
22. получим ответ 6
23. exit()
24. если библиотека больше не нужна - как избавиться от неё
25. в терминале пишем pip uninstall mylibrary - имя должно совпадать с тем, которое указано в файле setup.py в параметре name
26. всё, библиотека удалена
    
