from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        """Confirm a new user can be created."""
        User = get_user_model()
        user = User.objects.create_user(
            username='jaya',
            email='jaya@email.com',
            password='testing123'
        )
        self.assertEqual(user.username, 'jaya')
        self.assertEqual(user.email, 'jaya@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        """Confirm a superuser can be created.
        Superusers should have both `is_staff` and
        `is_superuser` set to `True`."""
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testing456'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
