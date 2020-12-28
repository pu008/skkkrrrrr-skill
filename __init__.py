from mycroft import MycroftSkill, intent_file_handler


class Skkkrrrrr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skkkrrrrr.intent')
    def handle_skkkrrrrr(self, message):
        self.speak_dialog('skkkrrrrr')


def create_skill():
    return Skkkrrrrr()

