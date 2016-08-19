from django.test import TestCase, Client
from .models import User

# Create your tests here.


class TestAuthen(TestCase):

    def test_home_page(self):
        client = Client()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_can_login(self):
        email = 'sanyam@sanyamkhurana.com'
        username = 'sanyam'
        password = 'password'
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()

        # Assert no. of users in the db
        users_in_db = User.objects.count()
        self.assertEqual(users_in_db, 1)

        # Assert some important properties of user
        self.assertEqual(user.is_admin, False, "User is an admin")
        self.assertEqual(user.is_active, True, "User is not active")

        # Finally test if user can login to the site
        client = Client()
        response = client.post('/login/', {'username': username, 'password':
                                           password})

        self.assertEqual(response.status_code, 200)

        response = client.post('/login/', {'username': 'test', 'password':
                                           password})

        self.assertEqual(response.status_code, 401)
