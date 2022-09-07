import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
import tensorflow_hub as hub


tf.random.set_seed(42)

# Pretrained Keras Model
x = tf.random.normal(shape=(3, 299, 299, 3))
y = tf.constant([0, 1, 2])

model = keras.applications.InceptionV3(include_top=True)
model.summary()

base_inputs = model.layers[0].input
base_outputs = model.layers[-2].output
final_output = layers.Dense(3, activation="softmax")(base_outputs)

new_model = keras.Model(inputs=base_inputs, outputs=final_output)

new_model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"],
)

new_model.summary()
new_model.fit(x, y, epochs=15)
