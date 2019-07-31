# Universidad del Valle de Guatemala
# Autora: Andrea Cordón
# Carné: 16076
# chatUser.py
# This program is based on the following tutorial: https://sleekxmpp.readthedocs.io/en/latest/

# Importing all the libraries used in this program
import sleekxmpp
from sleekxmpp import ClientXMPP
import sys
import logging
import getpass
from sleekxmpp.exceptions import IqError, IqTimeout
from optparse import OptionParser
from menus import *
   
# Main class (not program)
class MyChatBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, option):

        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # Option for user to select login or sign in
        if (option == "1"):
            self.add_event_handler("session_start", self.sessionStart)
        elif(option == "2"):
            self.add_event_handler("register", self.register)
            self.add_event_handler("session_start", self.sessionStart)
        else:
            print("Please enter 1 or 2")
    
        # For the users personalized message
        self.add_event_handler("message", self.message)

    # Start function to start the session
    def sessionStart(self, event):
        print('Starting session')
        self.send_presence()
        self.get_roster()
        

    # Message management function 
    def message(self, messag):
        if messag['type'] in ('chat', 'normal'):
            messag.reply("Se envio\n%(body)s" % messag).send()
            print(messag)

    # Register management function using sleek exceptions
    def register(self, iq):
        serverResponse = Iq.reg()
        serverResponse["type"] = "set"
        serverResponse["register"]["username"] = self.boundjid.user
        serverResponse["register"]["password"] = self.password

        try:
            serverResponse.send(now=True)
            logging.info("Account created!: %s!" % self.boundjid)
        except IqError as e:
            logging.error("It was imposible to create the account: %s" %
                    e.reg["error"]["text"])
            self.disconnect()
        except IqTimeout:
            logging.error("Server response took longer than wanted, try again.")
            self.disconnect()
    
# Main program
if __name__ == '__main__':

    initialMenu()
    initialOption = input("What would you like to do? (1 or 2): ")
    parserOption = OptionParser()

    # Output options
    parserOption.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    parserOption.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    parserOption.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    # JID and password options
    parserOption.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    parserOption.add_option("-p", "--password", dest="password",
                    help="password to use")

    parserOps, args = parserOption.parse_args()

    #Setear el login
    logging.basicConfig(level=parserOps.loglevel,
                        format='%(levelname)-8s %(message)s')

    if parserOps.jid is None:
        parserOps.jid = input("Username: ")
    if parserOps.password is None:
        parserOps.password = getpass.getpass("Password: ")

    
    # Call to the main class (MyChatBot)
    xmpp = MyChatBot(parserOps.jid, parserOps.password, initialOption)
    

    
    # Call to all Register pluglins
    xmpp.register_plugin('xep_0030') # Service discovery
    xmpp.register_plugin('xep_0004')
    xmpp.register_plugin('xep_0066')
    xmpp.register_plugin('xep_0077')
    xmpp.register_plugin('xep_0199') # XMPP ping
    xmpp['xep_0077'].force_registration = False

  
            
    # Connect to the server
    if xmpp.connect():
        xmpp.process(block=False)
        print("Done")
        while(True):
            userMenu()
            loggedIn_option = input("What would you like to do?: ")

            # To get all the users joined to the chat
            if(loggedIn_option == "1"):
                print("\nContacts:")
                print(xmpp.client_roster)
                print("")

            # Send a message to a specific user 
            elif(loggedIn_option == "2"):
                user= input("What user would you like to message?: ")
                message = input(">> ")
                print("Sending message...")
                xmpp.send_message(mto= user, mbody = message, mtype = 'chat')
                print("Your message has been sent")

            # Add a new user
            elif(loggedIn_option == "3"):
                user = input("Who are you trying to add?: ")
                xmpp.send_presence(pto = user, ptype ='subscribe')
            
            # Send a group message    
            elif(loggedIn_option == "4"):
                print("Option not implemented in this version")

            # Show other user information   
            elif(loggedIn_option == "5"):
                print("Option not implemented in this version")

            # Set personal message    
            elif(loggedIn_option == "6"):
                print("Option not implemented in this version")

            # Log Off    
            elif(loggedIn_option == "7"):
                break   
                print("")

            # Delete my account
            elif(loggedIn_option == "8"):   
                print("Option not implemented in this version")

            # Go back
            elif(loggedIn_option == "Back"):   
                print("Option not implemented in this version")
    
    # In case connection fails       
    else:
        print("You were unable to connect. Try it again later")

    
