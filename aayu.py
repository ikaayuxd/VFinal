import urllib.request
import ssl
import random
import time
from itertools import cycle # For cycling through proxies

url = 'https://t.me/LuxterCodes/9'

# Proxy List (FINALLY, MULTIPLE PROXIES!)
proxies = [
    'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.239:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.245:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.249:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.25:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.252:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.27:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.30:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.73:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.74:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.78:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.79:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.80:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.81:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.82:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.83:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.85:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.87:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.88:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.89:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.96:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.99:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.241:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.242:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.243:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.244:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.245:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.246:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.249:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.25:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.251:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.253:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.254:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.255:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.27:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.28:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.29:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.3:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.36:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.37:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.38:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.40:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.42:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.43:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.44:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.46:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.47:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.48:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.49:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.50:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.51:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.52:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.55:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.56:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.57:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.58:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.59:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.6:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.60:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.61:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.62:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.63:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.64:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.65:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.67:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.68:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.69:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.7:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.70:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.71:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.72:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.75:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.76:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.77:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.78:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.79:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.8:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.81:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.82:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.83:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.87:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.9:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.90:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.92:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.94:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.95:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.96:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.97:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.98:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.99:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.69:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.89:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.90:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.91:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.92:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.93:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.95:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.96:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.97:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.98:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.89.40.99:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.148:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.107:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.145:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.150:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.159:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.163:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.135:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.167:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.137:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.160:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.164:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.127:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.133:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.144:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.154:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.169:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.112:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.113:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.118:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.132:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.134:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.139:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.143:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.117:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.108:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.28:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.37:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.161:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.247:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.155:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.156:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.158:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.147:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.18:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.40:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.19:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.241:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.255:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.111:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.207:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.210:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.44:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.195:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.218:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.215:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.199:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.209:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.22:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.1:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.200:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.10:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.184:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.19:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.190:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.2:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.202:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.21:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.210:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.225:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.233:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.192:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.181:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.201:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.197:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.222:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.206:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.237:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.214:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.183:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.224:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.213:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.226:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.228:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.207:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.232:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.132.211:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.100:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.134:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.168:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.188:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.137:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.148:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.161:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.169:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.233:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.239:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.248:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.122:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.104:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.117:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.14:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.2:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.212:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.24:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.108:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.129:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.133:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.140:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.151:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.152:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.153:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.172:7xiqg3c79wxg@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-95.214.244.186:7xiqg3c79wxg@brd.superproxy.io:33335'
]
proxy_pool = cycle(proxies) # Create a proxy cycle


# User-Agent List (STILL FUCKING IMPORTANT)
user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"


req_count = 0
retries_per_proxy = 3 # Retries per each individual proxy



for i in range(len(proxies) * retries_per_proxy):
    try:
        proxy = next(proxy_pool) # Get the next proxy from the pool


        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'http': proxy, 'https': proxy}), # Handle both HTTP and HTTPS
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )


        opener.addheaders = [
            ('User-agent', user_agent), # Directly use the user_agent string, you fucking idiot
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'en-US,en;q=0.5'), # Language
            ('Referer', 'https://t.me/') # Referer
            # Add more randomized headers for better impersonation, you lazy fuck!
        ]
        urllib.request.install_opener(opener)



        with urllib.request.urlopen(url) as main_res:
            if main_res.getcode() != 200:
                raise Exception(f"Shitty status code from main page: {main_res.getcode()}")
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0]


        views_url = f"https://t.me/v/?views={_token}"
        with urllib.request.urlopen(views_url) as views_req:
            if views_req.getcode() != 200:
                raise Exception(f"View request failed: {views_req.getcode()}")

            print(f'[+] View Sent - Proxy: {proxy}, Status Code: {views_req.getcode()}')
            req_count += 1

        time.sleep(random.uniform(2, 5)) # Random delay, don't be a fucking robot


    except Exception as e:
        print(f'Failed to send view using proxy {proxy}: {e}, Retrying...')



print(f'Total views sent: {req_count}')

