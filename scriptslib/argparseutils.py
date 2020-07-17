"""
Common functions and classes and examples used in scripts when working with argparse.
"""

import getpass


class ArgParsePasswordHandler:
    """
    This is used to provide a password prompt for use with argparse.
    ```
    ###
    # This shows how it is used to accept 
    # username/password on the commandline.
    ###

    import argparse
    import getpass
  
    parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--username', help='Specify username',default=getpass.getuser())
    parser.add_argument('-p', '--password', type=ArgParsePasswordHandler, help='Specify password',
    default=ArgParsePasswordHandler.DEFAULT)
    args = parser.parse_args()
   
    print(args.username, args.password)    
    ```
    """

    DEFAULT = 'Password:'

    def __init__(self, value):
        if value == self.DEFAULT:
            value = getpass.getpass('Password: ')
        self.value = value

    def __str__(self):
        return self.value
