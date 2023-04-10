from django.test import TestCase

from ..models import Category


class CategoryTest(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="phylosphi")

    def test_category(self):
        p=Category.objects.get(name="phylosphi")
        self.assertEqual(p.name,"phylosphi")


