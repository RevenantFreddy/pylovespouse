import winsdk.windows.devices.bluetooth.advertisement as wwda
import winsdk.windows.storage.streams as wwss
import asyncio
import time
import sys

async def send_command(command,duration):
    advt_publish = wwda.BluetoothLEAdvertisementPublisher()
    manufacturerData  = wwda.BluetoothLEManufacturerData()
    manufacturerData.company_id = 0xFF
    writer = wwss.DataWriter()
    writer.write_bytes(bytearray.fromhex("0000006db643ce97fe427c"+command))
    manufacturerData.data =  writer.detach_buffer()
    advt_publish.advertisement.manufacturer_data.append(manufacturerData)
    advt_publish.start()
    time.sleep(duration)
    while(str(advt_publish.status).split('.')[1]!="STARTED"):
        pass
    advt_publish.stop()
    
def SINGLE_SHOCK_MODE1(mode):
    if(mode==0):
        asyncio.run(send_command("d5964c",0.001))
    elif(mode==1):
        asyncio.run(send_command("d41f5d",0.001))
    elif(mode==2):
        asyncio.run(send_command("d7846f",0.001))
    elif(mode==3):
        asyncio.run(send_command("d60d7e",0.001))
    elif(mode==4):
        asyncio.run(send_command("d1b20a",0.001))
    elif(mode==5):
        asyncio.run(send_command("d03b1b",0.001))
    elif(mode==6):
        asyncio.run(send_command("d3a029",0.001))
    elif(mode==7):
        asyncio.run(send_command("d22938",0.001))
    elif(mode==8):
        asyncio.run(send_command("dddec0",0.001))
    elif(mode==9):
        asyncio.run(send_command("dc57d1",0.001))
        
def SINGLE_SHOCK_MODE2(mode):
    if(mode==0):
        asyncio.run(send_command("a5113f",0.001))
    elif(mode==1):
        asyncio.run(send_command("a4982e",0.001))
    elif(mode==2):
        asyncio.run(send_command("a7031c",0.001))
    elif(mode==3):
        asyncio.run(send_command("a68a0d",0.001))
    elif(mode==4):
        asyncio.run(send_command("a13579",0.001))
    elif(mode==5):
        asyncio.run(send_command("a0bc68",0.001))
    elif(mode==6):
        asyncio.run(send_command("a3275a",0.001))
    elif(mode==7):
        asyncio.run(send_command("a2ae4b",0.001))
    elif(mode==8):
        asyncio.run(send_command("ad59b3",0.001))
    elif(mode==9):
        asyncio.run(send_command("acd0a2",0.001))
        
def SHAKE(mode,duration):
    if(mode==0):
        asyncio.run(send_command("C5175C",duration))
    elif(mode==1):
        asyncio.run(send_command("F41D7C",duration))
    elif(mode==2):
        asyncio.run(send_command("F7864E",duration))
    elif(mode==3):
        asyncio.run(send_command("F60F5F",duration))
    elif(mode==4):
        asyncio.run(send_command("F1B02B",duration))
    elif(mode==5):
        asyncio.run(send_command("F0393A",duration))
    elif(mode==6):
        asyncio.run(send_command("F3A208",duration))
    elif(mode==7):
        asyncio.run(send_command("F22B19",duration))
    elif(mode==8):
        asyncio.run(send_command("FDDCE1",duration))
    elif(mode==9):
        asyncio.run(send_command("FC55F0",duration))
        
def TELESCOPIC_MODE(mode):
    if(mode==0):
        asyncio.run(send_command("E5157D",0.001))
    elif(mode==1):
        asyncio.run(send_command("E49C6C",0.001))
    elif(mode==2):
        asyncio.run(send_command("E7075E",0.001))
    elif(mode==3):
        asyncio.run(send_command("E68E4F",0.001))
    elif(mode==4):
        asyncio.run(send_command("E1313B",0.001))
    elif(mode==5):
        asyncio.run(send_command("E0B82A",0.001))
    elif(mode==6):
        asyncio.run(send_command("E32318",0.001))
    elif(mode==7):
        asyncio.run(send_command("E2AA09",0.001))
    elif(mode==8):
        asyncio.run(send_command("ED5DF1",0.001))
    elif(mode==9):
        asyncio.run(send_command("ECD4E0",0.001))
        
def OFF():
    asyncio.run(send_command("E5157D",0.001))
