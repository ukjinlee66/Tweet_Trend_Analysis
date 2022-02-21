import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json

consumer_key='p3yC9Lhr2dbt5l6Izr3pXFsSR'
consumer_secret='EccWuY7mBxZAhfpYVNpL6GeVIATSPb1pK33Y2x9PNt29y0UpYy'
access_token ='998580368-a8MKHoBNFKWmw8ypMgddlcdpc3OzmUkzFMrk7rMH'
access_secret='ZaAvPc02M2W7ARg9jkCYg4RRgnyv23PkwJ6YqTwcJgbHv'

class TweetsListener(StreamListener):  #클라이언트 소켓을 받음
  # tweet object listens for the tweets
  def __init__(self, csocket):
    self.client_socket = csocket    # 클라이언트 소켓을 받는 생성자
  def on_data(self, data):    # 오버라이딩
    try:
      msg = json.loads( data )      # json 문자열을 딕셔너리로 변환
      print("new message")
      # if tweet is longer than 140 characters
      if "extended_tweet" in msg:       # extended_tweet라는 key가 있는지 확인
        # add at the end of each tweet "t_end"
        self.client_socket\
            .send(str(msg['extended_tweet']['full_text']+"t_end")\
            .encode('utf-8'))
        # client_socket에 인코딩 해서 보냄

        print(msg['extended_tweet']['full_text'])
      else:
        # add at the end of each tweet "t_end"
        self.client_socket\
            .send(str(msg['text']+"t_end")\
            .encode('utf-8'))
        #client_socket으로 보냄

        print(msg['text'])
      return True
    except BaseException as e:
        print("Error on_data: %s" % str(e))
    return True
  def on_error(self, status):
    print(status)
    return True

def sendData(c_socket, keyword):
  print('start sending data from Twitter to socket')
  # authentication based on the credentials
  auth = OAuthHandler(consumer_key, consumer_secret)  # 인증
  auth.set_access_token(access_token, access_secret)  # 인증
  # start sending data from the Streaming API
  twitter_stream = Stream(auth, TweetsListener(c_socket))  # stream 객체 생성
  twitter_stream.filter(track = keyword, locations=[124, 33, 130, 38], languages=["ko"])  # stream을 연결하고 실행

if __name__ == "__main__":
    # server (local machine) creates listening socket
    s = socket.socket()         # socket 객체 생성
    host = "127.0.0.1"            # localhost
    port = 5555                 # port 5555
    s.bind((host, port))         # socket binding , 소켓을 특정 네트워크 인터페이스와 포트번호에 연결하는데 사용한다.
    print('socket is ready')
    # server (local machine) listens for connections
    s.listen(4)                 # 서버가 클라이언트의 접속을 허용하도록 한다. 최대 4개를 허용하도록한다.
    print('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
      #연결 허용, c_socket 변수에는 클라이언트 소켓이 저장되고, addr에는 클라이언트 ip 주소가 저장된다.
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    sendData(c_socket, keyword = ['방앗간'])
      #c_socket과 keyword = 'piano'를 sendData함수의 인자로 넣음
