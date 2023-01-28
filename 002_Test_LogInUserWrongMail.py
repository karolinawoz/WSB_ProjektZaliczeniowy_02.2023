import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class MyTestCase(unittest.TestCase):
    invalid_email = "votig668ezgiant.com"
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

    # TC:ID002
    # 1. Kliknij "Menu"
    # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
    # 3. Kliknij "Zaloguj sie"
    # 4. Wpisz błędny adres e-mail
    # 5. Wpisz hasło
    # 6. Kliknij "Zaloguj się”
    # 7. Sprawdzenie czy nadal wyświetla się przycisk zaloguj się

    def test002_LogowanieIstniejacegoKontaUzytkownikaBlednyFormatMaila(self):
        # 1. Kliknij "Menu"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Otwórz nawigację").click()

        # 2. Kliknij "Wyraź zgodę na przetwarzanie danych osobowych"
        self.driver.find_element(AppiumBy.ID, "android:id/button2").click()

        # 3. Kliknij "Zaloguj sie"
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]/android.widget.CheckedTextView").click()

        # 4. Wpisz błędny adres e-mail
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/email_input").send_keys(self.invalid_email)

        # 5. Wpisz hasło
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/password_input").send_keys(
            self.valid_password)

        # 6. Kliknij "Zaloguj się”
        self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/login_button").click()

        # 7. Sprawdzenie czy nadal wyświetla się przycisk zaloguj się
        btn_afterlogin = self.driver.find_element(AppiumBy.ID, "pl.mapa_turystyczna.app:id/login_button")
        self.assertTrue(btn_afterlogin.is_displayed())
