from sys import platform
import glob, time, os, subprocess

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.options import Options
except (ImportError, ModuleNotFoundError):
    print("Selenium not found. Installing...")
    try:
        subprocess.run(["pip", "install", "selenium"], check=True)
        print("Selenium installed successfully. Please run the script again.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Selenium: {e}")
        exit(1)

# Define the driver globally
driver = None

def main():
    global driver
    if platform == 'win32':
        base_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")

        pattern = os.path.join(base_path, "*default-release*")
        matching_folders = glob.glob(pattern)

        folder_paths = []

        for folder in matching_folders:
            folder_paths.append(folder)

        path = folder_paths[-1]

        # print(path)
        options = Options()
        options.add_argument(f"-profile {path}")
        # options.add_argument(path)

    elif platform == 'linux' or platform == 'linux2':
        base_path = os.path.expanduser(r"~/.mozilla/firefox")  # /home/xnuvers007/.mozilla/firefox

        pattern = os.path.join(base_path, "*default-esr*")
        matching_folders = glob.glob(pattern)

        folder_paths = []

        for folder in matching_folders:
            folder_paths.append(folder)

        path = folder_paths[-1]

        # print(path)
        options = Options()
        options.add_argument(f"-profile {path}")
        # options.add_argument(path)

    else:
        print("OS not supported.")
        exit(1)

    link_meet = input("Masukkan link meet: ")

    driver = webdriver.Firefox(options=options)

    driver.get(link_meet)  # Load the page once

    try:
        mic = input("matikan mic ? ")
        cam = input("matikan cam ? ")
        if mic.lower() == "y":
            mic_button = '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[1]'
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mic_button))).click()
        if cam.lower() == "y":
            cam_button = '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[2]'
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cam_button))).click()
    except:
        pass

    gabung_button = '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, gabung_button))).click()

    while True:
        try:
            view_button = '/html/body/div[1]/c-wiz/div[1]/div/div[14]/div[3]/div[21]/div/div/div[1]/div[2]/div/button'
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, view_button))).click()
            accept_button = '/html/body/div[1]/c-wiz/div[1]/div/div[14]/div[3]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/span/div[1]/div[2]'
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, accept_button))).click()
            admit_all = '/html/body/div[1]/div[4]/div[2]/div/div[2]/button[2]'
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, admit_all))).click()
        except:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Script interrupted by user.")
        print("")
        for i in range(3, 0, -1):
            print(f"Exiting in {i} seconds...", end="\r")
            time.sleep(1)
    finally:
        if driver:
            driver.quit()
