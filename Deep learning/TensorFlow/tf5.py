import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

tf.random.set_seed(42)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Custom layer
class Dense(layers.Layer):
    def __init__(self, units):
        super(Dense, self).__init__()
        self.units = units

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b

    def build(self, input_shape):
        # Weights
        self.w = self.add_weight(
            name="w",
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True,
        )
        # Biases
        self.b = self.add_weight(
            name="b", shape=(self.units,), initializer="zeros", trainable=True
        )


# Custom activation function
class MyReLU(layers.Layer):
    def __init__(self):
        super(MyReLU, self).__init__()

    def call(self, x):
        return tf.math.maximum(x, 0)


# Custom model
class MyModel(keras.Model):
    def __init__(self, num_classes=10):
        super(MyModel, self).__init__()
        self.flatten = layers.Flatten()
        self.dense1 = Dense(64)
        self.dense2 = Dense(num_classes)
        self.relu = MyReLU()

        # self.dense1 = layers.Dense(64)
        # self.dense2 = layers.Dense(num_classes)

    def call(self, input_tensor):
        x = self.flatten(input_tensor)
        x = self.relu(self.dense1(x))
        return tf.nn.softmax(self.dense2(x))


model = MyModel()
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"],
)

model.fit(x_train, y_train, batch_size=32, epochs=3)
