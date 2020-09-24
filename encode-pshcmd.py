#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    ṔowerShell Encode Command
#

__version__ = '0.1'
__author__ = 'Michael Ritter'


import base64
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--command', metavar="<command", required=True, help="PowerShell command to encode")
args = parser.parse_args()

command = args.command


encodedPowerShellCommand = base64.b64encode(command.encode('utf-16-le'))
decodedPowerShellCommand = base64.b64decode(encodedPowerShellCommand)

launcherCommand = "powershell.exe -exec bypass -enc " + encodedPowerShellCommand


print("\n\nDecoded Command:\n" + decodedPowerShellCommand)
print("\n\nEncoded Command:\n" + encodedPowerShellCommand)
print("\n\nLauncher Command:\n" + launcherCommand)
