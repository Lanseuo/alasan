def build_response(response, session_attributes):
    return {
        "version": "1.0",
        "response": response,
        "sessionAttributes": session_attributes
    }


def answer(output, reprompt=None, session_attributes={}, card=None, ssml=False):
    response = {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "shouldEndSession": True
    }

    if reprompt:
        response["reprompt"] = {
            "output_speech": {
                "type": "PlainText",
                "text": reprompt
            }
        }

    if card:
        response["card"] = card

    return build_response(
        response=response,
        session_attributes=session_attributes
    )


def question(output, reprompt=None, session_attributes={}, card=None, ssml=False):
    response = {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "shouldEndSession": False
    }

    if reprompt:
        response["reprompt"] = {
            "output_speech": {
                "type": "PlainText",
                "text": reprompt
            }
        }

    if card:
        response["card"] = card

    return build_response(
        response=response,
        session_attributes=session_attributes
    )
