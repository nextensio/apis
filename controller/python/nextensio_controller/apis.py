import sys
import requests
import time
import json
import os

def doGet(url):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.get(url)
    else:
        return requests.get(url, verify=cert)

def doPost(url, data):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.post(url, json=data)
    else:
        return requests.post(url, json=data, verify=cert)

def is_controller_up(url):
    try:
        ret = doGet(url+"getalltenants")
        return (ret.status_code == 200)
    except:
        pass
        return False


def do_post(url, data, suffix):
    try:
        ret = doPost(url+suffix, data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_gateway(url, data):
    return do_post(url, data, "addgateway")

def create_tenant(url, data):
    return do_post(url, data, "addtenant")


def get_tenants(url):
    try:
        ret = doGet(url+"getalltenants")
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])


def create_user(url, data):
    return do_post(url, data, "adduser")

def create_bundle(url, data):
    return do_post(url, data, "addbundle")
    
def create_user_attr(url, data):
    return do_post(url, data, "adduserattr")
 
def create_bundle_attr(url, data):
    return do_post(url, data, "addbundleattr")
 
def create_host_attr(url, data):
    return do_post(url, data, "addhostattr")
 
def create_userext_attr(url, data):
    return do_post(url, data, "adduserextattr")

def create_policy(url, tenant, pid, policy):
    rego = []
    for p in policy:
        rego.append(ord(p))
    data = {'tenant': tenant, 'pid': pid, 'rego': rego}
    return do_post(url, data, "addpolicy")


def create_route(url, data):
    return do_post(url, data, "addroute")


def create_cert(url, cert):
    data = {'certid': 'CACert', 'cert': [ord(c) for c in cert]}
    return do_post(url, data, "addcert")
