import sys
import pyperclip

TEXT = {
    'agree': """Yes, I agree. That sounds fine to me""",
    'busy': """Sorry, I am busy""",
    'upsell': """Would you consider making this a monthly donation?"""
}

if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + '  copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
