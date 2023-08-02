![GNU License](https://img.shields.io/github/license/xnuvers007/google-meet-auto?style=plastic&logo=GNU&logoColor=red&color=blue)
![GitHub repo size](https://img.shields.io/github/repo-size/xnuvers007/google-meet-auto?style=plastic&logo=github&logoColor=blue&label=Size%20Repo&color=blue)
![GitHub release (with filter)](https://img.shields.io/github/v/release/xnuvers007/google-meet-auto?color=red)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/xnuvers007/google-meet-auto)

# google-meet-auto

requirements:
  - python 3.10+ [download python here](https://python.org/downloads)
  - selenium ```after download python just type pip install selenium if you forget, the script will automatically```
  - firefox [download firefox here](https://www.mozilla.org/id/firefox/new/)

This repo can you use for auto accept join with only firefox

i dont use
```
from selenium.webdriver.firefox.webdriver import FirefoxProfile

profile = FirefoxProfile("C:\\Path\\to\\profile")
```
because is deprecated source = https://stackoverflow.com/questions/64614622/how-to-setup-firefox-profile-in-selenium-correctly

and i don't use this too because is deprecated too

```from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument("-profile")
options.add_argument("/home/gabriel/.mozilla/firefox/whatever.selenium")
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_options=options)
```
source link code = https://stackoverflow.com/questions/50321278/how-to-load-firefox-profile-with-python-selenium

so i decided to use profile from storage
