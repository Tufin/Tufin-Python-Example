import requests, sys, base64, collections


# global vars
server_ip = '127.0.0.1'
headers = {}
user = 'admin'
password = 'tufin123'
debug = False

def http_post(url, data, headers=headers):

        try:
                r = requests.post(url=url, headers=headers, data=data, verify=False)
        except requests.exceptions.RequestException as e:
                print >> sys.stderr, e
                return

        if debug:
                print r.text

        http_result = collections.namedtuple('HTTP_Result', ['status', 'text'])
        return http_result(r.status_code, r.text)


def http_get(url, headers=headers):

        try:
                r = requests.get(url=url, headers=headers, verify=False)
        except requests.exceptions.RequestException as e:
                print >> sys.stderr, e
                return

        if debug:
                print r.text

        http_result = collections.namedtuple('HTTP_Result', ['status', 'text'])
        return http_result(r.status_code, r.text)


def main(argv):
        headers['Accept'] = 'application/xml'
        headers['Authorization'] = 'Basic ' + base64.b64encode(user + ':' + password)


        r = http_get('https://127.0.0.1/securetrack/api/devices/')
        if r.status != 200:
                print >> sys.stderr, "Failed to get devices"
                print >> sys.stderr, "Status: ", r.status
                return -1

        print r.text


if  __name__ =='__main__':
    main(sys.argv[1:])
