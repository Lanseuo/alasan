# Your first skill

In this section you are going to create your first skill. You will be able to say hello and your skill will greet you back. Therefore we need one custom intent. Create a custom intent called `HelloIntent` in the Alexa Developer Console and add *Hello* as a Sample Utterance.

A conversation with the skill could look like that:

- **User**: Alexa, start awesome skill.
- **Alexa**: Welcome from Alasan. Say hello to me!
- **User**: Hello.
- **Alexa**: Hello, thanks for chatting with me.

First of all we need to import Alasan and create an instance of it.

```python
from alasan import Alasan, Response

skill = Alasan()
```

## LaunchIntent

Next we can listen to *LaunchIntent*s. They are called, when the user starts the skill (Alexa, open ... / Alexa, start ...).

```python
@skill.launch()
def launch():
    ...
```

## Response

Now we want to build a response for the intent. Therefore we use the class `Response` and return it. The response is built using method cascading.

```python
@skill.launch()
def launch():
    return Response.speak("Welcome to Alasan. Say hello to me!")
```

## Custom Intent

After that Alexa waits for a new intent. If the user says *Hello*, a *HelloIntent* will be fired.

```python
@skill.intent("HelloIntent")
def hello_intent():
    ...
```

This time we want to respond, but then the skill should end. Therefore we have to call the method `end_session()`.

```python
@skill.intent("HelloIntent")
def hello_intent():
    return Response \
        .speak("Hello, thanks for chatting with me.") \
        .end_session()
```

## Deployment

That's it. Now we can test our skill. To do so, we have to upload it to AWS Lambda. We will be using serverless for that.

```shell
serverless deploy
```

Now you should be able to talk to your skill. Just say: *Alexa, start awesome skill.*