import unittest
from django.test import TestCase
from news.models import News


class NewsModelTest(TestCase):

    def setUp(self):
        News.objects.create(id="100", heading="")
        News.objects.create(id="101", heading="ataae")
        News.objects.create(id="102", heading="assww", details="")
        News.objects.create(id="103", heading="tccc", details="hrthbesb")

    def test_heading(self):
        self.assertEqual(
            News.objects.get(id=100).heading,
            ""
        )
        self.assertEqual(
            News.objects.get(id=101).heading,
            "ataae"
        )

    def test_details(self):
        self.assertEqual(
            News.objects.get(id=102).details,
            ""
        )
        self.assertEqual(
            News.objects.get(id=103).details,
            "hrthbesb"
        )

    def test_count(self):
        self.assertEqual(
            News.objects.count(),
            4
        )

    @unittest.expectedFailure
    def test_unique(self):
        News.objects.create(heading="ataae")
