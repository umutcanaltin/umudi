import os
from airium import Airium
html_generator = Airium()



class App():
    def __init__(self, app_name, platform = "win", test= False):
        self.app_name = app_name
        self.platform = platform
        self.test = test

    def create_blank_template(self):
        return 0

    def init_andro_project():
        return 0
    
    def init_ios_project():
        return 0
    
    def init_mac_project():
        return 0
    
    def init_win_project():
        return 0

    def init_linux_project():
        return 0







def initialize_html():
    html_generator('<!DOCTYPE html>')
    with html_generator.html():
        with html_generator.head():
            html_generator.meta(charset="utf-8")
            html_generator.meta(name="viewport",content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no")
            html_generator.title(_t="umudi blank page")
            html_generator.link(rel="stylesheet", href="css/fontawesome/fontawesome-all.css")
            html_generator.link(rel="stylesheet", href="css/fontawesome/fontawesome-brands.css")
            html_generator.link(rel="stylesheet", href="css/main.css")


    html = str(html_generator)
    print(html)