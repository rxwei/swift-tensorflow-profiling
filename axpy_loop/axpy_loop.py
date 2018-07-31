import tensorflow as tf
from tensorflow.python.ops import functional_ops
from tensorflow.python.framework import ops
from tensorflow.python.framework import function
from tensorflow.python.framework import dtypes
import time

def time_this(f):
    start = time.time()
    print 'Start: %ss' % start
    f()
    end = time.time()
    print 'End: %ss' % end
    print 'Elapsed: %ss' % (end - start)

with ops.Graph().as_default() as g:
    x_init = tf.constant(0.2, shape=[64, 512])
    w = tf.constant(0.2, shape=[512, 512])
    b = tf.constant(0.2, shape=[512])

    @function.Defun(dtypes.int32, *[dtypes.float32] * 3)
    def Cond(i, x, w, b):
        return i < 1000

    @function.Defun(dtypes.int32, *[dtypes.float32] * 3)
    def Body(i, x, w, b):
        return i + 1, tf.matmul(x, w) + b, w, b

    y = functional_ops.While([0, x_init, w, b], Cond, Body)

    def main():
        with tf.Session(graph=g) as sess:
            sess.run(y)
    time_this(main)
    tf.train.write_graph(g, '.', 'python_graph.pbtxt')

