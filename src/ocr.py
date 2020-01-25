# '''from google.cloud import vision
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcp-explore-261416-44d1aa9d9fa7.json"
# client = vision.ImageAnnotatorClient()
# import io
#
# path = "/home/aashi/Downloads/index.jpeg"
# with io.open(path, 'rb') as image_file:
#         content = image_file.read()
# image = vision.types.Image(content=content)
# response = client.image_properties(image=image)
# props = response.image_properties_annotation
# print('Properties of the image:')
#
# for color in props.dominant_colors.colors:
#     print('Fraction: {}'.format(color.pixel_fraction))
#     print('\tr: {}'.format(color.color.red))
#     print('\tg: {}'.format(color.color.green))
#     print('\tb: {}'.format(color.color.blue))'''

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print(texts)
    # print(texts.description)
    # return ("hello")
    l = []
    for text in texts:
        l.append((text.description))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
    return l    #             for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))

# detect_text("C://Users//Shilpa Bundela//Desktop//ocr//upload_file_python-master//src//images//demo.jpg")
'''path and name of image'''
# import os
'''# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client.json"'''
# def detect_text(uri):
#     """Detects text in the file located in Google Cloud Storage or on the Web.
#     """
#     from google.cloud import vision
#     client = vision.ImageAnnotatorClient()
#     image = vision.types.Image()
#     image.source.image_uri = uri
#
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print('Texts:')
#     print((texts))
#
#     for text in texts:
#         print('\n"{}"'.format(text.description))
#
#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])
#
#         print('bounds: {}'.format(','.join(vertices)))
# detect_text("gs://uniqueway1/index.jpeg")
