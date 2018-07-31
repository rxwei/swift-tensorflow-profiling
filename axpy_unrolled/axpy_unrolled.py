import tensorflow as tf
import time

def time_this(f):
    start = time.time()
    print 'Start: %ss' % start
    f()
    end = time.time()
    print 'End: %ss' % end
    print 'Elapsed: %ss' % (end - start)

x = tf.constant(0.2, shape=[64, 512])
w = tf.constant(0.2, shape=[512, 512])
b = tf.constant(0.2, shape=[512])

# 1000 times
for i in xrange(1000):
    x = tf.matmul(x, w) + b

def main():
    with tf.Session() as sess:
        sess.run(x)

time_this(main)
