import socketio

sio = socketio.Client(logger=False, engineio_logger=False)
@sio.event
def my_message(data):
    print(f"I received the following message {data}")

@sio.event
def connect():
    print("I am connected")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('handshake')
def on_message(data):
    print('HandShake', data)
    #sio.emit('status', {'get': 'systemStatus'})
    #sio.emit('query:history', {"date":"2022-01-01T00:00:00.000Z","type":"Month"})

@sio.on('response:query:history')
def on_message(data):
    price_list.append(data)


price_list = []

sio.connect('http://192.168.1.187:80')

date_list = ["2022-01-01T00:00:00.000Z", "2022-02-01T00:00:00.000Z", "2022-03-01T00:00:00.000Z", "2022-04-01T00:00:00.000Z"]
for date in date_list:
    sio.emit('query:history', {"date":date,"type":"Month"})
sio.sleep(3)
sio.disconnect()
print(price_list)



#["query:history",{"date":"2022-01-01T00:00:00.000Z","type":"Month"}]