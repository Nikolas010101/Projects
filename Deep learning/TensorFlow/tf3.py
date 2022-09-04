import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = keras.Sequential(
    [
        layers.SimpleRNN(
            256, return_sequences=True, input_shape=(28, 28), activation="relu"
        ),
        layers.SimpleRNN(256, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    metrics=["accuracy"],
)

model.fit(x_train, y_train, batch_size=64, epochs=10)
model.evaluate(x_test, y_test, batch_size=64)
