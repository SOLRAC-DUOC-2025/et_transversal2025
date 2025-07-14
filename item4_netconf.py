from ncclient import manager

router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>11.1.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

with manager.connect(**router) as m:
    print("✅ Conectado vía NETCONF")
    m.edit_config(target="running", config=config_loopback)
    print("✅ Loopback111 configurada")
