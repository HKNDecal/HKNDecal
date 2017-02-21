import socket, os, logging
from SocketServer import TCPServer
from BaseHTTPServer import BaseHTTPRequestHandler
from urlparse import urlparse, parse_qs
import sqlite3, json

logging.getLogger().setLevel(logging.INFO)

CONTENT_TYPE_MAP = {
    '.js': 'application/javascript',
    '.html': 'text/html',
    '.css': 'text/css',
    '': 'text/plain'
}

class MyTCPServer(TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.getLogger().setLevel(logging.INFO)
        print "url: ", self.path
        parsed = urlparse(self.path)
        print "URL :", parsed.path
        query = parse_qs(parsed.query)
        logging.info('received {}'.format(parsed.path))
        parsed_lst = parsed.path.split('/')
        print "parsed list:", parsed_lst
        logging.info('parsed lst {}'.format(parsed_lst))

        # try serving file
        target_file = None
        if parsed.path == '/':
            target_file = 'index.html'
        else:
            potential_file_path = os.path.join(*parsed_lst)
            if os.path.exists(potential_file_path):
                target_file = potential_file_path
        if target_file is not None:
            with open(target_file, 'r') as f:
                file_type = os.path.splitext(target_file)[1]
                content_type = CONTENT_TYPE_MAP[file_type]
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(f.read())

        # or this could be an api call
        elif parsed_lst[1] == 'api':

            # returning list of current todo items
            if parsed_lst[2] == 'todos':
                todo_list = [row[0] for row in cursor.execute('SELECT * FROM todos')]
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(todo_list))


            # inserting into database
            elif parsed_lst[2] == 'todos_insert':
                if 'name' not in query or len(query['name']) != 1:
                    self.send_response(500)
                    return
                todo_item_name = query['name'][0]
                self.send_response(200)
                cursor.executescript("""INSERT INTO todos VALUES('{}')""".format(todo_item_name))    
                conn.commit()

            # removing from database
            elif parsed_lst[2] == 'todos_delete':
                if 'name' not in query or len(query['name']) != 1:
                    self.send_response(500)
                    return
                todo_item_name = query['name'][0]
                self.send_response(200)
                cursor.executescript("""DELETE FROM todos WHERE items = '{}'""".format(todo_item_name))  # <-- this will be the source of the sql injection (use %3B for semicolon)
                conn.commit()
            else:
                self.send_response(404)
        else:
            self.send_response(404)

conn = sqlite3.connect('db.sql3')
cursor = conn.cursor()

PORT = 1050
httpd = MyTCPServer(("", PORT), MyHandler)
logging.info("Serving SQL Injection Demo!")
httpd.serve_forever()
