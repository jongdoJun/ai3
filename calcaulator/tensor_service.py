import tensorflow as tf
tf.__version__
class TensorService:
    def __init__(self, payload):
       # print(tf.VERSION)
        self._num1 = payload.num1
        self._num2 = payload.num2

    @tf.function
    def add(self):
        return tf.add(self._num1 , self._num2)

    @tf.function
    def subract(self):
        return tf.subtract(self._num1 , self._num2)

    @tf.function
    def multiply(self):
        return tf.multiply(self._num1 , self._num2)

    @tf.function
    def divide(self):
        return tf.divide(self._num1 , self._num2)