from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Configurações para o Chrome
    chrome_options = Options()
    chrome_options.headless = True  # Executar em modo headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Caminho para o ChromeDriver
    chrome_driver_path = "C:\\WebDriver\\chromedriver.exe"
    
    # Iniciar o WebDriver usando ChromeDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(10)
    
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)
