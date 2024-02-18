# Python-Pf-isc-Opn-kea
An .xml conversion of pfsense isc-dhcp static lease device info to opnsense kea-dhcp reservation info.


pfsense xml -> array of [json obj] -> opnsense xml

  opnsense xml  -add new random uuid per device; re-used users' subnet uuid
