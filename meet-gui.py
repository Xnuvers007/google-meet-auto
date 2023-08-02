import os
import time, glob
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def install_selenium():
    try:
        subprocess.run(["pip", "install", "selenium"], check=True)
        print("Selenium installed successfully. Please run the script again.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Selenium: {e}")
        exit(1)

def get_firefox_profile():
    if os.name == "nt":
        base_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
        pattern = os.path.join(base_path, "*default-release*")
    else:
        base_path = os.path.expanduser(r"~/.mozilla/firefox")
        pattern = os.path.join(base_path, "*default-esr*")

    matching_folders = glob.glob(pattern)
    return max(matching_folders, key=os.path.getctime) if matching_folders else None

def prompt_yes_no(question):
    return messagebox.askyesno("Confirmation", question)

def start_meet():
    profile_path = get_firefox_profile()
    if not profile_path:
        messagebox.showerror("Error", "Firefox profile not found.")
        return

    options = Options()
    options.add_argument(f"-profile {profile_path}")

    link_meet = link_entry.get()

    driver = webdriver.Firefox(options=options)
    driver.get(link_meet)

    try:
        if prompt_yes_no("Matikan mic?"):
            mic_button = '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[1]'
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, mic_button))).click()
        if prompt_yes_no("Matikan cam?"):
            cam_button = '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[2]'
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cam_button))).click()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

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
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    driver.quit()

root = tk.Tk()
root.title("Google Meet Automation")
try:
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
except:
    pass
root.geometry("400x150")

label = tk.Label(root, text="Enter Google Meet Link:")
label.pack(pady=10)

link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_meet)
start_button.pack(pady=10)

root.mainloop()
