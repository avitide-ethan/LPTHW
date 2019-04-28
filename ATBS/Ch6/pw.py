#! python3
# pw.py - Insecure password locker program from ATBS Ch6.

PASSWORDS =  {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Copied password for {} to the clipboard'.format(account))
else:
    print("There is no account named" + account)

