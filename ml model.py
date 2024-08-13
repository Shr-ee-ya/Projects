import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten

from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

IMAGE_SIZE = [224, 224]
train_path = r'C:\Users\91881\OneDrive\Desktop\chest_xray\train'
test_path = r'C:\Users\91881\OneDrive\Desktop\chest_xray\test'

vgg=VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
for layer in vgg.layers:
    layer.trainable = False

folders= glob(r'C:\Users\91881\OneDrive\Desktop\chest_xray\train\*')
x= Flatten()(vgg.output)
prediction= Dense(len(folders), activation='softmax')(x)

model= Model(inputs=vgg.input, outputs=prediction)
model.summary()

from types import MethodDescriptorType
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen= ImageDataGenerator(rescale=1./255)

training_set=train_datagen.flow_from_directory(r'C:\Users\91881\OneDrive\Desktop\chest_xray\train',
                                               target_size=(224,224),
                                               batch_size=10,
                                               class_mode='categorical')

test_set=test_datagen.flow_from_directory(r'C:\Users\91881\OneDrive\Desktop\chest_xray\test',
                                          target_size=(224,224),
                                          batch_size=10,
                                          class_mode='categorical')

r = model.fit(
    training_set,
    validation_data=test_set,
    epochs=1,
    steps_per_epoch=len(training_set),
    validation_steps=len(test_set)
)

import tensorflow as tf
from keras.models import load_model

model.save('chest_xray.h5')
from keras.models import load_model

from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
#model=load_model(r'C:\Users\91881\OneDrive\Desktop\practice\pnuemonia_detection\my_model.keras')
model = load_model(r'C:\Users\91881\OneDrive\Desktop\practice\pnuemonia_detection\chest_xray.h5')


img=image.load_img(r'C:\Users\91881\OneDrive\Desktop\chest_xray\val\NORMAL\NORMAL2-IM-1431-0001.jpeg',target_size=(224,224))
x=image.img_to_array(img)
x=np.expand_dims(x,axis=0)
img_data=preprocess_input(x)
classes=model.predict(img_data)

#classes
result=classes[0][0]

if result>0.5:
    print("Result is Normal")
else:
    print("Person is Affected By PNEUMONIA")
