from __future__ import print_function

import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint as pp
import csv
import matplotlib.pyplot as plt

tf.set_random_seed(777)  # reproducibility
num_classes = 1
input_dim = 54  # data_size
hidden_size = 128  # output from the LSTM
batch_size = 1   # one sentence
sequence_length = 16  # |ihello| == 6
learning_rate = 0.001

dataY = [[[1]],[[2]],[[3]],[[4]],[[5]],[[6]],[[7]]]

y1_data = np.array(dataY[0], dtype=np.float32)
y2_data = np.array(dataY[1], dtype=np.float32)
y3_data = np.array(dataY[2], dtype=np.float32)
y4_data = np.array(dataY[3], dtype=np.float32)
y5_data = np.array(dataY[4], dtype=np.float32)
y6_data = np.array(dataY[5], dtype=np.float32)
y7_data = np.array(dataY[6], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, sequence_length, input_dim])  # X one-hot
Y = tf.placeholder(tf.float32, [None, 1])  # Y label

def lstm_cell():
    cell = rnn.BasicLSTMCell(hidden_size, state_is_tuple=True)
    return cell

multi_cells = rnn.MultiRNNCell([lstm_cell() for _ in range(3)], state_is_tuple=True)
outputs, _states = tf.nn.dynamic_rnn(multi_cells, X, dtype=tf.float32)

Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], num_classes, activation_fn=None)

# cost/loss
loss = tf.reduce_sum(tf.square(Y_pred - Y))
# optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

# RMSE
targets = tf.placeholder(tf.float32, [None, 1])
prediction = tf.placeholder(tf.float32, [None, 1])
rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - prediction)))

with tf.Session() as sess:
	saver = tf.train.Saver()
	sess.run(tf.global_variables_initializer())
	count = 0
	for i in range(10):
		test_l = open('data_punch_l.csv', 'r')
		test_r = open('data_punch_r.csv', 'r')
		test_l2 = open('data_punch_l2.csv', 'r')
		test_r2 = open('data_punch_r2.csv', 'r')
		hold = open('data_hold.csv', 'r')
		hello = open('data_hello.csv', 'r')
		clap = open('data_clap.csv', 'r')
		j=0
		dataX = [[[0 for rows in range(54)]for cols in range(16)]]
#		helloreader = csv.reader(hello)
#		clapreader = csv.reader(clap)
#		holdreader = csv.reader(hold)
		for j in range(1 * 7 * 189) :# 데이터세트 개수
			if j % 7 == 0 :
				strline = test_l.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y1_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data})
				
				print(test_predict)
			elif j % 7 == 1 :
				strline = test_r.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y2_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data}) # 예측 결과 
				
				print(test_predict)
			elif j % 7 == 2 :
				strline = test_l2.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y3_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data}) # 예측 결과 
			
				print(test_predict)
			elif j % 7 == 3 :
				strline = test_r2.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y4_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data}) # 예측 결과 
			
				print(test_predict)
			elif j % 7 == 4 :
				strline = hold.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y5_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data})
			
				print(test_predict)
			elif j % 7 == 5 :
				strline = hello.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y6_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data})
			
				print(test_predict)
			elif j % 7 == 6 :
				strline = clap.readline()
				line = strline.split(',')
				linetodata = list(line)
				c = 0;
				for a in range(16):
					for b in range(54):
						dataX[0][a][b] = linetodata[c]
						c = c + 1
				x1_data = np.array(dataX, dtype=np.float32)
				_, step_loss = sess.run([train, loss], feed_dict={X: x1_data, Y: y7_data})
				count = count + 1
				print("[step: {}] loss: {}".format(i, step_loss))
				test_predict = sess.run(Y_pred, feed_dict={X: x1_data})
			
				print(test_predict)

	saver = tf.train.Saver()
	saver.save(sess, 'model2.ckpt')

#			line = helloreader.readline()
#			linetodata = list(line)
#			c = 0;
#			for a in range(16):
#				for b in range(54):
#					dataX[0][a][b] = linetodata[c]
#					c = c + 1
#			x1_data = np.array(dataX, dtype=np.float32)
#			l, _ = sess.run([loss, train], feed_dict={X: x1_data, Y: y1_data})
#			result = sess.run(prediction, feed_dict={X: x1_data})
#			count = count + 1
#			print(i, count, "loss:", l, "Prediction:", result)
#			else :
#				l, _ = sess.run([loss, train], feed_dict={X: x2_data, Y: y2_data})
#				result = sess.run(prediction, feed_dict={X: x2_data})
#				print(i, "loss:", l, "Prediction:", result)
	
#	result = sess.run(prediction, feed_dict={X: pre_data})
#	print("Training End - Prediction X :", result)
#	result = sess.run(prediction, feed_dict={X: pre_data2})
#	print("Training End - Prediction Y :", result)

#pp.pprint(dataX)

#pp.pprint(tf.shape(x_data))

#cell = rnn.BasicLSTMCell(num_units=2, state_is_tuple=True)
#outputs, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)
#sess = tf.InteractiveSession()
#sess.run(tf.global_variables_initializer())
#pp.pprint(outputs.eval())
