from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('will', 'will@example.com', 'Abc123$%')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, 'will@example.com')

    def test_raises_error_when_no_username_is_supplied_when_creating_user(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='will@example.com', password='Abc123$%')

    def test_raises_error_with_message_when_no_username_is_supplied_when_creating_user(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='will@example.com', password='Abc123$%')

    def test_raises_error_when_no_email_is_supplied_when_creating_user(self):
        self.assertRaises(ValueError, User.objects.create_user, username='will', email='', password='Abc123$%')

    def test_raises_error_with_message_when_no_email_is_supplied_when_creating_user(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='will', email='', password='Abc123$%')

    def test_creates_super_user(self):
        user=User.objects.create_superuser('will', 'will@example.com', 'Abc123$%')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'will@example.com')

    def test_raises_error_when_no_username_is_supplied_when_creating_superuser(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='will@example.com', password='Abc123$%')

    def test_raises_error_with_message_when_no_username_is_supplied_when_creating_superuser(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='will@example.com', password='Abc123$%')

    def test_raises_error_when_no_email_is_supplied_when_creating_superuser(self):
        self.assertRaises(ValueError, User.objects.create_user, username='will', email='', password='Abc123$%')

    def test_raises_error_with_message_when_no_email_is_supplied_when_creating_superuser(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='will', email='', password='Abc123$%')

    def test_raises_error_when_superuser_parameter_is_staff_is_not_true(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='', email='will@example.com', password='Abc123$%', is_staff=False)

    def test_raises_error_with_message_when_parameter_is_staff_is_not_true_when_creating_superuser(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='will', email='will@example.com', password='Abc123$%', is_staff=False)

    def test_raises_error_when_superuser_parameter_is_superuser_is_not_true(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='will', email='', password='Abc123$%', is_superuser=False)

    def test_raises_error_with_message_when_parameter_is_superuser_is_not_true_when_creating_superuser(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='will', email='will@example.com', password='Abc123$%', is_superuser=False)