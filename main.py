from config import Config
from sender import Sender
from template import Template
from utils import read_csv

invite_info = {
    "title": "🎂 День рождения 🥳",
    "description": "Приглашаю тебя на свой день рождения. Буду рад тебя видеть!",
    "greetings": "Привет, ",
    "phone_number": "+7(800)555-35-35",
    "address": "Улица Пушкина, дом Колотушкина"
}

context = read_csv("./data/invite_data.csv")

template = Template("./templates/")
template.load_template("invite_template.html")

sender = Sender(Config.SMPT_SERVER, Config.SMTP_PORT,
                Config.SMTP_USERNAME, Config.SMTP_PASSWORD)

for line in context:
    line.update(invite_info)

    template.set_context(line)
    html_content = template.render_to_html()

    sender.send_message(line['email'],
                        invite_info['title'], html_content)
