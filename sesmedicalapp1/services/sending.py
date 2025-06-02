import time

import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

yag = yagmail.SMTP(os.getenv("EMAIL"), os.getenv("PASSWORD"))

contents = "Divine is a chicken Bumbum with small small things"
subject = "Your Description"

while True:
    yag.send('divineobinali9@gmail.com', subject, contents)
    time.sleep(120)

