# xmpp-chat
Project for the Networks course. The idea is to have a chat user that works over the XMPP protocol.
To install and use this program, you can follow this simple steps:

### Windows
Make sure you have python installed or you won't be able to use this program. To verify if it is installed, you can open a command prompt by searching for "Command Prompt" or "cmd" in the windows start menu.

Once you have opened the command prompt, type "python". If output comes out, it will include the version you are using and you'll know it is installed.

If you do not have python, you have to go to the python website (https://www.python.org/downloads/) and download the python version 3.6.5 as it is the one I used to develop this chat. 

Next, you have to install some libraries using pip. If you try using pip and it doesn't seem to be installed, you have to install it. To do so, you can write `<python get-pip.py>`on the command prompt to get it installed. You can check its installation by using the `<pip -v>` command on the command prompt.

Once pip is installed, you have to add the following libraries:
`<pip install Sleekxmpp>`
`<pip install dnspython>`

Once intalled, you can run the program by going to the path the file is inside the command prompt and write: `<python chatUser.py>`.

### Linux
The same rules apply to the Linux configuration as they did for the Windows one. First, you have to check if python is installed or not. Open a terminal and type `<python>` into it. If no output comes out, go to the python website (https://www.python.org/downloads/) and download the 3.6.5 version. 

Next, you have to install some libraries using pip. If you try using pip and it doesn't seem to be installed, you have to install it. To do so, you can write `<apt install python3-pip>`on the terminal to get it installed. You can check its installation by using the `<pip -v>` command on the terminal.

Once pip is installed, you have to add the following libraries:
`<pip install Sleekxmpp>`
`<pip install dnspython>`

Once intalled, you can run the program by going to the path the file is inside the command prompt and write: `<python chatUser.py>`.
