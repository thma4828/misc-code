"""
#CON NUERAL NETS
creates a moving window over your image that is looking for a feature out of a window of nxn pixels or do something
then it is going to classify that region of the image as something. 
break down the image by pixels, now lets start at a 3x3 convolution, we will start with a 3x3 window, now we can shift that window!
some windows have overlap, some dont!. Once we have reached the edge, we might move down, left, right. etc. 
(so if we have a 6x6 matrix, there are 3 convolutions such that we are not skipping any pixels!)
#CONVOLUTION creates new regions of screen ([][], such as this! now these regions might have values in them
                                            [][])
([1][3][5], 
 [2][6][1]
 [1][1][0]) <----this is a feauture map. So now we are going to POOL
 #POOLING
 when we pool we are going to do something a little different than creating feature map. We take a 2x2 pool out of the grid. [1][3]
                                                                                                                             [2][6]
 then we find the max value in the pool (6). shift over two, max val in pool is 3, max val in pool is 1 after next shift etc.
 #CONVOLUTION+POOLING == hidden layer of Nueral Network.
 fully connected nuerons, are also connected to outputs to choose from, 
we take our input data + convolutions + pooling(hidden layer) + fully connected layer --->OUTPUT
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

hm_epochs = 1
n_classes = 10
batch_size = 16

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

keep_rate = 0.7
keep_prob = tf.placeholder(tf.float32)

def conv2D(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')
    
def maxpool2D(x):       #   size of window,     movement of window, no padding,,,
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

def convo_nueral_net(x): #5x5 convolution takes 1 in puts 32 out.
    print('--convolutional nueral net prediction has begun--')
    weights = {'W_conv1':tf.Variable(tf.random_normal([5,5,1,32])),
               'W_conv2':tf.Variable(tf.random_normal([5,5,32,64])),
                #fully connected layer
               'W_fc':tf.Variable(tf.random_normal([7*7*64,512])),
               'out':tf.Variable(tf.random_normal([512, n_classes]))}

    biases = {'b_conv1':tf.Variable(tf.random_normal([32])),
              'b_conv2':tf.Variable(tf.random_normal([64])),
                #fully connected layer
              'b_fc':tf.Variable(tf.random_normal([512])),
              'out':tf.Variable(tf.random_normal([n_classes]))}
              
    #matrix operations to reshape our 728 pixel image to a flat 28x28          
    x = tf.reshape(x, shape=[-1,28,28,1])
    print('     x reshaped')
    
    conv1 = tf.nn.relu(conv2D(x, weights['W_conv1']) + biases['b_conv1'])
    conv1 = maxpool2D(conv1)
    
    print('     first layer of convolution complete')
    
    conv2 = tf.nn.relu(conv2D(conv1, weights['W_conv2']) + biases['b_conv2'])
    conv2 = maxpool2D(conv2)
    print('     second layer of convolution complete')
    fc = tf.reshape(conv2, [-1,7*7*64])
    fc = tf.nn.relu(tf.matmul(fc, weights['W_fc']) + biases['b_fc']) 
    fc = tf.nn.dropout(fc, keep_rate)
    print('     through final layer')
    
    output = tf.matmul(fc, weights['out']) + biases['out']
    print('     returning output')
    
    return output

def train_neural_network(x):
    print('training init')
    prediction = convo_nueral_net(x)
    # OLD VERSION:
    #cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )
    # NEW:
    print('calc: cost, optimizer')
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    
    
    with tf.Session() as sess:
        # OLD:
        #sess.run(tf.initialize_all_variables())
        # NEW:
        print('CALLING SESS.RUN PLEASE WAIT!')
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c

            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_neural_network(x)