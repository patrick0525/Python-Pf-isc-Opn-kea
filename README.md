# Python-Opnsense
.xml conversion of pfsense isc-dhcp static lease device info into opnsese kea-dhcp static lease device info.
pfsense xml -> array of [json obj] -> opnsense xml

  opnsense xml  -add new random uuid per device
                - re-used users' <subnet> uuid
