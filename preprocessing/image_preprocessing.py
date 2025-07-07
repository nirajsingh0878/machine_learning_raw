import tensorflow as tf
from tensorflow.keras import layers


def get_image_preprocessing_pipeline(input_size, resize):
    # Write your code here.
    image_preprocessing_pipeline = tf.keras.Sequential([
        layers.Resizing(height=resize,width=resize),
        layers.Rescaling(1/255),
        layers.RandomFlip("horizontal_and_vertical"),
        layers.RandomRotation(0.1),
        layers.RandomContrast(0.1),
        layers.RandomCrop(int(resize*0.9),int(resize*0.9),3),
        layers.RandomZoom(height_factor=0.1,width_factor=0.1),
        layers.RandomTranslation(height_factor=0.1,width_factor=0.1),
        layers.RandomBrightness(factor=0.1),
    ])

    image_preprocessing_pipeline.build(input_shape=(input_size,input_size,3))
    return image_preprocessing_pipeline




'''
Image Preprocessing 🟢 ⭐
Image classification problems often require you to perform preprocessing of the training images to ensure that the image classification model is generalizable into the test and validation data sets.

Implement and return an image preprocessing pipeline using TensorFlow sequential layers.

The image preprocessing pipeline should contain:

A resizing layer of 180x180x3

A rescaling layer to result in pixel values between 0 and 1

A random flip layer to result in horizontal and vertical augmentation

A random rotation layer with a factor of 0.1

A random contrast layer with a factor of 0.1

A random crop layer with a height and width factor of 0.9

A random zoom layer with a height and width factor of 0.1

A random translation layer with a height and width factor of 0.1

A random brightness layer with a factor of 0.1

You will then build the pipeline with an input layer of 270x270x3 and then return the compiled image processing pipeline.
'''