Flask Example - Hotter or Colder app
=====================================

Small example Flask applicaton created by reworking a MediaCloud Flask example created by Rahul for MAS.500.

Challenges along the way
---------

Be really diligent about setting up requirements.txt and including the libraries at the top of your .py file.  Only include libraries in requirements.txt that aren't included with Python3 as standard.

You need a Procfile in the root of the repo when deploying to Heroku.

You need a runtime.txt file which specifies which version of Python you're using.

Use heroku logs to check what might have gone wrong when you're trying to deploy your app.

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



