from typing import List
from flask import Flask, render_template, redirect
from lxml import etree
import requests


app = Flask(__name__)


def parseXML(xml : str) -> List[dict]:
    """
    Args:
        xml (str): The source link url to retrieve xml files

    Returns: .tif uri in dictionary
        List[dict]:
            {'L': 'L8', 'three_d_1': '001', 'three_d_2': '003', 'img': '...', \
            'img_file': '...TIF'}
    """
    response = requests.get(xml)
    response_trunkated = response.text
    root = etree.fromstring(bytes(response_trunkated, encoding='utf-8'))

    tif_list = []
    # iterate over the context (i.e. the **lxml.etree.iterparse object**) and \
    # extract the tag elements.
    # From http://python101.pythonlibrary.org/_sources/chapter31_lxml.txt
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = 'None'
            else:
                text = elem.text
            key = 'Key'
            file_ending = 'TIF'
            if key in elem.tag and text[-3:] == file_ending:
                url_item = text.split('/')
                url_item_dic = dict(L=url_item[0], three_d_1=url_item[1], \
                                    three_d_2=url_item[2], img=url_item[3], \
                                    img_file=url_item[4])
                tif_list.append(url_item_dic)
    return tif_list


@app.route('/')
def read_item():
    """

    Returns:
        List[dict]: list of dictionaries to the templates/item.html
            {'L': 'L8', 'three_d_1': '001', 'three_d_2': '003', 'img': '...', \
            'img_file': '...TIF'}
    """
    ids = parseXML('https://landsat-pds.s3.amazonaws.com/')
    return render_template('item.html', ids=ids)
