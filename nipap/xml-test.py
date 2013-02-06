#!/usr/bin/python
# coding: utf-8

import xmlrpclib

import optparse
import time
import sys

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest='port', type='int', default='1337', help="TCP port")
parser.add_option('-U', '--user')
parser.add_option('-P', '--password')

(options, args) = parser.parse_args()

cred = ''
if options.user and options.password:
	cred = options.user + ':' + options.password + '@'

server_url = 'http://%(cred)s127.0.0.1:%(port)d/XMLRPC' % { 'port': options.port, 'cred': cred }
server = xmlrpclib.Server(server_url, allow_none=1);

ad = { 'authoritative_source': 'nipap' }

#res = server.smart_search_prefix({ 'auth': ad, 'query_string': 'test1', 'search_options': { 'include_all_parents': True } })
#res = server.smart_search_prefix({ 'auth': ad, 'query_string': 'test1', 'search_options': { 'include_all_parents': True, 'root_prefix': '1.0.4.0/24' } })
res = server.smart_search_prefix({ 'auth': ad, 'query_string': 'THISWILLNEVERMATCH', 'search_options': { 'include_all_parents': True, 'parent_prefix': 11963 } })
#res = server.smart_search_prefix({ 'auth': ad, 'query_string': 'test1', 'search_options': { 'include_all_parents': True, 'parent_prefix': 'bajs' } })

for p in res['result']:
    print "".join(" " for i in xrange(p['indent'])), p['prefix'], p['match']

#res = server.list_pool({ 'auth': ad, 'pool': { 'id': 1003 } })
print res

sys.exit(0)

remove_query = {
		'auth': {
			'authoritative_source': 'kll'
			},
		'schema': {
			'id': 1
			}
		}
#server.remove_schema(remove_query)
#print server.list_vrf({ 'auth': ad })
#sys.exit(0)
#print server.add_vrf({ 'auth': { 'authoritative_source': 'kll' },
#        'attr': {
#            'vrf': '1257:124',
#            'name': 'test2',
#            'description': 'my test VRF'
#            }
#        }
#    )
#print server.list_vrf({ 'auth': ad, 'vrf': {} })
#print server.add_prefix({ 'auth': ad, 'attr': {
#            'prefix': '1.0.0.0/24',
#            'type': 'assignment',
#            'description': 'test'
#        }
#    })
#
#print "All VRFs:"
#res = server.list_prefix({ 'auth': ad })
#for p in res:
#    print "%10s %s" % (p['vrf_name'], p['prefix'])
#
#print "VRF: test2"
#res = server.list_prefix({ 'auth': ad,
#        'prefix': {
#            'vrf': '1257:124'
#            }
#        })
#for p in res:
#    print "%10s %s" % (p['vrf_name'], p['prefix'])

#t0 = time.time()
#import sys
#ss = u'ballong'
#print "Type of search string:", type(ss)
#print ss
#res = server.search_schema({ 'operator': 'regex_match', 'val1': 'name', 'val2': 'test' }, { 'max_result': 500 })
a = {
        'auth': {
            'authoritative_source': 'kll'
            },
        'query_string': 'test',
        'search_options': {
            'include_all_parents': True,
            'root_prefix': '1.3.0.0/16'
            }
        }
res = server.smart_search_prefix(a)
for p in res['result']:
    print p['vrf_rt'], p['display_prefix'], p['description'], p['match']
#res = server.smart_search_prefix('test', { 'root_prefix': '1.3.0.0/8', 'max_result': 500 })
#t1 = time.time()
#d1 = t1-t0
#print "Timing:", d1
#print res

#
# echo test
#
#print "try the echo function without args"
#args = {}
#print "ARGS:", args
#print "RESULT:", server.echo()
#print ""
#
#print "try the echo function with a message argument"
#args = { 'message': 'Please reply to me, Obi-Wan Kenobi, you are my only hope!' }
#print "ARGS:", args
#print "RESULT:", server.echo( args )
#print ""


#
# try list function
#
#print "try the list prefix function with a node argument"
#args = { 'node': 'kst5-core-3' }
#print "ARGS:", args
#print "RESULT:", server.list_prefix( args )
#print ""



