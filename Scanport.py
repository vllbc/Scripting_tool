
import time
import socket
import threading


class scanThread(threading.Thread):
	def __init__(self, ip, port_min=0, port_max=65535):
		threading.Thread.__init__(self)
		assert isinstance(port_max, int) and isinstance(port_min, int)
		self.ip = ip
		self.port_min = max(0, port_min)
		self.port_max = min(65535, port_max)

	def run(self):
		return self.__checker()
	def __checker(self):
		for port in range(self.port_min, self.port_max+1):
			self.__connect(port)
	def __connect(self, port):
		socket.setdefaulttimeout(1)
		s = socket.socket()
		try:
			t_start = time.time()
			s.connect((self.ip, port))
			t_end = time.time()
			flag = True
		except:
			flag = False
		s.close()
		if flag:
			info = f'Find --> [IP]: {self.ip}, [PORT]: {port}, [Connect Time]: {(t_end-t_start)*1000}'
			print(info)
			self.__save(info)
		return flag
	# 保存结果
	def __save(self, content):
		if content:
			try:
				with open('results.txt', 'a') as f:
					f.write(content + '\n')
			except:
				time.sleep(0.1)


if __name__ == '__main__':
	ip = input('输入IP>>>\n')
	port_min = input('输入最小端口(默认为0)\n')
	try:
		port_min = int(port_min)
	except:
		print('[Warning]: 发生错误,调整为最小端口值')
		port_min = 0
	port_max = input('输入最大端口(最大为65535)\n')
	try:
		port_max = int(port_max)
	except:
		print('[Warning]: 发生错误,调整为最大端口值')
		port_max = 65535
	# 一个线程负责扫描num个端口
	num = 8
	interval = (port_max - port_min) // num
	for i in range(interval):
		scanThread(ip, i * num, (i + 1) * num).start()