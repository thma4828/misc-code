import tensorflow as tf
import nltk
import pylab
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
#mnist is a data set online
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
#number of nodes in hidden layers
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500
#num classes
n_classes = 10
#batch size for testing
batch_size = 100
#height x width
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')
#(input data * weights) + bias. 
def nueral_network_model(data):
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}
                      
    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}
    
    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}
    
    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      'biases':tf.Variable(tf.random_normal([n_classes]))}
                      
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)
    
    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)
    
    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']),  hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)
    
    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']
    
    return output
    
def train_nueral_network(x):
    prediction = nueral_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    hm_epochs = 5
    #this will make is slow as it gets bigger
    with tf.Session() as sess:
        #init all variables is deprec
        sess.run(tf.global_variables_initializer())  
        #this for loop trains the training data to optimize weights
        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict = {x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch ', epoch + 1, ' completed out of ', hm_epochs, ' ||  loss: ', epoch_loss)
        #now run data through our model with optimized weights
        correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        #evaluate the accuracy
        print('Accuracy: ', accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))


train_nueral_network(x)