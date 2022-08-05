import sys, os, re
from bs4 import BeautifulSoup

def main():
	# сопоставление относительного и полного пути
	link_replace_dict={
		"../manual.html":"http://aleksversus.narod.ru/index/easy_math_3/0-73",
		"vspomogatelnye_funkcii/0-74.html":"http://aleksversus.narod.ru/index/vspomogatelnye_funkcii/0-74",
		"operacii_s_drobnymi_chislami/0-75.html":"http://aleksversus.narod.ru/index/operacii_s_drobnymi_chislami/0-75",
		"logicheskie_operacii/0-76.html":"http://aleksversus.narod.ru/index/logicheskie_operacii/0-76",
		"operacii_s_tekstom/0-77.html":"http://aleksversus.narod.ru/index/operacii_s_tekstom/0-77",
		"operacii_s_shestnadcaterichnymi_chislami/0-78.html":"http://aleksversus.narod.ru/index/operacii_s_shestnadcaterichnymi_chislami/0-78",
		"operacii_s_massivami/0-79.html#em_arr_insert":"http://aleksversus.narod.ru/index/operacii_s_massivami/0-79#em_arr_insert",
		"operacii_s_massivami/0-79.html#em_arr_chtype":"http://aleksversus.narod.ru/index/operacii_s_massivami/0-79#em_arr_chtype",
		"operacii_s_massivami/0-79.html#em_arr_print":"http://aleksversus.narod.ru/index/operacii_s_massivami/0-79#em_arr_print",
		"operacii_s_massivami/0-79.html#em_fewarrs_print":"http://aleksversus.narod.ru/index/operacii_s_massivami/0-79#em_fewarrs_print",
		"operacii_s_massivami/0-79.html#em_arr_clear":"http://aleksversus.narod.ru/index/operacii_s_massivami/0-79#em_arr_clear",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_randFill":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_randFill",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_strtFill":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_strtFill",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_sort":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_sort",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_restand":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_restand",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_desort":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_desort",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_simpl":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_simpl",
		"operacii_s_massivami_stranica_2/0-80.html#em_arr_find":"http://aleksversus.narod.ru/index/operacii_s_massivami_stranica_2/0-80#em_arr_find",
		"operacii_s_celymi_chislami/0-81.html":"http://aleksversus.narod.ru/index/operacii_s_celymi_chislami/0-81",
		"rabota_s_koordinatnoj_setkoj/0-82.html":"http://aleksversus.narod.ru/index/rabota_s_koordinatnoj_setkoj/0-82",
		"istorija_versij/0-83.html":"http://aleksversus.narod.ru/index/istorija_versij/0-83"
	}
	page_path_list=[
		["..\\..\\[manual]\\easy.math\\istorija_versij\\0-83.html","D:\\my\\projects\\narod.ru\\aleksversus.narod.ru\\pages\\qsp\\Easy Libraries\\easy.math.3"]
	]
	for page_path in page_path_list:
		with open(page_path[0],'r',encoding='utf-8') as file:
			page=file.read()
		export_soup=recombinePage(page,link_replace_dict)

def recombinePage(page,link_replace_dict):
	soup=BeautifulSoup(page,'html.parser')
	soup.head.clear()
	new_tag = soup.new_tag('meta')
	new_tag["http-equiv"]="content-type"
	new_tag["content"]="text/html; charset=UTF-8"
	soup.head.append(new_tag)
	new_tag = soup.new_tag('meta')
	new_tag["name"]="viewport"
	new_tag["content"]="initial-scale=1, maximum-scale=1, user-scalable=no"
	soup.head.append(new_tag)
	new_tag = soup.new_tag('meta')
	new_tag["http-equiv"]="X-UA-Compatible"
	new_tag["content"]="IE=edge"
	soup.head.append(new_tag)
	new_tag = soup.new_tag('meta')
	new_tag["name"]="google-site-verification"
	new_tag["content"]="SVddT4tLZkBJXcutXo9CwHA1jFpb-1bKK0Y7Q1MkN2M"
	soup.head.append(new_tag)
	new_tag = soup.new_tag('title')
	new_tag.string="$MODULE_NAME$ - $SITE_NAME$"
	soup.head.append(new_tag)
	new_tag = soup.new_tag('link')
	new_tag['type']='text/css'
	new_tag['rel']='stylesheet'
	new_tag['href']='/_st/my.css'
	soup.head.append(new_tag)
	new_tag = soup.new_tag('link')
	new_tag['type']='text/css'
	new_tag['rel']='stylesheet'
	new_tag['href']='/css/qsp/qsp.css'
	soup.head.append(new_tag)
	new_tag = soup.new_tag('link')
	new_tag['type']='text/css'
	new_tag['rel']='stylesheet'
	new_tag['href']='/css/qsp/easy.library.css'
	soup.head.append(new_tag)
	new_tag = soup.new_tag('link')
	new_tag['type']='text/css'
	new_tag['rel']='stylesheet'
	new_tag['href']='/offline/window.css'
	soup.head.append(new_tag)
	links_list=soup.find_all('a')
	for link in links_list:
		# перебираем все ссылки на странице
		# нужно сравнить присутсвует ли в текущей ссылке какая-нибудь из составляющих
		for key in link_replace_dict:
			match=re.match(key,link['href'])
			if match!=None:
				print(link['href'].replace(key,link_replace_dict[key]))

if __name__ == '__main__':
	main()