# Instructions for the automated kettle

## Table of contents

### [1. - Wiring](#1---wiring)

- [1.1 - From the resistor](#11---from-the-resistor-temperature-probe)
- [1.2 - On the relay](#12---on-the-relay)
- [1.3 - Raspberry Pi pinout](#13---raspberry-pi-pinout)

### [2. - Run the web server](#2---run-the-web-server)

### [3. - Use the kettle](#3---use-the-kettle)

- [3.1 - Connect to the web interface](#31---connect-to-the-web-interface)
- [3.2 - Using the interface](#32---using-the-interface)

### [4. - Credits](#4---credits)

## 1. - Wiring

(see diagram for exact pin locations)

### 1.1 - From the resistor (Temperature probe)

Yellow wire -> GPIO 4

Red wire -> Pin 1

White wire -> Pin 6

### 1.2 - On the relay

VCC -> Pin 2

IN1 -> any GPIO pin, it is chosen on the web interface

GND -> Pin 9

### 1.3 - Raspberry Pi pinout

<img src="../../images/pinout.png" alt="Raspberry Pi pinout" width="300" height="450" align="center"/>

---

## 2. - Run the web server

On the Raspberry Pi (via SSH)

User : pi

Password : p

```sh
cd ~/autokettle/webapp
```

Update the Github repository

```sh
git pull
```

Run the web server

```sh
./run.sh
```

---

## 3. - Use the kettle

### 3.1 - Connect to the web interface

Raspberry Pi IP:5000 or bouilloire.nsi.lan:5000

### 3.2 - Using the interface

In the sandwich menu, enter the GPIO pin used for the relay and the desired water temperature


Click on 'Submit' to validate this information (normally it is stored)

### 3.3 - Fire in the hole !

Click on 'Heat up' on the main menu to start the kettle, it will stop when the desired temperature is reached

---

### 4. - Credits

Bastien Croguennoc, Gwendal Troadec
