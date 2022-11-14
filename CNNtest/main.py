import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import PIL
import pathlib
import os
from zipfile import ZipFile
from tensorflow import keras
from keras_preprocessing.image import ImageDataGenerator
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
# from keras.preprocessing.image import ImageDataGenerator
# from keras.utils import img_to_array, load_img
# from keras.models import load_model

train_path = 'archive/fruits-360/Training/'
# test_path = 'archive/fruits-360/Validation/'
test_path = 'archive/fruits-360/Validation'


batch_size = 128
img_height = 100
img_width = 100


# train_data = tf.keras.preprocessing.image_dataset_from_directory(
#     train_path,
#     validation_split=0.2,
#     subset='training',
#     seed=42,
#     image_size=(img_height, img_width),
#     batch_size=batch_size
# )
#
# val_data = tf.keras.preprocessing.image_dataset_from_directory(
#     train_path,
#     validation_split=0.2,
#     subset='validation',
#     seed=42,
#     image_size=(img_height, img_width),
#     batch_size=batch_size
# )
#
#
# class_names = train_data.class_names
# num_classes = len(class_names)


datagen = ImageDataGenerator(rescale=1./255)
# train_generator = datagen.flow_from_directory(
#     train_path,
#     target_size=(img_height,img_width),
#     batch_size=batch_size,
#     class_mode='categorical'
# )

test_generator = datagen.flow_from_directory(
    test_path,
    target_size=(img_height,img_width),
    batch_size=batch_size,
    class_mode='categorical'
)


# model = tf.keras.Sequential([
#     keras.Input(shape=(img_height, img_width, 3)),
#
#     keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
#     keras.layers.MaxPooling2D(2),
#     keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
#     keras.layers.MaxPooling2D(),
#     keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
#     keras.layers.MaxPooling2D(2),
#     keras.layers.Dropout(0.5),
#
#     keras.layers.Flatten(),
#     keras.layers.Dense(128, activation='relu'),
#     keras.layers.Dense(num_classes,  activation='softmax')
# ])
#
# model.summary()
#
#
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# history = model.fit(
#   train_generator,
#   steps_per_epoch=15,
#   validation_steps=20,
#   validation_data=test_generator,
#   epochs=50,
#   verbose=1
# )
#
# model.save("Fruitmodel.h5")


model = keras.models.load_model('Fruitmodel.h5')

loss, acc = model.evaluate(test_generator)

print('Loss:', loss)
print('Accuracy:', acc)
