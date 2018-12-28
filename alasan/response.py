from . import SIMPLE, STANDARD, LINK_ACCOUNT, ASK_FOR_PERMISSIONS_CONSENT


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

    def card(self, type_, title=None, content=None, text=None, image=None):
        self.data_dict["response"]["card"] = {}

        if type_ not in [SIMPLE, STANDARD, LINK_ACCOUNT, ASK_FOR_PERMISSIONS_CONSENT]:
            raise ValueError(
                "Card type has to be one of the following: SIMPLE, STANDARD, LINK_ACCOUNT, ASK_FOR_PERMISSIONS_CONSENT")

        self.data_dict["response"]["card"]["type"] = type_

        if title:
            self.data_dict["response"]["card"]["title"] = title
        if content:
            self.data_dict["response"]["card"]["content"] = content
        if text:
            self.data_dict["response"]["card"]["text"] = text
        if image:
            self.data_dict["response"]["card"]["image"] = {
                "smallImageUrl": image["small"],
                "largeImageUrl": image["large"]
            }

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
