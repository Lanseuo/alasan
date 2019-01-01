# Event

Incoming event are passed to functions that are defined with the appropriate decorator (`@skill.launch()` or `@skill.intent("MyIntent"`) as the first argument. The event is of the class `alasan.Event`.

## Launch

When the user invokes your skill without providing a specific intent, the Launch Request is being called.

```python
@skill.launch()
def launch_intent(event):
    ...
```

## Custom Intent

When the user makes a request that corresponds to one of the intents defined in your intent schema, an Intent Request is being called.

```python
@skill.intent("ExampleIntent")
def example_intent(event):
    ...
```

## Parameters

The JSON event sent to your skill is parsed into classes. They can be accessed using the `event` parameter. The names of the parameters conform with the names declared in the [Amazon JSON Request Reference](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html#request-format). But all parameters are written in underscore_case and start with a lowercase character, not camelCase.

Example: You can access the application ID (`context.System.application.applicationId` in JSON) like that:

```python
@skill.intent("ExampleIntent")
def example_intent(event):
    application_id = event.context.system.application.application_id
    ...
```

| Parameter                                                                                                          | Description                                                                                                                                                                                                                                                                                                          | Type             |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| version                                                                                                            | The version specifier for the request with the value defined as: "1.0"                                                                                                                                                                                                                                               | string           |
| [session](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html#session-object) | The session object provides additional context associated with the request. [More information @ Amazon Developer Docs](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html#session-object)                                                                                      | `alasan.Session` |
| [context](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html#context-object) | The context object provides your skill with information about the current state of the Alexa service and device at the time the request is sent to your service. [More information @ Amazon Developer Docs](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html#context-object) | `alasan.Context` |
| [request](https://developer.amazon.com/docs/custom-skills/request-types-reference.html)                            | A request object that provides the details of the user's request. [More information @ Amazon Developer Docs](https://developer.amazon.com/docs/custom-skills/request-types-reference.html)                                                                                                                           | `alasan.Request` |
