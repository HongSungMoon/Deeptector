from __future__ import print_function

import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint as pp
import csv
import os
import time

preX = [[[0,-0.037,0.8147035,-3.552,-0.005,0.705768,-2.3591,1.148,0.538314,-1.212,10.775,0.3617025,1.1785,-0.002,0.11380845,-1.151,1.162,0.670742,-3.562,0.012,0.3666155,-4.814,3.551,0.6062425,-1.2018,3.579,0.241942,0,0,0,0,0,0,-3.57,0.002,0.2873505,0,0,0,0,0,0,1.189,-0.0067,0.846563,0.031,1.1287,0.8717845,0.0197,2.383,0.841135,1.141,7.146,0.290964],
[-2.414,0.033,0.8256995,-1,1.184,0.716718,-2.4103,0.055,0.5487135,-5.9469,4.773,0.340277,-2.4087,0.002,0.1653165,-7.177,1.198,0.6569285,-4.784,1.174,0.400587,-2.408,2.415,0.597198,-2.3991,2.402,0.242817,0,0,0,0,0,0,-3.611,5.968,0.29974,0,0,0,0,0,0,-1.588,0.0264,0.865485,-4.8,0.0067,0.846817,-3.1574,1.216,0.8458895,-7.135,0.016,0.319628],
[-8.327,-2.409,0.860735,-2,-1.235,0.7201685,-5.9588,-1.218,0.554389,-1.253,10,0.3623525,-11.9543,0.012,0.219245,-1.258,-2.397,0.657444,-1.254,-2.397,0.4371645,-4.784,-3.589,0.609458,-2.3931,-28.711,0.207149,0,0,0,0,0,0,-3.576,-21.516,0.291115,0,0,0,0,0,0,-7.182,-2.4298,0.8470985,-4.836,-5.8862,0.819326,-2.4463,-1.191,0.851066,-4.792,-2.383,0.2585275],
[-1.255,-1.204,0.884803,-2.394,0.006,0.712393,-1.2244,0.02,0.5548975,-1.149,10,0.4243855,-2.3658,0.009,0.2441305,-1.165,-1.168,0.671485,-5.92,1.191,0.4377235,-4.753,-1.194,0.6213625,-3.6095,10.763,0.1839405,0,0,0,0,0,0,-2.394,-1.19,0.2683505,0,0,0,0,0,0,-3.546,-4.7236,0.8237155,-4.72,-2.3599,0.8196175,-3.5536,1.134,0.833764,-4.753,-1.203,0.2124485],
[-20.327,-8.314,0.8868755,-1.194,-1.172,0.722799,-0.0292,-2.405,0.5405425,8.335,-1.202,0.5034915,-8.4073,19.128,0.4307525,-1.185,-1.164,0.6760155,2.364,-2.388,0.4778815,-19.149,34.665,0.6525065,8.3963,21.542,0.1926585,0,0,0,0,0,0,2.411,25.104,0.259032,0,0,0,0,0,0,-23.934,-2.4985,0.8321,-14.344,-7.2196,0.8413935,-11.9634,-3.534,0.8223105,-4.753,-1.203,0.2124485],
[-9.595,-0.092,0.890247,1.188,0.003,0.7172385,0.0137,1.179,0.5247815,7.2063,13.179,0.5538385,2.3851,31.153,0.621743,2.336,1.139,0.679265,-1.196,2.409,0.54434,-8.354,29.965,0.642467,1.1896,11.956,0.1731375,0,0,0,0,0,0,1.152,4.8,0.2691415,0,0,0,0,0,0,-9.592,-3.522,0.808976,-8.37,-1.188,0.850064,-4.793,-2.374,0.8248065,0,0,0],
[-8.384,-3.558,0.8709615,-1.191,0.006,0.7069075,-2.3825,-3.571,0.509954,9.5699,-9.557,0.542362,-3.5733,55.007,0.587814,-1.128,2.414,0.6786815,-9.543,9.556,0.6115925,-20.301,47.834,0.64473,-4.7812,-26.315,0.1653075,0,0,0,0,0,0,-4.777,-14.362,0.260834,0,0,0,0,0,0,-9.565,-4.773,0.8331265,-2.836,-1.245,0.8008825,-8.301,-0.028,0.823479,0,0,0],
[-14.308,-3.579,0.825358,-9.59,1.215,0.713427,-10.7616,5.965,0.528586,-13.1777,-0.049,0.5830555,-7.1529,66.986,0.615375,-8.399,2.364,0.6669535,-10.764,1.194,0.634625,0.001,35.833,0.7086985,-3.5672,10.759,0.216386,0,0,0,0,0,0,0.003,2.396,0.237819,0,0,0,0,0,0,-14.341,-1.218,0.88392,-14.345,-2.375,0.78249,-15.922,-1.164,0.8366085,0,0,0],
[-13.114,-2.349,0.834371,-10.731,-0.055,0.7275395,-14.349,-0.03,0.559988,-13.1477,0.003,0.617187,-11.9619,20.274,0.6588435,-8.356,-5.929,0.658843,-3.576,-1.189,0.6330035,-0.103,3.601,0.7651625,-1.2095,7.178,0.2495755,0,0,0,0,0,0,-2.401,2.384,0.225457,0,0,0,0,0,0,-5.772,-1.179,0.8719715,-9.576,-0.032,0.663838,-10.785,-1.166,0.8591585,0,0,0],
[-20.416,-2.481,0.8581575,-19.165,-2.39,0.705496,-25.1124,0.029,0.565454,-33.4649,16.749,0.553778,-44.2418,21.599,0.669919,-11.967,-6.023,0.6483965,-17.943,-5.99,0.680154,-8.316,5.955,0.777144,-19.139,1.2,0.235573,0,0,0,0,0,0,-14.337,1.201,0.231726,0,0,0,0,0,0,-20.295,-5.967,0.840153,-20.32,-7.148,0.3590135,-26.342,-1.272,0.8711435,0,0,0],
[-27.477,-8.289,0.868306,-20.339,-7.16,0.6326795,-38.271,-5.96,0.554486,-75.3892,4.799,0.3338605,-74.205,19.123,0.6256335,-9.607,-5.983,0.5531695,-20.371,3.604,0.674484,-5.99,1.247,0.780122,-27.508,-19.137,0.19527,0,0,0,0,0,0,-21.546,-26.324,0.2129765,0,0,0,0,0,0,-28.73,-4.819,0.8271935,-17.541,-2.383,0.1959435,-31.109,-7.108,0.85871,0,0,0],
[-28.766,-4.822,0.8537665,-27.507,8.346,0.517184,-47.864,-2.381,0.530485,-100.46,23.911,0.2812035,-80.136,10.759,0.5908395,1.214,13.192,0.359861,-20.371,3.604,0.674484,-5.99,1.247,0.780122,-34.698,-3.592,0.147324,0,0,0,0,0,0,-17.922,3.588,0.1614545,0,0,0,0,0,0,-29.94,-6,0.849287,-29.912,-9.532,0.193274,-35.856,-2.438,0.8624425,0,0,0],
[-31.063,-13.142,0.8416555,-32.285,3.626,0.450884,-40.823,5.957,0.462677,-122.032,50.245,0.447592,-131.544,16.778,0.590668,-10.773,15.514,0.273132,0,0,0,0,0,0,-15.561,17.95,0.1193775,0,0,0,0,0,0,7.154,17.94,0.11909905,0,0,0,0,0,0,-37.025,-2.953,0.8535335,-29.912,-9.532,0.193274,-39.497,-9.595,0.8974665,0,0,0],
[-9.609,-8.368,0.856827,-8.415,0.025,0.5080005,-10.739,-1.18,0.4382725,-17.949,19.134,0.513675,-63.418,-0.058,0.6103685,-1.19,-2.39,0.3756205,0,0,0,0,0,0,-28.704,11.964,0.12051,0,0,0,0,0,0,16.758,21.533,0.0793377,0,0,0,0,0,0,-10.781,-8.323,0.8567995,0,0,0,-11.976,-8.313,0.9039045,0,0,0],
[-13.113,-3.659,0.8229135,-10.755,-3.636,0.5597025,-10.307,-3.572,0.4949325,-20.333,1.212,0.5977755,-20.355,-9.589,0.739648,3.584,-9.585,0.4479595,0,0,0,0,0,0,4.778,-16.754,0.1391995,0,0,0,0,0,0,31.093,-16.745,0.0804362,0,0,0,0,0,0,-10.792,-8.438,0.858712,0,0,0,-10.733,-8.417,0.9057,0,0,0],
[-7.163,-8.302,0.8335965,-7.147,-3.569,0.5769225,-7.194,-2.382,0.514294,-0.005,-10.74,0.637246,-4.8,-8.345,0.788328,-2.388,-4.733,0.479688,-20.371,3.604,0.674484,-5.99,1.247,0.780122,-13.137,-7.183,0.16546,0,0,0,0,0,0,-0.01,-4.784,0.12790105,0,0,0,0,0,0,-8.396,-9.121,0.820541,0,0,0,-4.535,-2.373,0.921046,0,0,0]]]

pre_data = np.array(preX, dtype=np.float32)

tf.set_random_seed(777)  # reproducibility

num_classes = 16
input_dim = 54  # data_size
hidden_size = 2  # output from the LSTM
batch_size = 1   # one sentence
sequence_length = 16  # |ihello| == 6
learning_rate = 0.1

X = tf.placeholder(tf.float32, [None, sequence_length, input_dim])  # X one-hot
Y = tf.placeholder(tf.int32, [None, num_classes])  # Y label

# Make a lstm cell with hidden_size (each unit output vector size)
def lstm_cell():
    cell = rnn.BasicLSTMCell(hidden_size, state_is_tuple=True)
    return cell

#cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
#initial_state = cell.zero_state(batch_size, tf.float32)
#outputs, _states = tf.nn.dynamic_rnn(cell, X, initial_state=initial_state, dtype=tf.float32)

multi_cells = rnn.MultiRNNCell([lstm_cell() for _ in range(3)], state_is_tuple=True)
outputs, _states = tf.nn.dynamic_rnn(multi_cells, X, dtype=tf.float32)

X_for_fc = tf.reshape(outputs, [-1, hidden_size])
outputs = tf.contrib.layers.fully_connected(X_for_fc, num_classes, activation_fn=None)

# reshape out for sequence_loss
outputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])

weights = tf.ones([batch_size, sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(
    logits=outputs, targets=Y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

#prediction
prediction = tf.argmax(outputs, 1)

init = tf.global_variables_initializer()

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
sess = tf.Session(config=config)

hello = open('data_hello.csv', 'r')
#with tf.Session(config=config) as sess:
#	sess.run(tf.global_variables_initializer())
#	for i in range(2000):
#		if i % 2 == 1 :
#			l, _ = sess.run([loss, train], feed_dict={X: x1_data, Y: y1_data})
#			result = sess.run(prediction, feed_dict={X: x1_data})
#			print(i, "loss:", l, "Prediction:", result)
#		else :
#			l, _ = sess.run([loss, train], feed_dict={X: x2_data, Y: y2_data})
#			result = sess.run(prediction, feed_dict={X: x2_data})
#			print(i, "loss:", l, "Prediction:", result)
#	
#	result = sess.run(prediction, feed_dict={X: pre_data})
#	print("Training End - Prediction X :", result)
#	result = sess.run(prediction, feed_dict={X: pre_data2})
#	print("Training End - Prediction Y :", result)

def python_init():
	config = tf.ConfigProto()
	config.gpu_options.per_process_gpu_memory_fraction = 0.3
	global sess
	sess.run(init)

	saver = tf.train.Saver()
	saver.restore(sess, os.getcwd() + "/model.ckpt")
	print(os.getcwd() + "/model.ckpt")

'''def action_classification(arg):
	data = np.array(arg, dtype=np.float)
	print(data)
	data = data.reshape(1, 16, 54)
	global sess
	global prediction
	global pre_data
	#predict_output = sess.run(prediction, feed_dict={X: data})
	#print("Prediction:", predict_output)
	return predict_output'''

def action_classification(arg):
	print("enter")
	global sess
	global prediction
	dataX = [[[0 for rows in range(54)]for cols in range(16)]]
	line = arg.split(',')
	linetodata = list(line)
	c = 0
	for a in range(16):
		for b in range(54):
			dataX[0][a][b] = linetodata[c]
			c = c + 1
	data = np.array(dataX, dtype=np.float32)
	predict_output = sess.run(prediction, feed_dict={X: data})
	print("Prediction:", predict_output)
	return predict_outputs


#def action_classification(arg):
#	print("Enter")
#	global sess
#	global prediction
#        
#	dataX = [[[0 for rows in range(54)]for cols in range(16)]]
#	c = 0;
#	strline = hello.readline()
#	line = strline.split(',')
#	linetodata = list(line)
#	print(linetodata)
#	for a in range(16):
#		for b in range(54):
#			dataX[0][a][b] = linetodata[c]
#			c = c + 1
#	data = np.array(dataX, dtype=np.float32)
#	predict_output = sess.run(prediction, feed_dict={X: pre_data})
#	print("Prediction:", predict_output)
#	return predict_output

def python_close():
	global sess
	sess.close()

#python_init()
#action_classification()
#python_close()

#pp.pprint(dataX)

#pp.pprint(tf.shape(x_data))

#cell = rnn.BasicLSTMCell(num_units=2, state_is_tuple=True)
#outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)
#sess = tf.InteractiveSession()
#sess.run(tf.global_variables_initializer())
#pp.pprint(outputs.eval())
