import asyncio
import websockets
import sqlite3  
import django
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alumni.settings")
django.setup()
from Home import models

clients=[]
# db=sqlite3.connect('Home/chat.db')
# cursor=db.cursor()
try:
    async def chat_reciever(websocket, path):
        await websocket.send(json.dumps({
            'users':[w.user for w in clients],
            'type':'onlineusers',
            }));
        clients.append(websocket)
        websocket.user=str(await websocket.recv())

        for client in clients:
            if client != websocket:
                await client.send(json.dumps({
            'users':[str(websocket.user)],
            'type':'onlineusers',
            }));
        
        print('---------------- > ',websocket.user,"\n is connected to chat....")
        try:
            while True:
                msg = json.loads(await websocket.recv())
                if msg.get('username') and msg.get('message'):
                    msg['chatid'] = models.chat.objects.create(Username = msg.get('username'), Messege = msg.get('message'))
                    msg['chatid'] = str(msg['chatid'].id)
                    for client in clients:
                        if client != websocket:
                            msg['type'] = 'othermsg'
                        else:
                            msg['type'] = 'minemsg'
                        await client.send(json.dumps(msg));
        except:
            pass
        remove_usr = websocket.user
        clients.remove(websocket)
        for client in clients:
                await client.send(json.dumps({
                        'type' : 'remuser',
                        'user' : remove_usr,
                    }));
        print(websocket,"\n is disconnected from chat....")

    start_server = websockets.serve(chat_reciever, '0.0.0.0', 9000)
    asyncio.get_event_loop().run_until_complete(start_server)
    print('Server started  localhost:9000...\nServer Logs....\n')
except:
    pass

try:
    asyncio.get_event_loop().run_forever()
except:
    print('Server Closed !')
# db.close()