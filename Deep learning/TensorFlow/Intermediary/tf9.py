import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
import tensorflow_hub as hub

# Pretrained Hub Model

x = tf.random.normal(shape=(5, 299, 299, 3))
y = tf.constant([0, 1, 2, 3, 4])
url = "https://tfhub.dev/google/imagenet/inception_v3/feature_vector/4"
base_model = hub.KerasLayer(url, input_shape=(299, 299, 3))
base_model.trainable = False

model = keras.Sequential(
    [
        base_model,
        layers.Dense(128, activation="relu"),
        layers.Dense(64, activation="relu"),
        layers.Dense(5, activation="softmax"),
    ]
)

model.compile(
    optimizer=keras.optimizers.Adam(),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"],
)

model.fit(x, y, batch_size=32, epochs=15)
