Flask Example - Hotter or Colder app
=====================================

Small example Flask applicaton created by reworking a MediaCloud Flask example created by Rahul for MAS.500.

Installation
------------

Make sure you havy Python 2.7 (and the pip package manager).

You also need to install some requirements:

```
pip install -r requirements.txt
```

Copy `settings.config.template` to `settings.config` and edit it.

Use
---

Run this command and then visit `localhost:5000` with a web browser

```
python mcserver.py
```

You will be able to monitor progress in the `logs/mcserver.log` log file.

Challenges along the way
---------

You need a Procfile in the root of the repo when deploying to Heroku. Only include libraries in here that aren't included with Python3 as standard.

You need a runtime.txt file which specifies which version of Python you're using.

