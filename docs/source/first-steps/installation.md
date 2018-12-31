# Installation

Alasan uses [serverless](https://serverless.com/), a toolkit for deploying serverless application, to upload your skill to AWS Lambda. You can install it using the package manager [npm](https://www.npmjs.com/).

```shell
npm install -g serverless
```

Next we will create a project using serverless

```shell
serverless create --template aws-python3 --path <name-of-your-skill>
cd <name-of-your-skill>
```

Next we will install Alasan using pip. Moreover, put *alasan* into *requirements.txt*.

```shell
pip install alasan
echo alasan > requirements.txt
```

Serverless needs a plugin for managing Python requirements. We can install it like that.

```shell
sls plugin install -n serverless-python-requirements
```

Next we will have to configure serverless. Therefore we can use the a configuration file called `serverless.yml`. Put the following into the file.

```yaml
service: <name-of-your-skill>

provider:
  name: aws
  runtime: python3.6

functions:
  skill:
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

Replace `<name-of-your-skill>` with the name your AWS Lambda function should be called. Moreover, we have to change the handler, the entrypoint for our skill. Replace `myskill` with the name of your file / module and `skill` with the instance of Alasan (`skill = Alasan()`).

For example if you are using one file ...

```
- awesome_skill.py [ my_skill = Alasan() ]
- README.md
...
```

... your configuration should look like that: `handler: awesome_skill.my_skill`.

But if you are using a module ...

```
- fun_skill
  - __init__.py [ skill = Alasan() ]
  ...
- README.md
...
```

... your configuration should look like that: `handler: fun_skill.skill`.