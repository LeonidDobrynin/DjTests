import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def create_student():
    return Student.objects.create(name="admin", birth_date=None)


@pytest.fixture
def client():
    return APIClient()



# #Проверка создания курса
# @pytest.mark.django_db
# def test_courses(client,create_student,course_factory):
#     course_create = course_factory(_quantity=1)
#
#     response = client.get('/courses/')
#
#     assert response.status_code == 200
#     data = response.json()
#     for i, c in enumerate(data):
#         assert c['name'] == course_create[i].name



# #Проверка списка курсов
# @pytest.mark.django_db
# def test_list_courses(client,create_student,course_factory):
#     course_create = course_factory(_quantity=5)
#
#     response = client.get('/courses/')
#
#     assert response.status_code == 200
#     data = response.json()
#     for i, c in enumerate(data):
#         assert c['name'] == course_create[i].name



# #Проверка курса по id
# @pytest.mark.django_db
# def test_list_courses(client,create_student,course_factory):
#     course_create = course_factory(_quantity=5)
#
#     response = client.get('/courses/?id=1')
#
#     assert response.status_code == 200
#     data = response.json()
#     for i, c in enumerate(data):
#         assert c['name'] == course_create[i].name

# #Проверка курса по name
# @pytest.mark.django_db
# def test_list_courses(client,create_student,course_factory):
#     course_create = course_factory(_quantity=5)
#     req = '/courses/?name='
#     name_course = course_create[0].name
#     response = client.get(req+name_course)
#
#     assert response.status_code == 200
#     data = response.json()
#     for i, c in enumerate(data):
#         assert c['name'] == course_create[i].name

# #Проверка курса по id
# @pytest.mark.django_db
# def test_list_courses(client):
#
#     response = client.post('/courses/', data={'name':'Course_name', 'student':1}  )
#
#     assert response.status_code == 201

# #Проверка курса по id
# @pytest.mark.django_db
# def test_list_courses(client,create_student,course_factory):
#
#
#     course_create = course_factory(_quantity=5)
#
#
#     response = client.patch('/courses/1/', data={'name':'NEW_TEXT',}  )
#
#     assert response.status_code == 200

#Проверка курса по id
@pytest.mark.django_db
def test_list_courses(client,create_student,course_factory):


    course_create = course_factory(_quantity=5)


    response = client.delete('/courses/1/' )

    assert response.status_code == 204

