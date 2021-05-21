# Github API challenge named API!

## Overview

This is a simple web services app written in Flask (Python web framework), it listens for events when a new repository is created, triggering a protection mechanism to for the master branch and notifying the owner the administrator using @issue

## Requirements

--------------------------------------------------------------------------------

- Git 2.0+ installed on your machine [Download](https://git-scm.com/)
- Python 3.7+ installed in your machine
- A code editor like [Atom](https://atom.io)
- [A Github account](https://github.com)
- An Github Organisation. _you can create one from your free Github account_
- [A free Ngrok account](https://ngrok.com/)

## Getting started

--------------------------------------------------------------------------------

It's super simple web application, doesn't use docker or anything like that, the idea is you can host this Flask app anywhere with not a specific virtualization platform.

### Setup

1. Fork this repository.
2. Clone this repository to your local machine.
3. Open the terminal and start ngrok server, _this will be used to create a tunnel between your local machine and a webhook from Github._

```bash
./ngrok http 8080
```

1. Once you have your ngrok tunnel working you will need to start up the **server.py**, which is the main component here.

On your terminal window, type the following command.

```bash
export FLASK_APP=server.py
pyton3 -m flask run
```

### Configuration

TBD

## Contributing

--------------------------------------------------------------------------------

Long-term discussion and bug reports are limited only during the interview with Github. Code reviews are possible, as long are done via Github Pull requests.

--------------------------------------------------------------------------------

This project is licensed under the Apache 2.0 License.

### To be deleted

Please create a simple web service that listens for organization events to know when a repository has been created.

When the repository is created please automate the protection of the master branch.

Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

A simple web-application that listens to events from Github API
