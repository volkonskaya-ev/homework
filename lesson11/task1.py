# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://sbis.ru")
    sleep(1)
    tab_contacts = driver.find_element(By.CSS_SELECTOR, "[href = '/contacts']")
    tab_contacts.click()
    sleep(1)

    logo = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    logo.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)

    block_power = driver.find_element(By.CSS_SELECTOR,
                                      '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    block_power.is_displayed()
    sleep(10)
    details = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content \
    tensor_ru-Index__card"] [href="/about"]')
    details.click()
    sleep(3)
    assert driver.current_url == 'https://tensor.ru/about', \
        f'Неверно открыт сайт. Ожидали: https://tensor.ru/about. Получили: {driver.current_url}'

finally:
    driver.quit()
