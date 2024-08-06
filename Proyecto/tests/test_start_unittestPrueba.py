import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):
    def setUp(self):
        # Inicializa el controlador de Edge
        self.driver = webdriver.Edge()  # Asegúrate de que msedgedriver.exe está en tu PATH
        self.driver.get("https://github.com/BryanPillajo/unnitest")

    def testId(self):
        elemento = self.driver.find_element(By.ID, "NoImportante")

    def testIdName(self):
        # Encuentra el elemento por ID
        elemento = self.driver.find_element(By.ID, "NoImportante")
        self.assertIsNotNone(elemento, "El elemento con ID 'NoImportante' no se encontró.")

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
