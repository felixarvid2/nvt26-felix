#switch 1
vlan 10
name KONTOR
interface range gigabitEthernet 0/1 - 2
    switchport mode trunk
    switchport trunk allowed vlan 10
    switchport trunk native vlan 999
interface fastEthernet 0/5
    switchport mode access
    switchport access vlan 10
spanning-tree vlan 10 root primary
interface FastEthernet 0/5
    spanning-tree portfast

!switch 2
vlan 10
name KONTOR
interface range gigabitEthernet 0/1 - 2
    switchport mode trunk
    switchport trunk allowed vlan 10
    switchport trunk native vlan 999
interface fastEthernet 0/6
    switchport mode access
    switchport access vlan 10
interface FastEthernet 0/6
    spanning-tree portfast

!switch 3
vlan 10
name KONTOR
interface range gigabitEthernet 0/1 - 2
    switchport mode trunk
    switchport trunk allowed vlan 10
    switchport trunk native vlan 999
interface fastEthernet 0/5
    switchport mode access
    switchport access vlan 10
spanning-tree vlan 10 root secondary
interface FastEthernet 0/5
    spanning-tree portfast
