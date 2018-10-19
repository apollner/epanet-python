

#
#  test_toolkit.py
#   
#  Created:    October 19, 2018
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#  

import pytest

#from epanet.toolkit 
import toolkit as entk

from data import INPUT_FILE_NET_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST


def test_createdelete():
    _handle = entk.createproject()
    assert(_handle != None)
    
    _handle = entk.deleteproject(_handle)
    assert(_handle == None)
    

def test_run():
    _handle = entk.createproject()
    entk.runproject(_handle, INPUT_FILE_NET_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST, None)
    entk.deleteproject(_handle)    
    

def test_openclose():
    _handle = entk.createproject()
    entk.open(_handle, INPUT_FILE_NET_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    entk.close(_handle)
    entk.deleteproject(_handle)


@pytest.fixture()
def handle(request):    
    _handle = entk.createproject()
    entk.open(_handle, INPUT_FILE_NET_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    
    def close():
        entk.close(_handle)
        entk.deleteproject(_handle)
    
    request.addfinalizer(close)    
    return _handle    


def test_getnodeindex(handle):
    index = entk.getnodeindex(handle, "13")
    assert index == 4
    

def test_getnodename(handle):
    id = entk.getnodename(handle, 4)
    assert id == "13"
    

def test_getnodetype(handle):
    type = entk.getnodetype(handle, 4)
    assert type == entk.NodeType.JUNCTION.value
    
    
def test_getnodevalue(handle):
    value = entk.getnodevalue(handle, 4, entk.NodeProperty.ELEVATION)
    assert value == 695.
    
        
def test_hyd_step(handle): 
     entk.openh(handle)
     
     entk.inith(handle, entk.SaveOptions.NOSAVE)
     
     while True:
         time = entk.runh(handle)
         
         step = entk.nexth(handle)
         
         if time == 0.:
             break

     entk.closeh(handle)


    