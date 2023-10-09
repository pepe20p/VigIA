from django.test import TestCase
from main.views import index
from django.test import Client
# Create your tests here.

class TestesPaginas(TestCase):
    
    def test_view_index (self):
        c =Client()
        response = c.post("/", {"FILES": 'C:/Users/joaop/OneDrive/Documentos/codes/EngenhariaDeSoftware/Projeto/VigIA/media/teste.mp4'})
        self.assertEqual(response.status_code, 200)
    def test_view_sobre (self):
        c = Client()
        response = c.get("/sobre")
        self.assertEqual(response.status_code, 301)
    
    def test_view_contato (self):
        c = Client()
        response = c.get("/contato")
        self.assertEqual(response.status_code, 301)

    def test_view_ajuda (self):
        c = Client()
        response = c.get("/ajuda")
        self.assertEqual(response.status_code, 301)

