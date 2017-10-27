import utils


def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest, etc).
    The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID
    to prevent someone else from configuring a skill that sends requests
    to this function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")


    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


# ---------functions starts here --------------------------

def on_session_started(session_started_request, session):
    """Called when the session starts."""
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])


def on_launch(launch_request, session):
    """Called when the user launches the skill without specifying what they want."""
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """Called when the user specifies an intent for this skill."""

    # get ticker data intent
    if intent_request['intent']['name'] == "GetTickerPrice":
        tickerdata = utils.gettickerdata(intent_request['intent']['slots']['ticker']['value'])
        return build_response([], build_speechlet_response(
            "Current price of " + intent_request['intent']['slots']['ticker']['value'] + " is: ",
            tickerdata, "repromt",
            True))
    # create portfolio intent
    if intent_request['intent']['name'] == "CreatePortfolio":
        return elicit_response("test", False)


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# portfolioUtil.createportfolio("Myown")
# portfolioutil.insertportfolio("AAPL", 20, 100.1, "Myown_pf")
print(utils.gettickerdata('overstock'))
# --------------- Functions that control the skill's behavior -------------


def get_welcome_response():
    """If we wanted to initialize the session to have some attributes we could add those here."""
    welcome_txt = "Hi, welcome to stockit. If you have to create a new portfolio, say PORTFOLIO." \
                  " Else, just state the name of the stock that you want to follow. Thank you"
    return build_response([], build_speechlet_response("Stockit", welcome_txt, "repromt", True))


# --------------- Helpers that build all of the responses -----------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }


def elicit_response(attributes, should_end_session):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': {
            "outputSpeech": {
                "type": "PlainText",
                "text": "what should we name the portfolio"
            },
            "shouldEndSession": should_end_session,
            "directives": [
                {
                    "type": "Dialog.ElicitSlot",
                    "slotToElicit": "portfolioname",
                    "updatedIntent": {
                        "name": "CreatePortfolio",
                        "confirmationStatus": "NONE",
                        "slots":
                            {"portfolioname": {
                                "name": "portfolioname",
                                "confirmationStatus": "NONE"
                            }}
                    }
                }]}}
