# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
import os
import subprocess
import csv
from ciscosparkbot import SparkBot
from ciscosparkbot.models import Response

# Retrieve required details from environment variables
bot_email = os.getenv("SPARK_BOT_EMAIL")
spark_token = os.getenv("SPARK_BOT_TOKEN")
bot_url = os.getenv("SPARK_BOT_URL")
bot_app_name = os.getenv("SPARK_BOT_APP_NAME")

def do_something(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Spark
    :return: A text or markdown based reply
    """
    return "i did what you said - {}".format(incoming_msg.text)

# retrieve a link from a list in the linklist.csv files
# this function reads through the linklist.csv file every time it is invoked looking for a match which is
# not very efficient, but you can change the linklist.csv file at any time and not have to restart the bot script
def get_link(incoming_msg):

    incomingtext = incoming_msg.text

    incominglist = incomingtext.split(' ')
    if len(incominglist) != 2:
        output = "error: missing link name to retrieve"
        return output
    else:
        textarg = incomingtext.split(' ')[-1]
        theLink="link not found"
        # Open and read csv file
        with open('linkslist.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = None

            for row_number, row in enumerate(csv_reader):

                if row_number is 0:
                    header = row
                    continue

                else:
                    link_name = row[0]
                    if textarg==link_name:
                        theLink = row[1]
                        break

        return theLink


def ret_message(incoming_msg):
    m = Response()
    u = 'https://sayingimages.com/wp-content/uploads/'
    u = u + 'aaaaaalll-righty-then-alrighty-meme.jpg'
    m.files = u
    return m

def ping_message(incoming_msg):
    #osstring = Response()
    #osstring = str(os.system('echo ping -c 1 8.8.8.8'))
    incomingtext = incoming_msg.text
    incominglist=incomingtext.split(' ')
    if len(incominglist) != 2:
        output = "error: missing hostname or IP address to ping"
    else:
        textarg = incominglist[-1]
        output =  subprocess.check_output("ping -c 1 " + textarg, shell=True)
        output = output.decode('utf-8')
    return output

def pingip_message(incoming_msg):
    incomingtext = incoming_msg.text

    incominglist = incomingtext.split(' ')
    if len(incominglist) != 2:
        output = "error: missing hostname or IP address to ping"
        return output
    else:
        textarg = incomingtext.split(' ')[-1]
        osreturn = os.system("ping -c 1 " + textarg)
        if osreturn == 0:
            return textarg + " IS ALIVE."
        else:
            return textarg + " IS DOWN."
        #return textarg + " IS DOWN."

def routefilter_message(incoming_msg):
    incomingtext = incoming_msg.text
    destroute = incomingtext.split(' ')[-1]
    ipaddr = incomingtext.split(' ')[-2]
    commstring = "./routefilter.sh " + ipaddr + " " + destroute
    output = subprocess.check_output(commstring, shell=True)
    #output = subprocess.check_output(subprocess.call(['./routefilter.sh', ipaddr, destroute]))
    output = output.decode('utf-8')
    return output

print(bot_app_name, spark_token, bot_url,  bot_email)

# Create a new bot
bot = SparkBot(bot_app_name, spark_bot_token=spark_token,
               spark_bot_url=bot_url, spark_bot_email=bot_email, debug=True)


# Add new command
bot.add_command('/dosomething', 'help for do something', do_something)
bot.add_command('/demo', 'sample that allows spark message to be returned',
                ret_message)
bot.add_command('/showping', 'Returns ping results with packet count set to 1. Usage: /showping DESTINATION', ping_message)
bot.add_command('/pingip', 'checks if IP address is up/down (valid/invalid). Usage: /pingip DESTINATION', pingip_message)
bot.add_command('/routefilter', 'invokes route-filter shell script.', routefilter_message)
bot.add_command('/link', 'Returns the URL that matches the link name. Usage: /link LINK_NAME', get_link)


# Run Bot
bot.run(host='127.0.0.1', port=5000)
