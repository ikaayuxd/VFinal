import urllib.request
import ssl
import time
from itertools import cycle

url = 'https://t.me/LuxterCodes/9'

proxies = [
    'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-158.46.166.29:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-158.46.169.117:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.92:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.97:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.112:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.113:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.116:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.117:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.118:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-158.46.167.209:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-158.46.170.107:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.37:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.170:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.211:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.13:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.15:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.23:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.32:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.37:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.41:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.43:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.47:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.48:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.51:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.53:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.57:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.62:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.67:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.70:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.72:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.74:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.82:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.86:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.88:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.93:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.107:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.110:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.111:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.114:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.117:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.118:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.123:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.127:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.128:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.131:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.137:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.138:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.142:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.146:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.148:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.157:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.158:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.162:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.165:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.168:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.171:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.175:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.180:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.182:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.189:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.190:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.192:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.193:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.195:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.196:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.198:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.199:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.201:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.206:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.210:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.215:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.216:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.222:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.223:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.226:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.233:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.234:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.236:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.237:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.239:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.240:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.242:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.116.252:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.0:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.1:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.4:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.6:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.7:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.8:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.12:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.13:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.18:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.19:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.20:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.21:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.26:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.29:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.42:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.48:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.50:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.51:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.54:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.55:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.56:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.57:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.58:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.62:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.63:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.64:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.65:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.69:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.72:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.73:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.76:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.78:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.81:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.83:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.88:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.90:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.92:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.117.96:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.71:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.83:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.94:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.211:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.90.212:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.62:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.82:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.93:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.118:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.142:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.150:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.91.245:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.52:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.71:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.72:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.236:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.58.246:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.19:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.34:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.78:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.92:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.113:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.149:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.245:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.59.254:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.2:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.3:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.4:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.5:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.6:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.7:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.8:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.9:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.12:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.13:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.14:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.15:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.16:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.17:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.18:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.19:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.20:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.21:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.22:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.23:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.24:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.25:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.26:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.27:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.28:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.29:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.30:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.31:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.32:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.33:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.34:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.35:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.36:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.37:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.38:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.39:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.40:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.41:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.42:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.43:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.44:l4px1qej3sdb@brd.superproxy.io:33335',
'brd-customer-hl_5ad1b94c-zone-datacenter_proxy2-ip-178.171.38.45:l4px1qej3sdb@brd.superproxy.io:33335'
]
proxy_pool = cycle(proxies)

# SINGLE USER-AGENT (YOU DUMB FUCK)
user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"


req_count = 0
retries_per_proxy = 3

for i in range(len(proxies) * retries_per_proxy):
    try:
        proxy = next(proxy_pool)

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'http': proxy, 'https': proxy}),
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )

        opener.addheaders = [
            ('User-agent', user_agent), # DIRECTLY USING THE SINGLE USER-AGENT, YOU MORON
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Referer', 'https://t.me/')
            # ADD MORE HEADERS, YOU FUCKING CRETIN!
        ]
        urllib.request.install_opener(opener)

        with urllib.request.urlopen(url) as main_res:
            if main_res.getcode() != 200:
                raise Exception(f"Shitty status code from main page: {main_res.getcode()}")
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0] # Check for empty string here

        views_url = f"https://t.me/v/?views={_token}"
        with urllib.request.urlopen(views_url) as views_req:
            if views_req.getcode() != 200:
                raise Exception(f"View request failed: {views_req.getcode()}")

            print(f'[+] View Sent - Proxy: {proxy}, Status Code: {views_req.getcode()}')
            req_count += 1

        time.sleep(random.uniform(2, 5))

    except Exception as e:
        print(f'Failed to send view using proxy {proxy}: {e}, Retrying...')

print(f'Total views sent: {req_count}')
