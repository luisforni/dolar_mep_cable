import websockets
import asyncio
import json

al30a_ci_nombre = ''
al30a_ci_instru = ''
al30a_ci_plazol = ''
al30a_ci_precio = ''
al30c_ci_nombre = ''
al30c_ci_instru = ''
al30c_ci_plazol = ''
al30c_ci_precio = ''
al30d_ci_nombre = ''
al30d_ci_instru = ''
al30d_ci_plazol = ''
al30d_ci_precio = ''
al30a_24_nombre = ''
al30a_24_instru = ''
al30a_24_plazol = ''
al30a_24_precio = ''
al30c_24_nombre = ''
al30c_24_instru = ''
al30c_24_plazol = ''
al30c_24_precio = ''
al30d_24_nombre = ''
al30d_24_instru = ''
al30d_24_plazol = ''
al30d_24_precio = ''
al30a_48_nombre = ''
al30a_48_instru = ''
al30a_48_plazol = ''
al30a_48_precio = ''
al30c_48_nombre = ''
al30c_48_instru = ''
al30c_48_plazol = ''
al30c_48_precio = ''
al30d_48_nombre = ''
al30d_48_instru = ''
al30d_48_plazol = ''
al30d_48_precio = ''

gd30a_ci_nombre = ''
gd30a_ci_instru = ''
gd30a_ci_plazol = ''
gd30a_ci_precio = ''
gd30c_ci_nombre = ''
gd30c_ci_instru = ''
gd30c_ci_plazol = ''
gd30c_ci_precio = ''
gd30d_ci_nombre = ''
gd30d_ci_instru = ''
gd30d_ci_plazol = ''
gd30d_ci_precio = ''
gd30a_24_nombre = ''
gd30a_24_instru = ''
gd30a_24_plazol = ''
gd30a_24_precio = ''
gd30c_24_nombre = ''
gd30c_24_instru = ''
gd30c_24_plazol = ''
gd30c_24_precio = ''
gd30d_24_nombre = ''
gd30d_24_instru = ''
gd30d_24_plazol = ''
gd30d_24_precio = ''
gd30a_48_nombre = ''
gd30a_48_instru = ''
gd30a_48_plazol = ''
gd30a_48_precio = ''
gd30c_48_nombre = ''
gd30c_48_instru = ''
gd30c_48_plazol = ''
gd30c_48_precio = ''
gd30d_48_nombre = ''
gd30d_48_instru = ''
gd30d_48_plazol = ''
gd30d_48_precio = ''

async def  listen():
    global al30a_ci_nombre
    global al30a_ci_instru
    global al30a_ci_plazol
    global al30a_ci_precio
    global al30c_ci_nombre
    global al30c_ci_instru
    global al30c_ci_plazol
    global al30c_ci_precio
    global al30d_ci_nombre
    global al30d_ci_instru
    global al30d_ci_plazol
    global al30d_ci_precio
    global al30a_24_nombre
    global al30a_24_instru
    global al30a_24_plazol
    global al30a_24_precio
    global al30c_24_nombre
    global al30c_24_instru
    global al30c_24_plazol
    global al30c_24_precio
    global al30d_24_nombre
    global al30d_24_instru
    global al30d_24_plazol
    global al30d_24_precio
    global al30a_48_nombre
    global al30a_48_instru
    global al30a_48_plazol
    global al30a_48_precio
    global al30c_48_nombre
    global al30c_48_instru
    global al30c_48_plazol
    global al30c_48_precio
    global al30d_48_nombre
    global al30d_48_instru
    global al30d_48_plazol
    global al30d_48_precio
    global gd30a_ci_nombre
    global gd30a_ci_instru
    global gd30a_ci_plazol
    global gd30a_ci_precio
    global gd30c_ci_nombre
    global gd30c_ci_instru
    global gd30c_ci_plazol
    global gd30c_ci_precio
    global gd30d_ci_nombre
    global gd30d_ci_instru
    global gd30d_ci_plazol
    global gd30d_ci_precio
    global gd30a_24_nombre
    global gd30a_24_instru
    global gd30a_24_plazol
    global gd30a_24_precio
    global gd30c_24_nombre
    global gd30c_24_instru
    global gd30c_24_plazol
    global gd30c_24_precio
    global gd30d_24_nombre
    global gd30d_24_instru
    global gd30d_24_plazol
    global gd30d_24_precio
    global gd30a_48_nombre
    global gd30a_48_instru
    global gd30a_48_plazol
    global gd30a_48_precio
    global gd30c_48_nombre
    global gd30c_48_instru
    global gd30c_48_plazol
    global gd30c_48_precio
    global gd30d_48_nombre
    global gd30d_48_instru
    global gd30d_48_plazol
    global gd30d_48_precio

    url = 'wss://test-algobalanz.herokuapp.com/ws/luis'
    
    async with websockets.connect(url) as ws:
        msg  = await ws.recv()
        data = json.loads(msg)
        data = data['msg']

        nombre = data['securityID']
        instru = data['symbol']
        plazol = data['settlementType']
        precio = data['last']['price']

        # AL30 CI
        if nombre == 'AL30-0001-C-CT-ARS':
            al30a_ci_nombre = data['securityID']
            al30a_ci_instru = data['symbol']
            al30a_ci_plazol = data['settlementType']
            al30a_ci_precio = data['last']['price']

        if nombre == 'AL30C-0001-C-CT-EXT':
            al30c_ci_nombre = data['securityID']
            al30c_ci_instru = data['symbol']
            al30c_ci_plazol = data['settlementType']
            al30c_ci_precio = data['last']['price']

        if nombre == 'AL30D-0001-C-CT-USD':
            al30d_ci_nombre = data['securityID']
            al30d_ci_instru = data['symbol']
            al30d_ci_plazol = data['settlementType']
            al30d_ci_precio = data['last']['price']

        # AL30 24
        if nombre == 'AL30-0002-C-CT-ARS':
            al30a_24_nombre = data['securityID']
            al30a_24_instru = data['symbol']
            al30a_24_plazol = data['settlementType']
            al30a_24_precio = data['last']['price']

        if nombre == 'AL30C-0002-C-CT-EXT':
            al30c_24_nombre = data['securityID']
            al30c_24_instru = data['symbol']
            al30c_24_plazol = data['settlementType']
            al30c_24_precio = data['last']['price']

        if nombre == 'AL30D-0002-C-CT-USD':
            al30d_24_nombre = data['securityID']
            al30d_24_instru = data['symbol']
            al30d_24_plazol = data['settlementType']
            al30d_24_precio = data['last']['price']

        # AL30 48
        if nombre == 'AL30-0003-C-CT-ARS':
            al30a_48_nombre = data['securityID']
            al30a_48_instru = data['symbol']
            al30a_48_plazol = data['settlementType']
            al30a_48_precio = data['last']['price']

        if nombre == 'AL30C-0003-C-CT-EXT':
            al30c_48_nombre = data['securityID']
            al30c_48_instru = data['symbol']
            al30c_48_plazol = data['settlementType']
            al30c_48_precio = data['last']['price']

        if nombre == 'AL30D-0003-C-CT-USD':
            al30d_48_nombre = data['securityID']
            al30d_48_instru = data['symbol']
            al30d_48_plazol = data['settlementType']
            al30d_48_precio = data['last']['price']

        # GD30 CI
        if nombre == 'GD30-0001-C-CT-ARS':
            gd30a_ci_nombre = data['securityID']
            gd30a_ci_instru = data['symbol']
            gd30a_ci_plazol = data['settlementType']
            gd30a_ci_precio = data['last']['price']

        if nombre == 'GD30C-0001-C-CT-EXT':
            gd30c_ci_nombre = data['securityID']
            gd30c_ci_instru = data['symbol']
            gd30c_ci_plazol = data['settlementType']
            gd30c_ci_precio = data['last']['price']

        if nombre == 'GD30D-0001-C-CT-USD':
            gd30d_ci_nombre = data['securityID']
            gd30d_ci_instru = data['symbol']
            gd30d_ci_plazol = data['settlementType']
            gd30d_ci_precio = data['last']['price']

        # GD30 24
        if nombre == 'GD30-0002-C-CT-ARS':
            gd30a_24_nombre = data['securityID']
            gd30a_24_instru = data['symbol']
            gd30a_24_plazol = data['settlementType']
            gd30a_24_precio = data['last']['price']

        if nombre == 'GD30C-0002-C-CT-EXT':
            gd30c_24_nombre = data['securityID']
            gd30c_24_instru = data['symbol']
            gd30c_24_plazol = data['settlementType']
            gd30c_24_precio = data['last']['price']

        if nombre == 'GD30D-0002-C-CT-USD':
            gd30d_24_nombre = data['securityID']
            gd30d_24_instru = data['symbol']
            gd30d_24_plazol = data['settlementType']
            gd30d_24_precio = data['last']['price']

        # GD30 48
        if nombre == 'GD30-0003-C-CT-ARS':
            gd30a_48_nombre = data['securityID']
            gd30a_48_instru = data['symbol']
            gd30a_48_plazol = data['settlementType']
            gd30a_48_precio = data['last']['price']

        if nombre == 'GD30C-0003-C-CT-EXT':
            gd30c_48_nombre = data['securityID']
            gd30c_48_instru = data['symbol']
            gd30c_48_plazol = data['settlementType']
            gd30c_48_precio = data['last']['price']

        if nombre == 'GD30D-0003-C-CT-USD':
            gd30d_48_nombre = data['securityID']
            gd30d_48_instru = data['symbol']
            gd30d_48_plazol = data['settlementType']
            gd30d_48_precio = data['last']['price']

        # AL30 CI
        try:
            mep_al30_ci = al30a_ci_precio / al30d_ci_precio
            print('MEP   ', al30a_ci_instru, al30a_ci_plazol, '   ', mep_al30_ci)
        except:
            pass
        
        try:
            cab_al30_ci = al30a_ci_precio / al30c_ci_precio
            print('CABLE ', al30a_ci_instru, al30a_ci_plazol, '   ',cab_al30_ci)
        except:
            pass

        # AL30 24
        try:
            mep_al30_24 = al30a_24_precio / al30d_24_precio
            print('MEP   ', al30a_24_instru, al30a_24_plazol, ' ', mep_al30_24)
        except:
            pass
        
        try:
            cab_al30_24 = al30a_24_precio / al30c_24_precio
            print('CABLE ', al30a_24_instru, al30a_24_plazol, ' ',cab_al30_24)
        except:
            pass

        # AL30 48
        try:
            mep_al30_48 = al30a_48_precio / al30d_48_precio
            print('MEP   ', al30a_48_instru, al30a_48_plazol, ' ', mep_al30_48)
        except:
            pass
        
        try:
            cab_al30_48 = al30a_48_precio / al30c_48_precio
            print('CABLE ', al30a_48_instru, al30a_48_plazol, ' ',cab_al30_48)
        except:
            pass

        # GD30 CI
        try:
            mep_gd30_ci = gd30a_ci_precio / gd30d_ci_precio
            print('MEP   ', gd30a_ci_instru, gd30a_ci_plazol, '   ', mep_gd30_ci)
        except:
            pass
        
        try:
            cab_gd30_ci = gd30a_ci_precio / gd30c_ci_precio
            print('CABLE ', gd30a_ci_instru, gd30a_ci_plazol, '   ',cab_gd30_ci)
        except:
            pass

        # GD30 24
        try:
            mep_gd30_24 = gd30a_24_precio / gd30d_24_precio
            print('MEP   ', gd30a_24_instru, gd30a_24_plazol, ' ', mep_gd30_24)
        except:
            pass
        
        try:
            cab_gd30_24 = gd30a_24_precio / gd30c_24_precio
            print('CABLE ', gd30a_24_instru, gd30a_24_plazol, ' ',cab_gd30_24)
        except:
            pass

        # GD30 48
        try:
            mep_gd30_48 = gd30a_48_precio / gd30d_48_precio
            print('MEP   ', gd30a_48_instru, gd30a_48_plazol, ' ', mep_gd30_48)
        except:
            pass
        
        try:
            cab_gd30_48 = gd30a_48_precio / gd30c_48_precio
            print('CABLE ', gd30a_48_instru, gd30a_48_plazol, ' ',cab_gd30_48)
        except:
            pass

while True:
    asyncio.run(listen())