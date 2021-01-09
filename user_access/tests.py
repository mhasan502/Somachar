import unittest
from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username="abaa", password="hello", is_staff=True)
        User.objects.create(username="rrrr", password="hello", is_superuser=True)

    def test_username(self):
        u1 = User.objects.get(username="abaa")
        self.assertEqual(u1.username,"abaa")

    def test_superuser(self):
        u1 = User.objects.get(username="abaa")
        u2 = User.objects.get(username="rrrr")
        self.assertEqual(u1.is_superuser, False)
        self.assertEqual(u2.is_superuser, True)

    def test_staff(self):
        u1 = User.objects.get(username="abaa")
        u2 = User.objects.get(username="rrrr")
        self.assertEqual(u1.is_staff, True)
        self.assertEqual(u2.is_staff, False)

    @unittest.expectedFailure
    def test_without_password(self):
        u = User.objects.create(username="abaa")