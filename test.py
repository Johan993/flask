from pprint import pprint
from requests import get, post, delete

pprint(delete(f'http://127.0.0.1:8080/api/jobs/1').json())
# нет такого ID
pprint(delete('http://127.0.0.1:8080/api/jobs/999').json())
# неверный формат
pprint(delete('http://127.0.0.1:8080/api/jobs/пока').json())
# удаление уже удаленного
pprint(delete(f'http://127.0.0.1:8080/api/jobs/1').json())

pprint(get('http://127.0.0.1:8080/api/jobs').json())