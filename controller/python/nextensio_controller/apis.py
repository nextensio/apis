import sys
import requests
import time
import json
import os

def doGet(url, path, token, group):
    headers = {
        'Authorization': "Bearer %s" % token,
        'X-Nextensio-Group': group
    }
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.get(url + "/api/v1/" + path, headers=headers)
    else:
        return requests.get(url + "/api/v1/" + path, verify=cert, headers=headers)

def doPost(url, data, path, token, group):
    headers = {
        'Authorization': "Bearer %s" % token,
        'X-Nextensio-Group': group
    }
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.post(url + "/api/v1/" + path, json=data, headers=headers)
    else:
        return requests.post(url + "/api/v1/" + path, json=data, verify=cert, headers=headers)

def is_controller_up(url, token, group):
    try:
        ret = doGet(url, "global/get/alltenants", token, group)
        return (ret.status_code == 200)
    except:
        pass
        return False


def do_post(url, data, suffix, token, group):
    try:
        ret = doPost(url, data, suffix, token, group)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False

def do_get(url, suffix, token, group):
    try:
        ret = doGet(url, suffix, token, group)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])

def create_gateway(url, data, token, group):
    return do_post(url, data, "global/add/gateway", token, group)

def create_tenant(url, data, token, group):
    return do_post(url, data, "global/add/tenant", token, group)

def get_tenants(url, token, group):
    try:
        ret = doGet(url, "global/get/alltenants", token, group)
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])

def get_onboard_log(url, tenant, uid, token, group):
    try:
        ret = doGet(url, "tenant/%s/get/onboardlog/%s" % (tenant, uid), token, group)
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])

def get_trace_request(url, tenant, traceid, token, group):
    try:
        ret = doGet(url, "tenant/%s/get/tracereq/%s" % (tenant, traceid), token, group)
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])

def get_all_trace_requests(url, tenant, token, group):
    try:
        ret = doGet(url, "tenant/%s/get/alltracereq" % tenant, token, group)
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])


def create_tenant_cluster(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/tenantcluster" % tenant, token, group)

def create_attrset(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/attrset" % tenant, token, group)

def create_user(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/user" % tenant, token, group)

def create_bundle(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/bundle" % tenant, token, group)
    
def create_user_attr(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/userattr" % tenant, token, group)
 
def create_bundle_attr(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/bundleattr" % tenant, token, group)
 
def create_host_attr(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/hostattr" % tenant, token, group)
 
def create_userext_attr(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/userextattr" % tenant, token, group)

def create_trace_request(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/tracereq" % tenant, token, group)

def create_policy(url, tenant, pid, policy, token, group):
    rego = []
    for p in policy:
        rego.append(ord(p))
    data = {'pid': pid, 'rego': rego}
    return do_post(url, data, "tenant/%s/add/policy" % tenant, token, group)


def create_route(url, tenant, data, token, group):
    return do_post(url, data, "tenant/%s/add/route" % tenant, token, group)


def create_cert(url, cert, token, group):
    data = {'certid': 'CACert', 'cert': [ord(c) for c in cert]}
    return do_post(url, data, "global/add/cert", token, group)

def get_bundle_key(url, tenant, bid, token, group):
    ok, bundle = do_get(url, "tenant/%s/get/bundle/%s" % (tenant, bid), token, group)
    if not ok:
        return ""
    return bundle['Bundle']['sharedkey'] 

