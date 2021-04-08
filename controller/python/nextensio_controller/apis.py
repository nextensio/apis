import sys
import requests
import time
import json
import os

def doGet(url, path):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.get(url + "/api/v1/" + path)
    else:
        return requests.get(url + "/api/v1/" + path, verify=cert)

def doPost(url, data, path):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.post(url + "/api/v1/" + path, json=data)
    else:
        return requests.post(url + "/api/v1/" + path, json=data, verify=cert)

def is_controller_up(url):
    try:
        ret = doGet(url, "global/get/alltenants")
        return (ret.status_code == 200)
    except:
        pass
        return False


def do_post(url, data, suffix):
    try:
        ret = doPost(url, data, suffix)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_gateway(url, data):
    return do_post(url, data, "global/add/gateway")

def create_tenant(url, data):
    return do_post(url, data, "global/add/tenant")


def get_tenants(url):
    try:
        ret = doGet(url, "global/get/alltenants")
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])


def create_user(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/user" % tenant)

def create_bundle(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/bundle" % tenant)
    
def create_user_attr(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/userattr" % tenant)
 
def create_bundle_attr(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/bundleattr" % tenant)
 
def create_host_attr(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/hostattr" % tenant)
 
def create_userext_attr(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/userextattr" % tenant)

def create_policy(url, tenant, pid, policy):
    rego = []
    for p in policy:
        rego.append(ord(p))
    data = {'pid': pid, 'rego': rego}
    return do_post(url, data, "tenant/%s/add/policy" % tenant)


def create_route(url, tenant, data):
    return do_post(url, data, "tenant/%s/add/route" % tenant)


def create_cert(url, cert):
    data = {'certid': 'CACert', 'cert': [ord(c) for c in cert]}
    return do_post(url, data, "global/add/cert")
