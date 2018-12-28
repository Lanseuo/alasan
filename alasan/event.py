class Event:
    def __init__(self, event_dict):
        self.version = float(event_dict["version"])
        self.session = Session(event_dict["session"])
        self.context = Context(event_dict["context"])
        self.request = Request(event_dict["request"])

    def __repr__(self):
        if self.request.type == "LaunchRequest":
            return f"<Event 'LaunchRequest'>"
        elif self.request.type == "IntentRequest":
            return f"<Event '{self.request.intent.name}'>"


class Session:
    def __init__(self, session_dict):
        self.new = session_dict["new"]
        self.session_id = session_dict["sessionId"]
        self.application = EventProperty()
        self.application.application_id = session_dict["application"]["applicationId"]
        self.user = EventProperty()
        self.user.id = session_dict["user"]["userId"]


class Context:
    def __init__(self, context_dict):
        self.audio_player = "..."
        self.system = EventProperty()
        self.system.application = EventProperty()
        self.system.application.application_id = context_dict["System"]["application"]["applicationId"]
        self.system.user = EventProperty()
        self.system.user.user_id = context_dict["System"]["user"]["userId"]
        self.device = EventProperty()
        self.device.supported_interfaces = [
            interface
            for interface
            in context_dict["System"]["device"]["supportedInterfaces"].keys()
        ]


class Request:
    def __init__(self, request_dict):
        self.type = request_dict["type"]
        self.request_id = request_dict["requestId"]
        self.timestamp = request_dict["timestamp"]
        self.locale = request_dict["locale"]

        if "intent" in request_dict.keys():
            self.intent = Intent(request_dict["intent"])
        else:
            self.intent = None

        if "dialogState" in request_dict.keys():
            self.dialog_state = request_dict["dialogState"]
        else:
            self.dialog_state = None


class Intent:
    def __init__(self, intent_dict):
        self.name = intent_dict["name"]

        if "slots" in intent_dict.keys():
            self.slots = intent_dict["slots"]
        else:
            self.slots = {}


class EventProperty:
    pass
