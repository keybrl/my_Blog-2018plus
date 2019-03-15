import requests
import base64
import hmac
from hashlib import sha1, md5
import time
import os
from xml.etree import ElementTree
import re
import json


blog_config_file = 'sync_blog_config.json'
assets_config_file = 'sync_assets_config.json'

class OSSBucket(object):
    content_type_map = {
        '.*': 'application/octet-stream',
        '.001': 'application/x-001',
        '.301': 'application/x-301',
        '.323': 'text/h323',
        '.906': 'application/x-906',
        '.907': 'drawing/907',
        '.a11': 'application/x-a11',
        '.acp': 'audio/x-mei-aac',
        '.ai': 'application/postscript',
        '.aif': 'audio/aiff',
        '.aifc': 'audio/aiff',
        '.aiff': 'audio/aiff',
        '.anv': 'application/x-anv',
        '.asa': 'text/asa',
        '.asf': 'video/x-ms-asf',
        '.asp': 'text/asp',
        '.asx': 'video/x-ms-asf',
        '.au': 'audio/basic',
        '.avi': 'video/avi',
        '.awf': 'application/vnd.adobe.workflow',
        '.biz': 'text/xml',
        '.bmp': 'application/x-bmp',
        '.bot': 'application/x-bot',
        '.c4t': 'application/x-c4t',
        '.c90': 'application/x-c90',
        '.cal': 'application/x-cals',
        '.cat': 'application/vnd.ms-pki.seccat',
        '.cdf': 'application/x-netcdf',
        '.cdr': 'application/x-cdr',
        '.cel': 'application/x-cel',
        '.cer': 'application/x-x509-ca-cert',
        '.cg4': 'application/x-g4',
        '.cgm': 'application/x-cgm',
        '.cit': 'application/x-cit',
        '.class': 'java/*',
        '.cml': 'text/xml',
        '.cmp': 'application/x-cmp',
        '.cmx': 'application/x-cmx',
        '.cot': 'application/x-cot',
        '.crl': 'application/pkix-crl',
        '.crt': 'application/x-x509-ca-cert',
        '.csi': 'application/x-csi',
        '.css': 'text/css',
        '.cut': 'application/x-cut',
        '.dbf': 'application/x-dbf',
        '.dbm': 'application/x-dbm',
        '.dbx': 'application/x-dbx',
        '.dcd': 'text/xml',
        '.dcx': 'application/x-dcx',
        '.der': 'application/x-x509-ca-cert',
        '.dgn': 'application/x-dgn',
        '.dib': 'application/x-dib',
        '.dll': 'application/x-msdownload',
        '.doc': 'application/msword',
        '.dot': 'application/msword',
        '.drw': 'application/x-drw',
        '.dtd': 'text/xml',
        '.dwf': 'Model/vnd.dwf',
        # '.dwf': 'application/x-dwf',
        '.dwg': 'application/x-dwg',
        '.dxb': 'application/x-dxb',
        '.dxf': 'application/x-dxf',
        '.edn': 'application/vnd.adobe.edn',
        '.emf': 'application/x-emf',
        '.eml': 'message/rfc822',
        '.ent': 'text/xml',
        '.epi': 'application/x-epi',
        '.eps': 'application/x-ps',
        # '.eps': 'application/postscript',
        '.etd': 'application/x-ebx',
        '.exe': 'application/x-msdownload',
        '.fax': 'image/fax',
        '.fdf': 'application/vnd.fdf',
        '.fif': 'application/fractals',
        '.fo': 'text/xml',
        '.frm': 'application/x-frm',
        '.g4': 'application/x-g4',
        '.gbr': 'application/x-gbr',
        '.	application/x-': '.gif',
        '.gl2': 'application/x-gl2',
        '.gp4': 'application/x-gp4',
        '.hgl': 'application/x-hgl',
        '.hmr': 'application/x-hmr',
        '.hpg': 'application/x-hpgl',
        '.hpl': 'application/x-hpl',
        '.hqx': 'application/mac-binhex40',
        '.hrf': 'application/x-hrf',
        '.hta': 'application/hta',
        '.htc': 'text/x-component',
        '.htm': 'text/html',
        '.html': 'text/html',
        '.htt': 'text/webviewhtml',
        '.htx': 'text/html',
        '.icb': 'application/x-icb',
        '.ico': 'image/x-icon',
        # '.ico': 'application/x-ico',
        '.iff': 'application/x-iff',
        '.ig4': 'application/x-g4',
        '.igs': 'application/x-igs',
        '.iii': 'application/x-iphone',
        '.img': 'application/x-img',
        '.ins': 'application/x-internet-signup',
        '.isp': 'application/x-internet-signup',
        '.IVF': 'video/x-ivf',
        '.java': 'java/*',
        '.jfif': 'image/jpeg',
        '.jpe': 'image/jpeg',
        # '.jpe': 'application/x-jpe',
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpeg',
        # '.jpg': 'application/x-jpg',
        '.js': 'application/x-javascript',
        '.jsp': 'text/html',
        '.la1': 'audio/x-liquid-file',
        '.lar': 'application/x-laplayer-reg',
        '.latex': 'application/x-latex',
        '.lavs': 'audio/x-liquid-secure',
        '.lbm': 'application/x-lbm',
        '.lmsff': 'audio/x-la-lms',
        '.ls': 'application/x-javascript',
        '.ltr': 'application/x-ltr',
        '.m1v': 'video/x-mpeg',
        '.m2v': 'video/x-mpeg',
        '.m3u': 'audio/mpegurl',
        '.m4e': 'video/mpeg4',
        '.mac': 'application/x-mac',
        '.man': 'application/x-troff-man',
        '.math': 'text/xml',
        '.mdb': 'application/msaccess',
        # '.mdb': 'application/x-mdb',
        '.mfp': 'application/x-shockwave-flash',
        '.mht': 'message/rfc822',
        '.mhtml': 'message/rfc822',
        '.mi': 'application/x-mi',
        '.mid': 'audio/mid',
        '.midi': 'audio/mid',
        '.mil': 'application/x-mil',
        '.mml': 'text/xml',
        '.mnd': 'audio/x-musicnet-download',
        '.mns': 'audio/x-musicnet-stream',
        '.mocha': 'application/x-javascript',
        '.movie': 'video/x-sgi-movie',
        '.mp1': 'audio/mp1',
        '.mp2': 'audio/mp2',
        '.mp2v': 'video/mpeg',
        '.mp3': 'audio/mp3',
        '.mp4': 'video/mpeg4',
        '.mpa': 'video/x-mpg',
        '.mpd': 'application/vnd.ms-project',
        '.mpe': 'video/x-mpeg',
        '.mpeg': 'video/mpg',
        '.mpg': 'video/mpg',
        '.mpga': 'audio/rn-mpeg',
        '.mpp': 'application/vnd.ms-project',
        '.mps': 'video/x-mpeg',
        '.mpt': 'application/vnd.ms-project',
        '.mpv': 'video/mpg',
        '.mpv2': 'video/mpeg',
        '.mpw': 'application/vnd.ms-project',
        '.mpx': 'application/vnd.ms-project',
        '.mtx': 'text/xml',
        '.mxp': 'application/x-mmxp',
        '.net': 'image/pnetvue',
        '.nrf': 'application/x-nrf',
        '.nws': 'message/rfc822',
        '.odc': 'text/x-ms-odc',
        '.out': 'application/x-out',
        '.p10': 'application/pkcs10',
        '.p12': 'application/x-pkcs12',
        '.p7b': 'application/x-pkcs7-certificates',
        '.p7c': 'application/pkcs7-mime',
        '.p7m': 'application/pkcs7-mime',
        '.p7r': 'application/x-pkcs7-certreqresp',
        '.p7s': 'application/pkcs7-signature',
        '.pc5': 'application/x-pc5',
        '.pci': 'application/x-pci',
        '.pcl': 'application/x-pcl',
        '.pcx': 'application/x-pcx',
        '.pdf': 'application/pdf',
        '.pdx': 'application/vnd.adobe.pdx',
        '.pfx': 'application/x-pkcs12',
        '.pgl': 'application/x-pgl',
        '.pic': 'application/x-pic',
        '.pko': 'application/vnd.ms-pki.pko',
        '.pl': 'application/x-perl',
        '.plg': 'text/html',
        '.pls': 'audio/scpls',
        '.plt': 'application/x-plt',
        '.png': 'image/png',
        # '.png': 'application/x-png',
        '.pot': 'application/vnd.ms-powerpoint',
        '.ppa': 'application/vnd.ms-powerpoint',
        '.ppm': 'application/x-ppm',
        '.pps': 'application/vnd.ms-powerpoint',
        # '.ppt': 'application/vnd.ms-powerpoint',
        '.ppt': 'application/x-ppt',
        '.pr': 'application/x-pr',
        '.prf': 'application/pics-rules',
        '.prn': 'application/x-prn',
        '.prt': 'application/x-prt',
        '.ps': 'application/x-ps',
        # '.ps': 'application/postscript',
        '.ptn': 'application/x-ptn',
        '.pwz': 'application/vnd.ms-powerpoint',
        '.r3t': 'text/vnd.rn-realtext3d',
        '.ra': 'audio/vnd.rn-realaudio',
        '.ram': 'audio/x-pn-realaudio',
        '.ras': 'application/x-ras',
        '.rat': 'application/rat-file',
        '.rdf': 'text/xml',
        '.rec': 'application/vnd.rn-recording',
        '.red': 'application/x-red',
        '.rgb': 'application/x-rgb',
        '.rjs': 'application/vnd.rn-realsystem-rjs',
        '.rjt': 'application/vnd.rn-realsystem-rjt',
        '.rlc': 'application/x-rlc',
        '.rle': 'application/x-rle',
        '.rm': 'application/vnd.rn-realmedia',
        '.rmf': 'application/vnd.adobe.rmf',
        '.rmi': 'audio/mid',
        '.rmj': 'application/vnd.rn-realsystem-rmj',
        '.rmm': 'audio/x-pn-realaudio',
        '.rmp': 'application/vnd.rn-rn_music_package',
        '.rms': 'application/vnd.rn-realmedia-secure',
        '.rmvb': 'application/vnd.rn-realmedia-vbr',
        '.rmx': 'application/vnd.rn-realsystem-rmx',
        '.rnx': 'application/vnd.rn-realplayer',
        '.rp': 'image/vnd.rn-realpix',
        '.rpm': 'audio/x-pn-realaudio-plugin',
        '.rsml': 'application/vnd.rn-rsml',
        '.rt': 'text/vnd.rn-realtext',
        # '.rtf': 'application/msword',
        '.rtf': 'application/x-rtf',
        '.rv': 'video/vnd.rn-realvideo',
        '.sam': 'application/x-sam',
        '.sat': 'application/x-sat',
        '.sdp': 'application/sdp',
        '.sdw': 'application/x-sdw',
        '.sit': 'application/x-stuffit',
        '.slb': 'application/x-slb',
        '.sld': 'application/x-sld',
        '.slk': 'drawing/x-slk',
        '.smi': 'application/smil',
        '.smil': 'application/smil',
        '.smk': 'application/x-smk',
        '.snd': 'audio/basic',
        '.sol': 'text/plain',
        '.sor': 'text/plain',
        '.spc': 'application/x-pkcs7-certificates',
        '.spl': 'application/futuresplash',
        '.spp': 'text/xml',
        '.ssm': 'application/streamingmedia',
        '.sst': 'application/vnd.ms-pki.certstore',
        '.stl': 'application/vnd.ms-pki.stl',
        '.stm': 'text/html',
        '.sty': 'application/x-sty',
        '.svg': 'text/xml',
        '.swf': 'application/x-shockwave-flash',
        '.tdf': 'application/x-tdf',
        '.tg4': 'application/x-tg4',
        '.tga': 'application/x-tga',
        # '.tif': 'application/x-tif',
        '.tif': 'image/tiff',
        '.tiff': 'image/tiff',
        '.tld': 'text/xml',
        '.top': 'drawing/x-top',
        '.torrent': 'application/x-bittorrent',
        '.tsd': 'text/xml',
        '.txt': 'text/plain',
        '.uin': 'application/x-icq',
        '.uls': 'text/iuls',
        '.vcf': 'text/x-vcard',
        '.vda': 'application/x-vda',
        '.vdx': 'application/vnd.visio',
        '.vml': 'text/xml',
        '.vpg': 'application/x-vpeg005',
        # '.vsd': 'application/vnd.visio',
        '.vsd': 'application/x-vsd',
        '.vss': 'application/vnd.visio',
        # '.vst': 'application/vnd.visio',
        '.vst': 'application/x-vst',
        '.vsw': 'application/vnd.visio',
        '.vsx': 'application/vnd.visio',
        '.vtx': 'application/vnd.visio',
        '.vxml': 'text/xml',
        '.wav': 'audio/wav',
        '.wax': 'audio/x-ms-wax',
        '.wb1': 'application/x-wb1',
        '.wb2': 'application/x-wb2',
        '.wb3': 'application/x-wb3',
        '.wbmp': 'image/vnd.wap.wbmp',
        '.wiz': 'application/msword',
        '.wk3': 'application/x-wk3',
        '.wk4': 'application/x-wk4',
        '.wkq': 'application/x-wkq',
        '.wks': 'application/x-wks',
        '.wm': 'video/x-ms-wm',
        '.wma': 'audio/x-ms-wma',
        '.wmd': 'application/x-ms-wmd',
        '.wmf': 'application/x-wmf',
        '.wml': 'text/vnd.wap.wml',
        '.wmv': 'video/x-ms-wmv',
        '.wmx': 'video/x-ms-wmx',
        '.wmz': 'application/x-ms-wmz',
        '.wp6': 'application/x-wp6',
        '.wpd': 'application/x-wpd',
        '.wpg': 'application/x-wpg',
        '.wpl': 'application/vnd.ms-wpl',
        '.wq1': 'application/x-wq1',
        '.wr1': 'application/x-wr1',
        '.wri': 'application/x-wri',
        '.wrk': 'application/x-wrk',
        '.ws': 'application/x-ws',
        '.ws2': 'application/x-ws',
        '.wsc': 'text/scriptlet',
        '.wsdl': 'text/xml',
        '.wvx': 'video/x-ms-wvx',
        '.xdp': 'application/vnd.adobe.xdp',
        '.xdr': 'text/xml',
        '.xfd': 'application/vnd.adobe.xfd',
        '.xfdf': 'application/vnd.adobe.xfdf',
        '.xhtml': 'text/html',
        # '.xls': 'application/vnd.ms-excel',
        '.xls': 'application/x-xls',
        '.xlw': 'application/x-xlw',
        '.xml': 'text/xml',
        '.xpl': 'audio/scpls',
        '.xq': 'text/xml',
        '.xql': 'text/xml',
        '.xquery': 'text/xml',
        '.xsd': 'text/xml',
        '.xsl': 'text/xml',
        '.xslt': 'text/xml',
        '.xwd': 'application/x-xwd',
        '.x_b': 'application/x-x_b',
        '.sis': 'application/vnd.symbian.install',
        '.sisx': 'application/vnd.symbian.install',
        '.x_t': 'application/x-x_t',
        '.ipa': 'application/vnd.iphone',
        '.apk': 'application/vnd.android.package-archive',
        '.xap': 'application/x-silverlight-app',
    }
    filename_ext = re.compile(r'(\.[^.]+?)$')

    def __init__(self, host, bucket, access_key_id, access_key_secret):
        self.host = host
        self.bucket = bucket
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret

    def make_auth(self, auth_info: dict) -> str:
        verb = auth_info.get('verb')
        content_md5 = auth_info.get('content-md5') if auth_info.get('content-md5') else ''
        content_type = auth_info.get('content-type') if auth_info.get('content-type') else ''
        date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        canonicalized_oss_headers = \
            auth_info.get('canonicalized_oss_headers') if auth_info.get('canonicalized_oss_headers') else ''
        canonicalized_resource = \
            auth_info.get('canonicalized_resource') if \
            auth_info.get('canonicalized_resource') else '/' + self.bucket + '/'

        signature = base64.b64encode(
            hmac.new(
                self.access_key_secret.encode(),
                (
                    verb + '\n' +
                    content_md5 + '\n' +
                    content_type + '\n' +
                    date + '\n' +
                    canonicalized_oss_headers +
                    canonicalized_resource
                ).encode(),
                sha1
            ).digest()
        ).decode()

        return 'OSS {ak_id}:{signature}'.format(ak_id=self.access_key_id, signature=signature)

    def list_object(self) -> list:
        objs = []
        marker = None

        while True:
            headers = {
                'Host': self.host,
                'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()),
                'Authorization': self.make_auth({
                    'verb': 'GET',
                })
            }
            res = requests.get(
                'https://' + self.host + '/{marker}'.format(marker=('?marker=' + marker) if marker else ''),
                headers=headers
            )
            etree = ElementTree.fromstring(res.text)
            for content in etree.findall('Contents'):
                objs.append((content.find('Key').text, content.find('ETag').text[1:-1]))

            marker = etree.findall('NextMarker')
            if marker:
                marker = marker[0].text
            else:
                break

        return objs

    def put_object(self, obj_name: str, data: bytes) -> str:
        # 检索Content-Type
        ext = OSSBucket.filename_ext.findall(obj_name)
        content_type = None
        if ext:
            content_type = OSSBucket.content_type_map.get(ext[0])
        if content_type is None:
            content_type = 'application/octet-stream'

        # 计算Content-MD5
        content_md5 = base64.b64encode(md5(data).digest()).decode()

        headers = {
            'Host': self.host,
            'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()),
            'Content-Type': content_type,
            'Content-MD5': content_md5,
            'Content-Disposition': 'inline',
            'Authorization': self.make_auth({
                'verb': 'PUT',
                'content-md5': content_md5,
                'content-type': content_type,
                'canonicalized_resource': '/' + self.bucket + '/' + obj_name
            })
        }
        res = requests.put('https://' + self.host + '/' + obj_name, data=data, headers=headers)
        return 'OK  ' if res.status_code == 200 else 'Fail'

    def get_object(self, obj_name: str) -> bytes:
        headers = {
            'Host': self.host,
            'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()),
            'Authorization': self.make_auth({
                'verb': 'GET',
                'canonicalized_resource': '/' + self.bucket + '/' + obj_name
            })
        }
        res = requests.get('https://' + self.host + '/' + obj_name, headers=headers)
        return res.content

    def del_object(self, obj_name: str) -> str:
        headers = {
            'Host': self.host,
            'Date': time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()),
            'Authorization': self.make_auth({
                'verb': 'DELETE',
                'canonicalized_resource': '/' + self.bucket + '/' + obj_name
            })
        }
        res = requests.delete('https://' + self.host + '/' + obj_name, headers=headers)
        return 'OK  ' if res.status_code == 204 else 'Fail'


class FileManager(object):
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def list_file(self) -> list:
        root = self.root_dir
        if root[-1] in ['/', '\\']:
            root = root[:-1]

        root_len = len(self.root_dir) + 1
        res = []
        for path in os.walk(root):
            if path[2]:
                for file in path[2]:
                    res.append((path[0].replace('\\', '/') + '/' + file)[root_len:])
        return res

    def read_file(self, file_name: str) -> bytes:
        with open(os.path.join(self.root_dir, file_name), 'rb') as file:
            data = file.read()
        return data

    def write_file(self, file_name: str, data: bytes):
        path = os.path.join(self.root_dir, file_name)
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        with open(path, 'wb') as file:
            file.write(data)

    def del_file(self, file_name: str):
        path = os.path.join(self.root_dir, file_name)
        if os.path.isfile(path):
            os.remove(path)

    def clear_empty_folder(self):
        for path in os.walk(self.root_dir, False):
            if path[0] == self.root_dir:
                continue
            if not path[1] and not path[2]:
                os.rmdir(path[0])


class OSSSynchronizer(object):
    def __init__(self, local_dir: FileManager, oss_bucket: OSSBucket):
        self.local_dir = local_dir
        self.oss_bucket = oss_bucket

    # 检查同步情况
    def sync_checking(self) -> list:
        file_list = self.local_dir.list_file()
        obj_list = self.oss_bucket.list_object()

        # 将(文件名, ETag)二元组列表转为键值映射字典
        obj_map = dict()
        for obj in obj_list:
            obj_map[obj[0]] = obj[1]

        # 同步列表，三元组(文件名, 是否在本地, ETag)的列表
        sync_list = []

        # 从本地文件列表更新同步列表
        for file in file_list:
            sync_list.append((file, True, obj_map.get(file)))
            if obj_map.get(file):
                obj_map.pop(file)

        # 从OSS对象字典更新同步列表
        for obj, etag in obj_map.items():
            sync_list.append((obj, False, etag))

        return sync_list

    # 从本地同步到OSS
    def sync_from_local_to_oss(self):
        sync_list = self.sync_checking()

        # 进行同步
        for thing in sync_list:
            if thing[1]:  # 文件在本地
                if thing[2] is not None:  # 本地和OSS各有一份
                    data = self.local_dir.read_file(thing[0])
                    file_md5 = md5(data).hexdigest().upper()
                    if file_md5 != thing[2]:  # 内容不一致，上传本地文件到OSS
                        res = self.oss_bucket.put_object(thing[0], data)
                        print('{status} [M] {filename}'.format(status=res, filename=thing[0]))
                else:  # 文件不在OSS，上传本地文件到OSS
                    data = self.local_dir.read_file(thing[0])
                    res = self.oss_bucket.put_object(thing[0], data)
                    print('{status} [+] {filename}'.format(status=res, filename=thing[0]))
            else:  # 文件不在本地，删除OSS上的对应对象
                res = self.oss_bucket.del_object(thing[0])
                print('{status} [-] {filename}'.format(status=res, filename=thing[0]))

    # 从OSS同步到本地
    def sync_from_oss_to_local(self):
        sync_list = self.sync_checking()

        # 进行同步
        for thing in sync_list:
            if thing[1]:  # 文件在本地
                if thing[2] is not None:  # 本地和OSS各有一份
                    data = self.local_dir.read_file(thing[0])
                    file_md5 = md5(data).hexdigest().upper()
                    if file_md5 != thing[2]:  # 内容不一致，下载OSS对应文件
                        res = self.oss_bucket.get_object(thing[0])
                        if res:
                            self.local_dir.write_file(thing[0], res)
                        print('{status} [M] {filename}'.format(status='OK  ' if res else 'Fail', filename=thing[0]))
                else:  # 文件不在OSS，删除本地文件
                    self.local_dir.del_file(thing[0])
                    print('{status} [-] {filename}'.format(status='OK  ', filename=thing[0]))
            else:  # 文件不在本地，下载OSS上的对应对象
                res = self.oss_bucket.get_object(thing[0])
                if res:
                    self.local_dir.write_file(thing[0], res)
                print('{status} [+] {filename}'.format(status='OK  ' if res else 'Fail', filename=thing[0]))

        # 清理空文件夹
        self.local_dir.clear_empty_folder()


if __name__ == '__main__':
    # 同步博客
    with open(blog_config_file, 'r', encoding='utf-8') as fp:
        config = json.load(fp)

    oss = OSSBucket(
        config['oss']['host'],
        config['oss']['bucket'],
        config['oss']['access_key_id'],
        config['oss']['access_key_secret']
    )
    local = FileManager(config['local_dir'])
    oss_synchronizer = OSSSynchronizer(local, oss)
    oss_synchronizer.sync_from_local_to_oss()

    # 同步静态文件
    with open(assets_config_file, 'r', encoding='utf-8') as fp:
        config = json.load(fp)

    oss = OSSBucket(
        config['oss']['host'],
        config['oss']['bucket'],
        config['oss']['access_key_id'],
        config['oss']['access_key_secret']
    )
    local = FileManager(config['local_dir'])
    oss_synchronizer = OSSSynchronizer(local, oss)
    oss_synchronizer.sync_from_local_to_oss()
