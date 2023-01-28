import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class MyTestCase(unittest.TestCase):

    valid_username = "testowa0001"
    valid_password = "iDKhVFbjTqNzlsP"
    start = "Schronisko PTTK przy Morskim Oku"
    destination = "Rysy"
    route_name = "Schronisko PTTK przy Morskim Oku – Rysy"

    # Setup & config
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "pl.mapa_turystyczna.app",
            "appActivity": "pl.mapa_turystyczna.app.MapActivity"
        }

        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)


    # Close the Appium client
    def tearDown(self):
      self.driver.quit()

    #TC: ID003
    # 1. Kliknij "Menu"
    # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
    # 3. Kliknij "Zgadzam się na użycie danych osobowych"
    # 4. Kliknij "Zaloguj się"
    # 5. Wpisz nazwę użytkownika
    # 6. Wpisz hasło
    # 7. Kliknij "Zaloguj się"
    # 8. Kliknij "Rozpocznij planowanie trasy"
    # 9. Wyszukaj punkt startowy "Schronisko PTTK przy Morskim Oku"
    # 10. Kliknij lokalizator miejsca
    # 11. Kliknij niebieską ikonkę człowieka w prawym dolnym rogu.
    # 12.Kliknij "Dodaj kolejny punkt" i wyszukaj "Rysy"
    # 13. Kliknij "Szczegóły"
    # 14. Kliknij pomarańczową ikonkę z dyskietką by zapisać trasę
    # 15. Kliknij przycisk "Wróć", przejdź do "Menu" i przejdź do "Zaplanowane trasy"
    # 16.Sprawdź czy na liście znajduje się trasa "Schronisko PTTK przy Morskim Oku – Rysy"


    def test003_ZapisywaniePlanowanejTrasyNaKoncieUzytkownika(self):
        # 1. Kliknij "Menu"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Otwórz nawigację").click()

        # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
        self.driver.find_element(AppiumBy.ID, "android:id/button2").click()

        # 3. Kliknij "Zgadzam się na użycie danych osobowych"
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View[2]/android.view.View/android.widget.Button[1]").click()

        # 4. Kliknij "Zaloguj się"
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]/android.widget.CheckedTextView").click()

        # 5. Wpisz nazwę użytkownika
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/email_input").send_keys(self.valid_username)

        # 6. Wpisz hasło
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/password_input").send_keys(self.valid_password)

        # 7. Kliknij "Zaloguj się"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/login_button").click()

        # 8. Kliknij "Rozpocznij planowanie trasy"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/title_view").click()

        # 9. Wyszukaj punkt startowy "Schronisko PTTK przy Morskim Oku"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/search_src_text").send_keys(self.start)
        self.driver.press_keycode(66)
        time.sleep(5)

        # 10. Kliknij lokalizator miejsca
        TouchAction(self.driver).tap(None, 700, 1200, 1).release().perform()

        # 11. Kliknij niebieską ikonkę człowieka w prawym dolnym rogu.
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/node_route_button").click()

        # 12.Kliknij "Dodaj kolejny punkt" i wyszukaj "Rysy"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/autocomplete_wrapper").click()
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/search_src_text").send_keys(self.destination)
        self.driver.press_keycode(66)
        time.sleep(5)

        # 13. Kliknij "Szczegóły"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/route_show_details_button").click()

        # 14. Kliknij pomarańczową ikonkę z dyskietką by zapisać trasę
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/route_save_button").click()
        TouchAction(self.driver).long_press(None, 722, 108).move_to(None, 722, 2130).release().perform()

        # 15. Kliknij przycisk "Wróć", przejdź do "Menu" i przejdź do "Zaplanowane trasy"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Zwiń").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Otwórz nawigację").click()
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.CheckedTextView").click()

        # 16.Sprawdź czy na liście znajduje się trasa "Schronisko PTTK przy Morskim Oku – Rysy"
        saved_route = self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/route_item_name")
        self.assertTrue(saved_route.text in self.route_name)