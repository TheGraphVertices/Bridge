# https://www.youtube.com/watch?v=9pn1KKhxwdM
# web server to receive json post requests from the esp32
# https://www.youtube.com/watch?v=kogOfxg1c_g&t=158s
# https://www.youtube.com/watch?v=dgvLegLW6ek
# https://www.youtube.com/watch?v=jKZ8XJwckSg


import flask, 

def main():
  PORT = 8000
  server = HTTPServer(('', PORT), helloHandler)
  print(f'server running on port {PORT}')
  server.serve_forever()

if __name__ == '__main__':
  main()