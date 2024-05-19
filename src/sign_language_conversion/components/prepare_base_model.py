import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from sign_language_conversion.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def get_base_model(self):
        
        input_shape = (224, 224, 3)
        inputs = tf.keras.layers.Input(shape=input_shape)
        
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
            input_tensor=inputs
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes):
        for layer in model.layers:
            model.trainable = False
            
        input_shape = (224, 224, 3)
        inputs = tf.keras.layers.Input(shape=input_shape)
            
        block_output = model.output

        flatten_in = tf.keras.layers.Flatten()(block_output)
        
        Dense1 = tf.keras.layers.Dense(512, activation='relu', kernel_initializer='he_uniform')(flatten_in)
        
        Dense2 = tf.keras.layers.Dense(216, activation='relu', kernel_initializer='he_uniform')(Dense1)
        
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(Dense2)

        full_model = tf.keras.models.Model(
            inputs=inputs,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

