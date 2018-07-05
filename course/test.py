from django.test import TestCase
from course.models import Teacher, Course, List, Summary, Link, Post, Comment


class CourseTestCase(TestCase):
    def setUp(self):
        Teacher.objects.bulk_create([
            Teacher(name="Simone"),
            Teacher(name="Agma"),
            Teacher(name="Elaine"),
            Teacher(name="Kalinka"),
            Teacher(name="Jó"),
            Teacher(name="Pablo"),
            Teacher(name="Tomé"),
            Teacher(name="Mello"),
            Teacher(name="Batista"),
            Teacher(name="Simões"),
            Teacher(name="Hermano"),
            Teacher(name="Monari"),
            Teacher(name="Zani"),
        ])

        Course.objects.bulk_create([
            Course(
                name="Engenharia de Software",
                code="SSC-130",
                teachers=["Simone"]
            ),
            Course(
                name="Computação Gráfica",
                code="SCC-250",
                teachers=["Agma"]
            ),
            Course(
                name="Base de Dados",
                code="SCC-240",
                teachers=["Elaine"]
            ),
            Course(
                name="Redes de Computadores",
                code="SSC-142",
                teachers=["Kalinka", "Jó"]
            ),
            Course(
                name="Processos Estocásticos",
                code="SME-121",
                teachers=["Pablo"]
            ),
            Course(
                name="Cálculo Numérico",
                code="SME-104",
                teachers=["Tomé"]
            ),
            Course(
                name="Introdução à Ciênciada da Computação I",
                code="SCC-221",
                teachers=["Mello", "Batista", "Simões"]
            ),
            Course(
                name="Introdução à Ciênciada da Computação II",
                code="SCC-201",
                teachers=["Mello", "Batista", "Simões"]
            ),
            Course(
                name="Algoritmos Evolutivos",
                code="SCC-221",
                teachers=["Simões"]
            ),
        ])

    # def test_tite_exists(self):
    #     """Animals that can speak are correctly identified"""
    #     # lion = Animal.objects.get(name="lion")
    #     # cat = Animal.objects.get(name="cat")
    #     # self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     # self.assertEqual(cat.speak(), 'The cat says "meow"')
