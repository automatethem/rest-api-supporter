import io
import base64
from PIL import Image
import numpy

'''
from rest_api_supporter.utils.base64_encode import base64_encode
image = Image.open("rock.jpg")
base64 = base64_encode(image)
print(base64) #data:image/png;base64,/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
'''
'''
from rest_api_supporter.utils.base64_encode import base64_encode
import datasets
path = 'up.wav'
dataset = datasets.Dataset.from_dict({"audio": [path]})
dataset = dataset.cast_column("audio", datasets.Audio())
array = dataset[0]["audio"]["array"]
#sampling_rate = dataset[0]["audio"]["sampling_rate"] #Wav2Vec2FeatureExtractor was trained using a sampling rate of 16000. Please make sure that the provided `raw_speech` input was sampled with 16000 and not 8000.
sampling_rate = 16000
base64 = base64_encode(array)
print(base64) #data:audio/wav;base64,UklGRiTuAgBXQVZFZm...At84WACNZGwA=
'''
def base64_encode(image):
    if isinstance(image, Image.Image):
        bytes_io = io.BytesIO()
        image.save(bytes_io, image.format)
        bytes = bytes_io.getvalue()
    elif isinstance(image, numpy.ndarray):
        bytes = image
    base64_encoded = base64.b64encode(bytes)
    base64_encoded = base64_encoded.decode("utf-8") 
    if isinstance(image, Image.Image):
        #return "data:image/png;base64,"+base64_encoded
        return "data:image/"+image.format.lower()+";base64,"+base64_encoded
    elif isinstance(image, numpy.ndarray): 
        return "data:audio/wav;base64,"+base64_encoded
