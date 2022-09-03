import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

tf.random.set_seed(42)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Sequential API
model = keras.Sequential(
    [
        layers.Flatten(input_shape=(28, 28), name="Input_layer"),
        layers.Dense(512, activation="relu", name="Dense_1"),
        layers.Dense(256, activation="relu", name="Dense_2"),
        layers.Dense(10, activation="softmax", name="Output_layer"),
    ]
)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"],
)

print(model.summary())

model.fit(x_train, y_train, batch_size=32, epochs=5)
model.evaluate(x_test, y_test, batch_size=32)

x_train = x_train.reshape(-1, 28 * 28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28 * 28).astype("float32") / 255.0

# Functional API
inputs = keras.Input(shape=784, name="Input_layer")
x = layers.Dense(512, activation="relu", name="Dense_1")(inputs)
x = layers.Dense(256, activation="relu", name="Dense_2")(x)
outputs = layers.Dense(10, activation="softmax", name="Output_layer")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=["accuracy"],
)

print(model.summary())

model.fit(x_train, y_train, batch_size=32, epochs=5)
model.evaluate(x_test, y_test, batch_size=32)
