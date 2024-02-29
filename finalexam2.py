# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

#1) Use your favorite Deep Learning algorithm to train the MNIST fashion data. and 2) Please provide the code and output accuracy of the test sample.
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top',
               'Trouser',
               'Pullover',
               'Dress',
               'Coat',
               'Sandal',
               'Shirt',
               'Sneaker',
               'Bag',
               'Ankle boot']




train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

# #3) Plot counts versus class for all misclassified ones from your algorithm. (with Poisson errors on the counts, see on the right for example)
# predictions = model.predict(test_images)
# correct_prediction = tf.equal(tf.argmax(predictions), tf.argmax(test_labels))
# print(correct_prediction)

index = []
ori = []
pred = []

predictions = model.predict(test_images)

for i in range(len(test_labels)):
    if test_labels[i] != np.argmax(predictions[i]):
        index.append(i)
        ori.append(test_labels[i])
        pred.append(predictions[i])

counts = []
for i in range(0,10):
    counts.append(ori.count(i))

counts = np.array(counts)
error = np.sqrt(counts)
class_names = np.array(class_names)
plt.errorbar(class_names, counts, yerr=error, fmt= 'o')
plt.show()

#4) Discuss why some classes are more misclassified than others and find that your algorithm works the best for which class and the worst for which class.
#티셔츠와 풀오버,셔츠는 비슷한 모양을 가지고있기때문에 misclassified된 경우가 3가지 경우에 특히 비슷하게 많다고 해석된다. 그리고 코트와 드레스가 함께 misclassified가 중간정도로 많게 확인되는데 이도 앞과 같은 이유라고 생각되며, 신발 종류들도 비슷하게 적게 misclassified되었다. touser가 가장 적게 misclassifed되었다.



