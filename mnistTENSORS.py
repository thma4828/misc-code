from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#one hop vector is a vector with 0, and 1's (Binary)
#importing tensorflow
import tensorflow as tf
#creating a vector for x that is 784 long and completely empty
x = tf.placeholder(tf.float32, [None, 784])
#10 outputs possible for 0-9
#W is a vector for weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
#no data in yet just setup
#soft max just standardizes info
y = tf.nn.softmax(tf.matmul(x, W) + b)
#This allows for us to check our data into the system to the actual output
#"checking our work" variable
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
#runs 1000 tries
for _ in range(100000):
    if _%100 == 0:
        print("on step... ", _)
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})

#correct the prediction
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_, 1))
#calculate accuracy
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


