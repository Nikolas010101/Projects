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

# Sequential API
model1 = keras.Sequential(
    [
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(64, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ]
)

# Functional API
inputs = layers.Input(shape=(28, 28))
x = layers.Flatten()(inputs)
x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(10, activation="softmax")(x)

model2 = keras.Model(inputs=inputs, outputs=outputs)

# Subclassing API
class MyModel(keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.flatten = layers.Flatten(input_shape=(28, 28))
        self.dense1 = layers.Dense(64, activation="relu")
        self.dense2 = layers.Dense(10, activation="softmax")

    def call(self, input_tensor):
        input = self.flatten(input_tensor)
        x = self.dense1(input)
        return self.dense2(x)


model3 = MyModel()

model = keras.models.load_model("complete_saved_model/")

model.fit(x_train, y_train, batch_size=32, epochs=2)
model.evaluate(x_test, y_test, batch_size=32)
model.save("complete_saved_model/")
