import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get('https://ekminuteaap.netlify.app/')

loginBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
loginBtn.click()

loginCredentials = driver.find_elements(By.XPATH, "//div[@class='inline']")

loginWith = []

for credential in loginCredentials:
    full_text = credential.text

    try:
        p_text = credential.find_element(By.TAG_NAME, "p").text

        cleaned_text = full_text.replace(p_text, "").strip()

        loginWith.append(cleaned_text.split()[-1])

    except:
        loginWith.append(full_text.split()[-1])


usernameInput= driver.find_element(By.ID, "username")
usernameInput.send_keys(loginWith[0])

passwordInput= driver.find_element(By.ID, "password")
passwordInput.send_keys(loginWith[1])

submitBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
submitBtn.click()

wait=WebDriverWait(driver,15)

wait.until(expected_conditions.visibility_of_element_located((By.ID, "root")))

videoClick= driver.find_element(By.XPATH, "//body/div/div[2]/div/div[1]")
videoClick.click()
print(videoClick.text)

wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "lucide-heart")))

likeBtn = driver.find_element(By.CLASS_NAME, "lucide-heart")
likeBtn.click()

commentBtn = driver.find_element(By.CLASS_NAME, "lucide-message-circle")
commentBtn.click()

input_comment = driver.find_element(By.XPATH, "//input")
input_comment.send_keys("nice")

postcomment_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Post']")
postcomment_btn.click()



time.sleep(2)
driver.quit()
