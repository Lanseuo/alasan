# Alasan

Alasan helps you building Alexa skills on AWS Lambda using Python.

## Installation

```
npm install -g serverless
serverless create --template aws-python3 --path <name-of-your-skill>
cd <name-of-your-skill>
echo git+https://github.com/Lanseuo/alasan.git > requirements.txt
sls plugin install -n serverless-python-requirements
```

serverless.yml

```yml
service: <name-of-your-skill>

provider:
  name: aws
  runtime: python3.6

functions:
  skill:
    # replace `myskill` with the name of your file / module and `skill` with the instance of Alasan (`skill = Alasan()`)
    handler: myskill.skill

package:
  individually: true
  exclude:
    - ./**
  include:
    - myskill.py

plugins:
  - serverless-python-requirements
```

## Usage

```python
from alasan import Alasan, Response

skill = Alasan()

@skill.launch()
def launch(event):
    return Response.speak("Was möchtest Du wissen?")


@skill.intent("FineIntent")
def fine_intent(event):
    return Response \
        .speak("That's good to hear.") \
        .end_session()
```

## Deployment

```
sls deploy
```

## Made with

- [serverless](https://serverless.com/) - serverless application framework

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas-hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details

