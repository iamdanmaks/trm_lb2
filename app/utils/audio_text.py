from google.cloud import storage
from google.cloud import speech

from tempfile import TemporaryFile


def upload_blob(bucket_name, source_file, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    t = TemporaryFile()
    t.write(source_file.read())
    t.seek(0)

    blob.upload_from_file(t)


def transcribe_text(audio_file):
    upload_blob('trm-lb2', audio_file, 'temp.mp3')

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(
        uri='gs://trm-lb2/temp.mp3'
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=48000,
        language_code="en-US"
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    return ' '.join([r.alternatives[0].transcript for r in response.results])
