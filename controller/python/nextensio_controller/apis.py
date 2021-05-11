import sys
import requests
import time
import json
import os

def doGet(url, path, token):
    headers = {'Authorization': "Bearer %s" % token}
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.get(url + "/api/v1/" + path, headers=headers)
    else:
        return requests.get(url + "/api/v1/" + path, verify=cert, headers=headers)

def doPost(url, data, path, token):
    headers = {'Authorization': "Bearer %s" % token}
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.post(url + "/api/v1/" + path, json=data, headers=headers)
    else:
        return requests.post(url + "/api/v1/" + path, json=data, verify=cert, headers=headers)

def is_controller_up(url, token):
    try:
        ret = doGet(url, "global/get/alltenants", token)
        return (ret.status_code == 200)
    except:
        pass
        return False


def do_post(url, data, suffix, token):
    try:
        ret = doPost(url, data, suffix, token)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_gateway(url, data, token):
    return do_post(url, data, "global/add/gateway", token)

def create_tenant(url, data, token):
    return do_post(url, data, "global/add/tenant", token)

def get_tenants(url, token):
    try:
        ret = doGet(url, "global/get/alltenants", token)
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])


def create_tenant_cluster(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/tenantcluster" % tenant, token)

def create_attrset(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/attrset" % tenant, token)

def create_user(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/user" % tenant, token)

def create_bundle(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/bundle" % tenant, token)
    
def create_user_attr(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/userattr" % tenant, token)
 
def create_bundle_attr(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/bundleattr" % tenant, token)
 
def create_host_attr(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/hostattr" % tenant, token)
 
def create_userext_attr(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/userextattr" % tenant, token)

def create_policy(url, tenant, pid, policy, token):
    rego = []
    for p in policy:
        rego.append(ord(p))
    data = {'pid': pid, 'rego': rego}
    return do_post(url, data, "tenant/%s/add/policy" % tenant, token)


def create_route(url, tenant, data, token):
    return do_post(url, data, "tenant/%s/add/route" % tenant, token)


def create_cert(url, cert, token):
    data = {'certid': 'CACert', 'cert': [ord(c) for c in cert]}
    return do_post(url, data, "global/add/cert", token)
