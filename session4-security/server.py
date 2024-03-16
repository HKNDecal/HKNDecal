from __future__ import print_function

import logging
import json
import os
import socket
import sqlite3

from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import urlparse, parse_qs

CONTENT_TYPE_MAP = {
    '.js': 'application/javascript',
    '.html': 'text/html',
    '.css': 'text/css',
    '': 'text/plain'
}
PORT = 1050
CONN = sqlite3.connect('db.sql3')
CURSOR = CONN.cursor()

class MyTCPServer(TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # logging.getLogger().setLevel(logging_level)
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        # logging.info('received {}'.format(parsed.path))
        parsed_lst = parsed.path.split('/')
        # print("parsed list:", parsed_lst)
        # logging.info('parsed lst {}'.format(parsed_lst))

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
                self.wfile.write(bytes(f.read(), encoding='utf-8'))

        # or this could be an api call
        elif parsed_lst[1] == 'api':

            # returning list of current todo items
            if parsed_lst[2] == 'todos':
                todo_list = [row[0] for row in CURSOR.execute('SELECT * FROM todos')]
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(todo_list), encoding='utf-8'))


            # inserting into database
            elif parsed_lst[2] == 'todos_insert':
                if 'name' not in query or len(query['name']) != 1:
                    self.send_response(500)
                    return
                todo_item_name = query['name'][0]
                self.send_response(200)
                sql = f"""INSERT INTO todos VALUES('{todo_item_name}')"""
                # logging.info("Executing {}".format(sql))
                CURSOR.executescript(sql)
                CONN.commit()

            # removing from database
            elif parsed_lst[2] == 'todos_delete':
                if 'name' not in query or len(query['name']) != 1:
                    self.send_response(500)
                    return
                todo_item_name = query['name'][0]
                self.send_response(200)
                sql = f"""DELETE FROM todos WHERE items = '{todo_item_name}'"""
                # logging.info("Executing {}".format(sql))
                CURSOR.executescript(sql)  # <-- this will be the source of the sql injection (use %3B for semicolon)
                CONN.commit()
            else:
                self.send_response(404)
        else:
            self.send_response(404)

def main() -> None:
    # logging_level = logging.CRITICAL
    # logging_level = logging.INFO
    # logging.disable()
    logging.getLogger().setLevel(logging.WARNING)

    httpd = MyTCPServer(('0.0.0.0', PORT), MyHandler)
    # logging.info('Serving SQL Injection Demo at http://localhost:{}'.format(PORT))
    print(f"Serving SQL Injection Demo at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except Exception:
        pass
    # logging.info('Terminating Server')
    print('Terminating Server')
    httpd.server_close()

if __name__ == "__main__":
    main()