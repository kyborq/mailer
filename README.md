# Mass Mailer

A small tool for mass mailing with html templates support written in Python

## How to use

### Installing

1. Clone repository and select directory

```
PS> git clone https://github.com/kyborq/mass-mailer.git
PS> cd mass-mailer
```

2. Install virtual environment and activate it

```
PS> python -m venv venv
PS> venv\Scripts\activate
```

3. Installing packages from requirements.txt

```
PS> pip install -r requirements.txt
```

4. Run

```
(venv) PS> python main.py
```

### Configuring

Create .env file in your project and fill next content

```
SMPT_SERVER=smtp.mail.ru
SMTP_PORT=587
SMTP_USERNAME=abcdefg@mail.ru
SMTP_PASSWORD=123
```
