from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        #testing new user with email is successful
        email = "test@gmail.com"
        password = "test123@"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,            
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        #if no email is provided, it should raise error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser('test@gmail.com', 'test1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)