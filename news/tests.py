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
        h1 = News.objects.get(id=100)
        h2 = News.objects.get(id=101)
        self.assertEqual(h1.heading, "")
        self.assertEqual(h2.heading, "ataae")

    def test_details(self):
        d1 = News.objects.get(id=102)
        d2 = News.objects.get(id=103)
        self.assertEqual(d1.details, "")
        self.assertEqual(d2.details, "hrthbesb")

    def test_count(self):
        count = News.objects.count()
        self.assertEqual(count, 4)

    @unittest.expectedFailure
    def test_unique(self):
        News.objects.create(heading="ataae")
