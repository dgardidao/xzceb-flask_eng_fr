import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of the LanguageTranslatorV3 class
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL
language_translator.set_service_url(url)


def english_to_french(english_text):
    # Use the Language Translator to translate English to French
    if english_text != None:
    	translation_response = language_translator.translate(
        	text=english_text,
        	source='en',
        	target='fr'
    	).get_result()

    	# Extract the translated text from the response
    	french_text = translation_response['translations'][0]['translation']
    else:
        french_text = None
    # Return the translated text
    return french_text

def french_to_english(french_text):
    # Use the Language Translator to translate French to English
    if french_text != None:
    	translation_response = language_translator.translate(
        	text=french_text,
        	source='fr',
        	target='en'
    	).get_result()

    	# Extract the translated text from the response
    	english_text = translation_response['translations'][0]['translation']
    else:
        english_text = None
    # Return the translated text
    return english_text
