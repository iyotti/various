import numpy as np
import matplotlib.pyplot as plt
'''
def hist():
	mu, sigma = 100, 15
	x = mu+sigma*np.random.randn(10000)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	ax.hist(x, bins=50)
	ax.set_title('first histogram $\mu=100,\ \sigma=15$')
	ax.set_xlabel('x')
	ax.set_ylabel('freq')
	fig.show()
'''

def hist(mu, sigma):
	x = mu + sigma * np.random.randn(10000)
	plt.hist(x , bins=50, normed=True)
	plt.title("quality_Histgram")
	plt.xlabel('quality')
	plt.ylabel('count')
	plt.show()

#hist(1000,15)

def w_hist(mu1,sigma1,mu2,sigma2):
	x1 = mu1+sigma1*np.random.randn(10000)
	x2 = mu2+sigma2*np.random.randn(10000)

	plt.hist(x1 , bins=50, normed=True, color='red')
	plt.hist(x2 , bins=50, normed=True, color='blue')
	plt.title("quality_Histgram")
	plt.xlabel('quality')
	plt.ylabel('count')
	plt.show()

w_hist(100,15,70,6)