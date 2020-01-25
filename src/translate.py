# -*- coding: utf-8 -*-
from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client.json"
def translate_text(text):
    # text = "hello i am Aashi"
    target='hi'
    """
    Target must be an ISO 639-1 language code.
    https://cloud.google.com/translate/docs/languages
    """
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    return(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
# translate_text()
# example_text = "Hola saludos desde Colombia excelentes tutoriales me gustaría poder por lo menos tener los subtitulos ene español ...excelente gracias por compartir tus conocimientos"
# translate_text(example_text.encode().decode()('utf-8'),target='en')
