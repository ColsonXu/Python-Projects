from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=1&c=2016&d=0&e=1&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r"goog.csv"
	fw = open(dest_url, "w")
	for line in lines:
		fw.write(line + "\n")
	fw.close()

download_stock_data(goog_url)
