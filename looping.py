'''
for
while
nested loop

'''
# for i in range(1,7,2):
#     print(i)

# a=[4,5,6,34,55,2]
# for i in a:
#     print(i)

# a='python'
# for i in a:
#     print(i)
#contiune print hi n number of lines
# while True:
#     print("Hi")

# raja=4
# while raja<9:
#     print("Hi",raja)
#     raja+=1

# for i in range(0,5):
#     for j in range(0,8):
#         print (i+j)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver executable (replace with your actual path)
DRIVER_PATH = '/path/to/chromedriver'

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Navigate to the login page (replace with the actual URL)
driver.get('YOUR_LOGIN_PAGE_URL')

try:
    # Find the email input field and enter the email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))  # Replace 'email' with the actual ID
    )
    email_field.send_keys('abcraja@yopmail.com')

    # Find the password input field and enter the password
    password_field = driver.find_element(By.ID, 'password')  # Replace 'password' with the actual ID
    password_field.send_keys('Qwert@123')

    # Find the SIGN IN button and click it
    sign_in_button = driver.find_element(By.XPATH, "//button[text()='SIGN IN']") # Replace with the actual XPath or ID
    sign_in_button.click()

    # Wait for the next page to load (adjust the wait time as needed)
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )

    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Keep the browser open for a while to observe the result (optional)
    time.sleep(5)
    driver.quit()