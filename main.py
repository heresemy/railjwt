#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DON'T EDIT
#MADE BY semy
"""
Free Fire Token Extractor API (self‑contained) - OB54 Updated
Usage: http://localhost:8000/semy?access_token=YOUR_ACCESS_TOKEN
"""

import json
import requests
import sys
import random
import time
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from concurrent.futures import ThreadPoolExecutor

# -------------------- Include protobuf generated code --------------------
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

# --- MajorLoginReq protobuf RIZER ---
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginReq.proto\"\xfa\n\n\x0bMajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12\"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12\"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t\"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MajorLoginReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MAJORLOGIN']._serialized_start = 24
  _globals['_MAJORLOGIN']._serialized_end = 1426
  _globals['_GAMESECURITY']._serialized_start = 1428
  _globals['_GAMESECURITY']._serialized_end = 1481
MajorLogin = _globals['MajorLogin']
GameSecurity = _globals['GameSecurity']

# --- MajorLoginRes protobuf (MajoRLoGinrEs_pb2) ---
DESCRIPTOR2 = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginRes.proto\"|\n\rMajorLoginRes\x12\x13\n\x0b\x61\x63\x63ount_uid\x18\x01 \x01(\x04\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0b\n\x03key\x18\x16 \x01(\x0c\x12\n\n\x02iv\x18\x17 \x01(\x0c\x62\x06proto3')
_globals2 = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR2, _globals2)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR2, 'MajorLoginRes_pb2', _globals2)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR2._loaded_options = None
  _globals2['_MAJORLOGINRES']._serialized_start = 23
  _globals2['_MAJORLOGINRES']._serialized_end = 147
MajorLoginRes = _globals2['MajorLoginRes']

# -------------------- End protobuf includes --------------------

# -------------------- Pre-cached Device Data --------------------
# Cache karke rakho taaki har baar generate na karna pade
ANDROID_VERSIONS = [
    "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)",
    "Android OS 10 / API-29 (Q/rel.cjw.20220518.114133)",
    "Android OS 11 / API-30 (RP1A.200720.012/rel.cjw.20220518.114133)",
    "Android OS 12 / API-31 (SP1A.210812.016.C2/rel.cjw.20220518.114133)",
    "Android OS 13 / API-33 (TP1A.220624.014/rel.cjw.20220518.114133)"
]

# Pre-generated device profiles (fast access ke liye)
DEVICE_CACHE = []
for _ in range(20):  # 20 different profiles pre-generate karo
    DEVICE_CACHE.append({
        "system_software": random.choice(ANDROID_VERSIONS),
        "system_hardware": random.choice(["Handheld", "Mobile"]),
        "screen_width": random.choice([1920, 2400, 3200]),
        "screen_height": random.choice([1080, 1440]),
        "screen_dpi": random.choice(["240", "320", "420", "515"]),
        "processor_details": random.choice(["ARMv8-A | 2400 | 8", "ARMv8-A | 2800 | 8", "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4"]),
        "memory": random.choice([4096, 6144, 8192, 12288]),
        "gpu_renderer": random.choice(["Adreno 640", "Adreno 660", "Mali-G78 MP20", "Mali-G78 MP14"]),
        "gpu_version": random.choice(["OpenGL ES 3.2", "OpenGL ES 3.1"]),
        "device_type": "Handheld",
        "cpu_type": random.choice([2, 3]),
        "cpu_architecture": random.choice(["32", "64"]),
        "unique_device_id": f"{random.choice(['Google|', 'Samsung|', 'OnePlus|', 'Xiaomi|', 'Oppo|'])}{random.randint(1000000000000, 9999999999999)}",
        "client_ip": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "library_token": f"{random.randint(1000000000000000000, 9999999999999999999)}|/data/app/com.dts.freefireth-{random.choice(['fpXCSpHIV6dKC7jL-WOyRA==', 'xKDLSpHIV6dKC7jL-WOyRB==', 'yPEMSpHIV6dKC7jL-WOyRC=='])}/base.apk",
        "external_storage_total": random.randint(40000, 60000),
        "external_storage_available": random.randint(30000, 50000),
        "internal_storage_total": random.randint(30000, 50000),
        "internal_storage_available": random.randint(20000, 40000),
        "game_disk_storage_available": random.randint(40000, 60000),
        "game_disk_storage_total": random.randint(20000, 40000),
        "external_sdcard_avail_storage": random.randint(40000, 60000),
        "external_sdcard_total_storage": random.randint(20000, 40000),
        "loading_time": random.randint(30000, 60000),
        "android_engine_init_flag": random.randint(100000, 120000),
        "is_vpn": random.randint(0, 1)
    })

def get_cached_device():
    """Fast device profile from cache (no generation overhead)"""
    return random.choice(DEVICE_CACHE)

# Thread pool for parallel requests
executor = ThreadPoolExecutor(max_workers=10)

def get_garena_token(uid, password):
    url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P4 (Vivo Y15c; Android 12; en;IN;)",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None
    
app = Flask(__name__)

# AES constants (from xC4.py)
AES_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
AES_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

def encrypt_aes(data: bytes) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return cipher.encrypt(pad(data, AES.block_size))

def build_major_login(open_id: str, access_token: str, platform_type: int, device_profile: dict) -> bytes:
    major = MajorLogin()
    
    # Fast assignment - no random generation here
    major.event_time = time.strftime("%Y-%m-%d %H:%M:%S")
    major.game_name = "free fire"
    major.platform_id = 1
    major.client_version = "1.126.1"
    major.system_software = device_profile["system_software"]
    major.system_hardware = device_profile["system_hardware"]
    major.telecom_operator = "MTN/Spacecetal"
    major.network_type = "WIFI"
    major.screen_width = device_profile["screen_width"]
    major.screen_height = device_profile["screen_height"]
    major.screen_dpi = device_profile["screen_dpi"]
    major.processor_details = device_profile["processor_details"]
    major.memory = device_profile["memory"]
    major.gpu_renderer = device_profile["gpu_renderer"]
    major.gpu_version = device_profile["gpu_version"]
    major.unique_device_id = device_profile["unique_device_id"]
    major.client_ip = device_profile["client_ip"]
    major.language = "en"
    major.open_id = open_id
    major.open_id_type = "4"
    major.device_type = device_profile["device_type"]
    major.memory_available.version = 55
    major.memory_available.hidden_value = 81
    major.access_token = access_token
    major.platform_sdk_id = 1
    major.network_operator_a = "MTN/Spacecetal"
    major.network_type_a = "WIFI"
    major.client_using_version = "2019119026"
    major.external_storage_total = device_profile["external_storage_total"]
    major.external_storage_available = device_profile["external_storage_available"]
    major.internal_storage_total = device_profile["internal_storage_total"]
    major.internal_storage_available = device_profile["internal_storage_available"]
    major.game_disk_storage_available = device_profile["game_disk_storage_available"]
    major.game_disk_storage_total = device_profile["game_disk_storage_total"]
    major.external_sdcard_avail_storage = device_profile["external_sdcard_avail_storage"]
    major.external_sdcard_total_storage = device_profile["external_sdcard_total_storage"]
    major.login_by = 3
    major.library_path = "/data/app/com.dts.freefireth-fpXCSpHIV6dKC7jL-WOyRA==/lib/arm"
    major.reg_avatar = 1
    major.library_token = device_profile["library_token"]
    major.channel_type = 3
    major.cpu_type = device_profile["cpu_type"]
    major.cpu_architecture = device_profile["cpu_architecture"]
    major.client_version_code = "2019119026"
    major.graphics_api = "OpenGLES2"
    major.supported_astc_bitset = 16383
    major.login_open_id_type = 4
    major.analytics_detail = b"\x15\x12\x14\x50\x0e\x59\x03\x49\x51\x0e\x46\x09\x00\x11\x58\x43\x39\x5f\x00\x5b\x51\x0f\x68\x5b\x56\x0a\x61\x07\x57\x6d\x0f\x03\x66"
    major.loading_time = device_profile["loading_time"]
    major.release_channel = "android"
    major.extra_info = "KqsHT8W93GdcG3ZozENfFwVHtm7qq1eRUNaIDNgRobozIBtLOiYCc4Y6zvvpcICxzQF2sOE4cbytwLs4xZbRnpRMpmWRQKmeO5vcs8nQYBhwqH7K"
    major.android_engine_init_flag = device_profile["android_engine_init_flag"]
    major.if_push = 1
    major.is_vpn = device_profile["is_vpn"]
    major.origin_platform_type = str(platform_type)
    major.primary_platform_type = str(platform_type)
    return major.SerializeToString()

def try_major_login(open_id: str, access_token: str, platform_type: int):
    # Fast cached device profile
    device_profile = get_cached_device()
    payload = build_major_login(open_id, access_token, platform_type, device_profile)
    encrypted_payload = encrypt_aes(payload)

    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB54"
    }
    try:
        # Faster timeout and keep-alive
        resp = requests.post(url, data=encrypted_payload, headers=headers, verify=False, timeout=5)
        if resp.status_code != 200:
            return None
        major_res = MajorLoginRes()
        major_res.ParseFromString(resp.content)
        if major_res.token:
            return {
                "account_uid": str(major_res.account_uid),
                "region": major_res.region,
                "token": major_res.token,
                "url": major_res.url,
                "timestamp": major_res.timestamp,
                "key": major_res.key.hex(),
                "iv": major_res.iv.hex()
            }
    except Exception as e:
        print(f"MajorLogin error for platform {platform_type}: {e}")
    return None

def decode_jwt(token: str) -> dict:
    import base64
    parts = token.split('.')
    if len(parts) != 3:
        return {}
    try:
        header = json.loads(base64.urlsafe_b64decode(parts[0] + '==').decode())
        payload = json.loads(base64.urlsafe_b64decode(parts[1] + '==').decode())
        return {"header": header, "payload": payload}
    except Exception:
        return {}

@app.route('/semy', methods=['GET'])
def semy_endpoint():
    access_token = request.args.get('access_token')
    uid = request.args.get('uid')
    password = request.args.get('password')

    # Fast token fetch
    if uid and password:
        garena_res = get_garena_token(uid, password)
        if garena_res and 'access_token' in garena_res:
            access_token = garena_res['access_token']
        else:
            return jsonify({"success": False, "error": "Garena Login Failed"}), 401

    if not access_token:
        return jsonify({"error": "Missing access_token or uid/password"}), 400

    # Fast inspect
    inspect_url = f"https://100067.connect.garena.com/oauth/token/inspect?token={access_token}"
    try:
        insp_resp = requests.get(inspect_url, timeout=5)
        if insp_resp.status_code != 200:
            return jsonify({"error": "Failed to inspect token", "status_code": insp_resp.status_code}), 400
        insp_data = insp_resp.json()
        open_id = insp_data.get('open_id')
        if not open_id:
            return jsonify({"error": "open_id not found in inspect response"}), 400
    except Exception as e:
        return jsonify({"error": f"Inspect request failed: {str(e)}"}), 500

    # Try platforms fast
    platform_types = [2, 3, 4, 6, 8]
    for pt in platform_types:
        result = try_major_login(open_id, access_token, pt)
        if result:
            jwt_decoded = decode_jwt(result['token'])
            return jsonify({
                "success": True,
                "platform_type_used": pt,
                "jwt": result['token'],
                "jwt_decoded": jwt_decoded,
                "account_uid": result['account_uid'],
                "region": result['region'],
                "url": result['url'],
                "timestamp": result['timestamp']
            })
    
    return jsonify({
        "success": False,
        "error": "MajorLogin failed. Account may be banned, not registered, or token invalid."
    }), 401

if __name__ == '__main__':
    # Production config for speed
    app.run(host='0.0.0.0', port=8006, debug=False, threaded=True, processes=1)
