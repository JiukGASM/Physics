from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt

network = models.Sequential()

network.add(layers.Flatten())
network.add(layers.Dense(64, activation='relu'))
network.add(layers.Dense(10, activation='softmax'))


(train_images, train_labels), (test_images, test_labels) = mnist.load_data() # bring data 3D matrix

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=10, batch_size=64)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

x0 = np.array(1)
print("0th order tensor :",x0,"Dim =", x0.ndim)

x1 = np.array([1,2,3,4])
print("1th order tensor :",x1,"Dim =", x1.ndim)

x2 = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,0,1,2]])
print("2th order tensor :",x2,"Dim =", x2.ndim)

x3 = np.array(
    [
        [
            [1,2,3,4],
               [5,6,7,8],
               [9,0,1,2]
        ],
        [
            [1,2,3,4],
               [5,6,7,8],
               [9,0,1,2]
        ],
        [
               [1,2,3,4],
               [5,6,7,8],
               [9,0,1,2]
        ]
    ]
)
print("3th order tensor :",x3,"Dim =", x3.ndim)
print(x3.shape)

from tensorflow.keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("Dim =", train_images.ndim)
print("Shape =", train_images.shape)
print("Type =", train_images.dtype)

digit = train_images[0]

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
plt.show()


