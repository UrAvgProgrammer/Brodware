from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from urllib.request import urlopen

chrome_path = r"D:\Work\Brodware\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

#get the list of vendor code to search
vendor_codes = pd.read_excel('Product_data.xlsx', sheet_name='GP')
vendor_codes = vendor_codes['Vendor Code']

#website name
link = "https://brodware.com"
#pdf folder
pdf_folder = r"D:\Work\Brodware\pdf"

def main():
	#To go to home page
	driver.get(link)
	driver.implicitly_wait(15)

	for vendor_code in vendor_codes:

		#simulate searching
		search_field = driver.find_element_by_xpath("""//*[@id="searchform"]/input""")
		search_field.send_keys(vendor_code)
		search_field.send_keys(Keys.ENTER)
		driver.implicitly_wait(15)

		try:
			#to simulate click to go to product info
			product_info = driver.find_element_by_xpath("""//article/div/div[2]/div/div[2]/h2/a""")
			product_info.click()
			driver.implicitly_wait(15)
			#logging
			with open("logs.csv", "a") as f:
				f.write('{}, Success\n'.format(vendor_code))
			print('{}, Success'.format(vendor_code))

			try:
				#saving pdfs
				pdf_link = driver.find_element_by_xpath("""//a[contains(@href, "/files/pdf/")]""")
				pdf_urls = []
				#if not "maintenance" in pdf_link:
				pdf_urls.append(pdf_link.get_attribute("href"))
				extract_pdf_from_page(pdf_urls, link)
			except Exception as e:
				print(e)

		except:
			#logging
			with open("logs.csv", "a") as f:
				f.write('{}, Failed\n'.format(vendor_code))
			print('{}, Failed'.format(vendor_code))


def extract_pdf_from_page(pdf_links, website):
	for links in pdf_links:
		if links.endswith('.pdf'):
			link = fix_url(links, website)
			response = urlopen(link)
			path = link.split('/')[-1]
			#saving pdf
			with open("%s/%s" % (pdf_folder, path), 'wb') as f:
				f.write(response.read())

def fix_url(link, website):
	if link[0] == "/":
		link = ''.join(website) + ''.join(link)
	elif not "http" in link:
		link = ''.join(website) + ''.join(link)
	return link

if __name__ == "__main__":
	main()
