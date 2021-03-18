############################################################################
# Copyright (c) 2018, Johan Mabille, Sylvain Corlay and Loic Gouarin       #
#                                                                          #
# Distributed under the terms of the BSD 3-Clause License.                 #
#                                                                          #
# The full license is in the file LICENSE, distributed with this software. #
############################################################################
import sys

from six.moves import urllib

from xml.etree import ElementTree, cElementTree
from xml.dom import minidom

from sphinx.util.inventory import InventoryFile
from sphinx.builders.html import INVENTORY_FILENAME

def get_sphinx_inventory(url):
    """
    get the sphinx inventory from a url.

    Parameters
    ----------

    url : url of the package where find objects.inv file

    Returns
    -------
    
    the inventory : dict

    """
    inventory_url = urllib.parse.urljoin(url, INVENTORY_FILENAME)
    f = urllib.request.urlopen(inventory_url)
    inventory = InventoryFile.load(f, url, urllib.parse.urljoin)
    f.close()
    return inventory


def extract_tag(inventory, url):
    """
    extract data from sphinx inventory. 
    
    The extracted datas come from a C++ project 
    documented using Breathe. The structure of the inventory 
    is a dictionary with the following keys

    - cpp:class (class names)
    - cpp:function (functions or class methods)
    - cpp:type (type names)

    each value of this dictionary is again a dictionary with

    - key : the name of the element
    - value : a tuple where the third index is the url to the corresponding documentation

    Parameters
    ----------

    inventory : dict
                sphinx inventory

    url : url of the documentation

    Returns
    -------

    dictionary with keys class, class_methods, func, type
    but now the class methods are with their class.
    """
    classes = {}
    class_methods = {}
    functions = {}
    types = {}

    get_relative_url = lambda x: x[2].replace(url, '')

    for c, v in inventory.get('cpp:class', {}).items():
        classes[c] = get_relative_url(v)
        class_methods[c] = {}

    for method, v in inventory.get('cpp:function', {}).items():
        found = False
        for c in class_methods.keys():
            find = c + '::'
            if find in method:
                class_methods[c][method.replace(find, '')] = get_relative_url(v)
                found = True
                break
        if not found:
            functions[method] = get_relative_url(v)

    for typename, v in inventory.get('cpp:type', {}).items():
        types[typename] = get_relative_url(v)

    return {'class': classes, 
            'class_methods': class_methods, 
            'func':functions, 
            'type': types
            }


def write_tagfile(tag_elem, package, url):
    """
    write the doxygen tagfile (package.tag).

    Parameters
    ----------

    tag_elem : dictionary given by extract_tag

    package : name of the package

    url : url of the documentation

    """
    root = ElementTree.Element('tagfile')
    ElementTree.SubElement(root, 'url').text = url

    for k, v in tag_elem['class'].items():
        classname = ElementTree.SubElement(root, 'compound', kind="class")
        ElementTree.SubElement(classname, 'name').text = k    
        ElementTree.SubElement(classname, 'filename').text = v
        for kk, vv in tag_elem['class_methods'][k].items():
            methodname = ElementTree.SubElement(classname, 'member', kind="function")
            ElementTree.SubElement(methodname, 'name').text = kk
            ElementTree.SubElement(methodname, 'anchorfile').text = vv

    for k, v in tag_elem['func'].items():
        methodname = ElementTree.SubElement(root, 'member', kind="function")
        ElementTree.SubElement(methodname, 'name').text = k
        ElementTree.SubElement(methodname, 'anchorfile').text = v

    for k, v in tag_elem['type'].items():
        methodname = ElementTree.SubElement(root, 'member', kind="function")
        ElementTree.SubElement(methodname, 'name').text = k
        ElementTree.SubElement(methodname, 'anchorfile').text = v

    tree = cElementTree.ElementTree(root)
    t = minidom.parseString(ElementTree.tostring(root)).toprettyxml()
    tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))
    tree1.write(package + ".tag", encoding='utf-8', xml_declaration=True)
