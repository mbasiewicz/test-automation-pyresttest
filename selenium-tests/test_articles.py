import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8080"

def test_view_articles(selenium):
    """Test wyświetlania listy artykułów"""
    selenium.get(f"{BASE_URL}/articles/")
    assert "Article List" in selenium.page_source

def test_form_exists(selenium):
    """Test czy formularz POST istnieje"""
    selenium.get(f"{BASE_URL}/articles/")
    
    title_input = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.NAME, "title"))
    )
    content_input = selenium.find_element(By.NAME, "content")
    post_button = selenium.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    
    assert title_input is not None
    assert content_input is not None
    assert post_button is not None

def test_api_browseable(selenium):
    """Test czy API jest dostępne przez przeglądarkę"""
    selenium.get(f"{BASE_URL}/articles/")
    assert "Django REST framework" in selenium.page_source or "GET" in selenium.page_source