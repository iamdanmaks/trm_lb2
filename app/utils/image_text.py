from google.cloud import vision
import io


def detect_text(image_file):
    client = vision.ImageAnnotatorClient()

    content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    return texts[0].description
