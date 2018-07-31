import tensorflow as tf
from tensorflow.python.framework import ops
import time

def time_this(f):
    start = time.time()
    print 'Start: %ss' % start
    f()
    end = time.time()
    print 'End: %ss' % end
    print 'Elapsed: %ss' % (end - start)

with ops.Graph().as_default() as g:
    x = tf.Variable(tf.constant(0.2, shape=[512, 512]))

    # 1000 times
    for i in xrange(1000):
        x = tf.assign(x, x + 0.2)

    def main():
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(x)
    time_this(main)

    tf.train.write_graph(g, '.', 'python_graph.pbtxt')