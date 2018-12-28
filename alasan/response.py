class Response:
    def __init__(self):
        self.data_dict = {
            "version": "1.0",
            "response": {
                "shouldEndSession": False,
                "directives": []
            }
        }

    def session_attributes(self, session_attributes):
        self.data_dict["sessionAttributes"] = session_attributes
        return self

    def speak(self, text, ssml=False):
        if not ssml:
            self.data_dict["response"]["outputSpeech"] = {
                "type": "PlainText",
                "text": text
            }
        else:
            self.data_dict["response"]["outputSpeech"] = {
                "type": "SSML",
                "ssml": text
            }
        return self

    def card(self, card_dict):
        self.data_dict["response"]["card"] = card_dict
        return self

    def reprompt(self, text, ssml=False):
        if not ssml:
            self.data_dict["response"]["reprompt"] = {
                "type": "PlainText",
                "text": text
            }
        else:
            self.data_dict["response"]["reprompt"] = {
                "type": "SSML",
                "ssml": text
            }
        return self

    def add_directive(self, directive_dict):
        self.data_dict["directives"].append(directive_dict)
        return self

    def end_session(self):
        self.data_dict["response"]["shouldEndSession"] = True
        return self
