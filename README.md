# Network Automation Webex ChatOps Bot
This is a ChatOps Webex bot that uses Python scripts to return several different types of network-related information to the Webex user. 

* /echo: Reply back with the same message sent.
* /help: Get help.
* /showping: Returns ping results with packet count set to 1. Usage: /showping google.com OR /showping 8.8.8.8
* /pingip: checks if IP address is up/down (valid/invalid). Usage: /pingip google.com OR /pingip 8.8.8.8
* /routefilter: invokes route-filter shell script. Requires both address/network device parameter and destination address parameter. Usage: /routefilter R1 4.4.4.4
* /link: Returns the URL that matches the link name. Usage: /link LINK_NAME (example: /link google returns "http://www.google.com" as configured in the file **linkslist.csv**


## Contacts
* Rohit Sharma (rohisha5@cisco.com)
* Gerardo Chaves (gchaves@cisco.com)

## Installation and Usage
In order to run this in your environment, you can start by cloning the repo:
```
$ git clone https://wwwin-github.cisco.com/gve/Net-Automation-ChatOps-Bot.git

```
Next, if you don't already have a Cisco Webex account, go ahead and register for one.  They are free.
You'll need to start by adding your bot to the Cisco Webex website.

[https://developer.ciscospark.com/add-app.html](https://developer.ciscospark.com/add-app.html)

1. Click create bot
2. Fill out all the details about your bot.
3. Click "Add Bot" and make sure to copy your bot access token! You will need this later.


Now open a terminal console window and navigate to the folder containing the cloned repo. Create a virtualenv and install the module.

```
virtualenv venv
source venv/bin/activate
pip install ciscosparkbot
```

NOTE: You can see the source code and documentation for the ciscosparkbot library here: https://github.com/imapex/ciscosparkbot

Next, using the same terminal window, set a few environment variables (if using ngrok, you will obtain the SPARK_BOT_URL as instructed further below):

```
export SPARK_BOT_URL=<your bots external URL>
export SPARK_BOT_TOKEN=<your bots token>
export SPARK_BOT_EMAIL=<your bots email>
export SPARK_BOT_APP_NAME=<your bots name>
```

You can also keep those export statements in a local .sh script (i.e. set_env.sh) for convenience but take care not to share the bot token in particular since it can be used to control all functionality of the bot
Once you have the commands in the file, you can load them using the following command in the same terminal:
```
source set_env.sh
```

### ngrok

ngrok will make easy for you to develop your code with a live bot.

You can find installation instructions here: https://ngrok.com/download

After you've installed ngrok, in another window start the service


`ngrok http 5000`


You should see a screen that looks like this:

```
ngrok by @inconshreveable                                                                                                                                 (Ctrl+C to quit)

Session Status                online
Version                       2.2.4
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://this.is.the.url.you.need -> localhost:5000
Forwarding                    https://this.is.the.url.you.need -> localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              2       0       0.00    0.00    0.77    1.16

HTTP Requests
-------------

POST /                         200 OK
```

Make sure and update your environment with this url:

```
export SPARK_BOT_URL=https://this.is.the.url.you.need

```

Now launch your bot!!


```
python netchatopsbot.py
```

You are now able to interact with your bot in a Webex Teams space!
