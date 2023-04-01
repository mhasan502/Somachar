import unittest
from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username="abaa", password="hello", is_staff=True)
        User.objects.create(username="rrrr", password="hello", is_superuser=True)

    def test_username(self):
        self.assertEqual(
            User.objects.get(username="abaa").username,
            "abaa"
        )

    def test_superuser(self):
        self.assertEqual(
            User.objects.get(username="abaa").is_superuser,
            False
        )
        self.assertEqual(
            User.objects.get(username="rrrr").is_superuser,
            True
        )

    def test_staff(self):
        self.assertEqual(
            User.objects.get(username="abaa").is_staff,
            True
        )
        self.assertEqual(
            User.objects.get(username="rrrr").is_staff,
            False
        )

    @unittest.expectedFailure
    def test_without_password(self):
        User.objects.create(username="abaa")
