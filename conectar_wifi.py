def conectar_wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectando a la red...')
        sta_if.active(True)
        sta_if.connect('SSID', 'contraseña') #Modificar por datos de WiFi
        while not sta_if.isconnected():
            pass
    red = sta_if.ifconfig()
    print('Configuracion de la red:', red[0:3])

conectar_wifi()

