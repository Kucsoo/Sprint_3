import random as r
class Helpers:
    def email_generation():
        login = 'kate_bogdanova_09'
        login_r = r.randint(100, 999)
        domen = '@mail.com'
        email = login+str(login_r)+domen
        return email


    def password_generation():
        password_r = r.randint(100000, 999999)
        password = str(password_r)
        return password

    def wrong_password_generation():
        password_r =r.randint(1, 99999)
        wrong_password = str(password_r)
        return wrong_password