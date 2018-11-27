#!/usr/bin/env python
import os
import sys
import threading

if sys.version_info[0] != 3:
	print('\n Use Python Version 3.X \n')
	exit(0)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alumni.settings")
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)

#################################

"""
if 1:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alumni.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)  
"""
# import asyncio
# import websockets
# import sqlite3
# #import os
# #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alumni")
# #from Home import models
# #print(dir(settings.BASE_DIR),settings.BASE_DIR)
# clients=[]
# clientsu=["",""]
# db=sqlite3.connect('chat.db')
# cursor=db.cursor()
# try:
#     async def hello(websocket, path):
#         clients.append(websocket)
#         lgnuser=await websocket.recv()
#         if lgnuser not in clientsu:
#             clientsu.insert(1,lgnuser)
#         await websocket.send("12415478874587487849787978488977897446477977897448177971791779746"+str(clientsu))
#         for client in clients:
#                 if client != websocket:
#                     await client.send("12415478874587487849787978488977897446477977897448177971791779746"+"['', '"+str(lgnuser)+"', '']")
#         print(websocket,lgnuser,"\n is connected to chat....")
#         while True:
#             try:
#                 msg = await websocket.recv()
#                 try:
#                     user,message=msg.split('<<<:>>>')
#                     cursor.execute('insert into chat(Username,msg) values("'+str(user)+'","'+str(message)+'")')
#                     db.commit()
#                 except:
#                     pass
#                 #Home.models.chat(Username='Lokesh Bhoyar',Messege=msg).save()
#             except:
#                 break
#             for client in clients:
#                 if client != websocket:
#                     await client.send(msg)
#         clients.remove(websocket)
#         for client in clients:
#                 await client.send("12415478874587487849787978488977897446477977897448177971791779747"+str(lgnuser))
#         if lgnuser in clientsu:
#             clientsu.remove(lgnuser);
#         print(websocket,"\n is disconnected from chat....")
#     start_server = websockets.serve(hello, '0.0.0.0', 9000)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     print('Server started  localhost:9000...\nServer Logs....\n')
#     try:
#         asyncio.get_event_loop().run_forever()
#     except:
#         print('Server Closed')
#     db.close()
# except:
#     print ("Welcome")
