import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np


def get_prediction(img_path):
    model = load_model('model/model_categorical.h5')
    # load image
    img = load_img(img_path, target_size=(300, 300), color_mode='grayscale')    # Load the image with target size
    img = img_to_array(img)         # Convert it to a numpy array with target shape
    img = img / 255                 # Rescale by 1/255
    img = np.expand_dims(img, axis=0)

    # predict
    prediction = model.predict(img)

    # get class
    classes = np.argmax(prediction, axis=1)
    if classes == 0:
        return 'NORMAL'
    elif classes == 1:
        return 'PNEUMONIA BACTERIA'
    elif classes == 2:
        return 'PNEUMONIA VIRUS'

    return 'not valid'





