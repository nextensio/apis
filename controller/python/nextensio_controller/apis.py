import sys
import requests
import time
import json
import os

def doGet(url):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.get(url)
    else
        return requests.get(url, verify=cert)

def doPost(url, data):
    cert = os.getenv('NEXTENSIO_CERT') 
    if cert == None:
        return requests.post(url, json=data)
    else
        return requests.post(url, json=data, verify=cert)

def is_controller_up(url):
    try:
        ret = doGet(url+"getalltenants")
        return (ret.status_code == 200)
    except:
        pass
        return False


def create_gateway(url, gw):
    data = {'name': gw}
    try:
        ret = doPost(url+"addgateway", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_tenant(url, name, gws, domains, image, pods):
    data = {'curid': 'unknown', 'name': name, 'gateways': gws,
            'domains': domains, 'image': image, 'pods': pods}
    try:
        ret = doPost(url+"addtenant", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def get_tenants(url):
    try:
        ret = doGet(url+"getalltenants")
        if ret.status_code != 200:
            return False, json.dumps([])
        return True, ret.json()
    except:
        pass
        return False, json.dumps([])


def create_user(url, uid, tenant, name, email, services, gateway, pod):
    data = {'uid': uid, 'tenant': tenant, 'name': name, 'email': email,
            'services': services, 'gateway': gateway, 'pod': pod}
    try:
        ret = doPost(url+"adduser", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_bundle(url, bid, tenant, name, services, gateway, pod):
    data = {'bid': bid, 'tenant': tenant, 'name': name,
            'services': services, 'gateway': gateway, 'pod': pod}
    try:
        ret = doPost(url+"addbundle", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_user_attr(url, uid, tenant, category, type, level, dept, team):
    data = {'uid': uid, 'tenant': tenant, 'category': category, 'type': type, 'level': level,
            'dept': dept, 'team': team}
    try:
        ret = doPost(url+"adduserattr", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_bundle_attr(url, bid, tenant, dept, team, IC, manager, nonemployee):
    data = {'bid': bid, 'tenant': tenant, 'IC': IC, 'manager': manager,
            'nonemployee': nonemployee, 'dept': dept, 'team': team}
    try:
        ret = doPost(url+"addbundleattr", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_policy(url, tenant, pid, policy):
    rego = []
    for p in policy:
        rego.append(ord(p))
    data = {'tenant': tenant, 'pid': pid, 'rego': rego}
    try:
        ret = doPost(url+"addpolicy", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_route(url, tenant, user, route, tag):
    data = {'tenant': tenant, 'route': user + ":" + route, 'tag': tag}
    try:
        ret = doPost(url+"addroute", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False


def create_cert(url, cert):
    data = {'certid': 'CACert', 'cert': [ord(c) for c in cert]}
    try:
        ret = doPost(url+"addcert", data)
        if ret.status_code != 200 or ret.json()['Result'] != "ok":
            return False
        return True
    except:
        pass
        return False
