import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

class MyTestCase(unittest.TestCase):

    valid_username = "testowyuzytkownik001"
    valid_email = "vo658@gmail.com"
    valid_password = "iDKhVFbjTqNzlsP"

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
        self.driver.implicitly_wait(2)


    # Close the Appium client
    def tearDown(self):
        self.driver.quit()

    #TC:ID001
    # 1. Kliknij "Menu"
    # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
    # 3. Kliknij "Zgadzam się na użycie danych osobowych"
    # 4. Kliknij "Załóż konto"
    # 5. Wpisz nazwę użytkownika
    # 6. Wpisz e-mail
    # 7. Wpisz hasło
    # 8. Zaznacz checkbox "Wyrażam zgodzę na przetwarzanie danych osobowych"
    # 9. Kliknij "Załóż konto"
    # 10. Otwórz Menu i sprawdź czy wyświetla się nazwa użytkownika

    def test001_ZakladanieKontaUzytkownikaPoprawnyEmail(self):
        # 1. Kliknij "Menu"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Otwórz nawigację").click()

        # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
        self.driver.find_element(AppiumBy.ID, "android:id/button2").click()
        time.sleep(5)

        # 3. Kliknij "Zgadzam się na użycie danych osobowych"
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View[2]/android.view.View/android.widget.Button[1]").click()

        # 4. Kliknij "Załóż konto"
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[8]/android.widget.CheckedTextView").click()

        # 5. Wpisz nazwę użytkownika
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/register_username_input").send_keys(self.valid_username)

        # 6. Wpisz e-mail
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/register_email_input").send_keys(self.valid_email)

        # 7. Wpisz hasło
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/register_password_input").send_keys(self.valid_password)

        # 8. Zaznacz checkbox "Wyrażam zgodzę na przetwarzanie danych osobowych"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/privacy_consent_checkbox").click()

        # 9. Kliknij "Załóż konto"
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/register_button").click()
        time.sleep(5)

        #10. Otwórz Menu i sprawdź czy wyświetla się nazwa użytkownika
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Otwórz nawigację").click()
        label_username = self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/username_view")
        self.assertTrue(label_username.text in self.valid_username)
