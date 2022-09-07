import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist
import tensorflow_hub as hub


tf.random.set_seed(42)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Pretrained-Model
model = keras.models.load_model("complete_saved_model/")
model.trainable = False

for layer in model.layers:
    assert layer.trainable == False
    layer.trainable = False

base_inputs = model.layers[0].input
base_outputs = model.layers[-2].output
final_output = layers.Dense(10, activation='softmax', name="new_dense")(base_outputs)
new_model = keras.Model(inputs=base_inputs, outputs=final_output)
new_model.summary()

new_model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"],
)

new_model.fit(x_train, y_train, batch_size=32, epochs=3)
