EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R_Small_US R1
U 1 1 5F664522
P 3300 2100
F 0 "R1" H 3232 2054 50  0000 R CNN
F 1 "R_Small_US" H 3232 2145 50  0000 R CNN
F 2 "Inductor_THT:L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2" H 3300 2100 50  0001 C CNN
F 3 "~" H 3300 2100 50  0001 C CNN
	1    3300 2100
	1    0    0    1   
$EndComp
Wire Wire Line
	4200 2200 3300 2200
$Comp
L Device:Crystal Y1
U 1 1 5F668951
P 4050 2500
F 0 "Y1" V 4004 2631 50  0000 L CNN
F 1 "Crystal" V 4095 2631 50  0000 L CNN
F 2 "Crystal:Resonator-2Pin_W8.0mm_H3.5mm" H 4050 2500 50  0001 C CNN
F 3 "~" H 4050 2500 50  0001 C CNN
	1    4050 2500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4050 2350 4200 2350
Wire Wire Line
	4200 2350 4200 2400
Wire Wire Line
	4050 2650 4200 2650
Wire Wire Line
	4200 2650 4200 2600
$Comp
L Connector:USB_C_Receptacle_USB2.0 J1
U 1 1 5F66DDEE
P 2100 2450
F 0 "J1" V 2161 3180 50  0000 L CNN
F 1 "USB_C_Receptacle_USB2.0" V 2252 3180 50  0000 L CNN
F 2 "Connector_USB:USB_C_Receptacle_GCT_USB4085" H 2250 2450 50  0001 C CNN
F 3 "https://www.usb.org/sites/default/files/documents/usb_type-c.zip" H 2250 2450 50  0001 C CNN
	1    2100 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 2450 2700 2350
Wire Wire Line
	2700 2650 2700 2550
Wire Wire Line
	3300 4700 4800 4700
Wire Wire Line
	4900 4700 4800 4700
Connection ~ 4800 4700
$Comp
L MCU_Microchip_ATmega:ATmega8U2-AU U1
U 1 1 5F5EC9ED
P 4900 3300
F 0 "U1" H 4900 1811 50  0000 C CNN
F 1 "ATmega8U2-AU" H 4900 1720 50  0000 C CNN
F 2 "Package_QFP:TQFP-32_7x7mm_P0.8mm" H 4900 3300 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/doc7799.pdf" H 4900 3300 50  0001 C CNN
	1    4900 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 1800 3300 2000
Wire Wire Line
	4800 1900 4800 1850
Wire Wire Line
	4800 1850 2700 1850
Wire Wire Line
	4200 2800 2700 2800
Wire Wire Line
	2700 2800 2700 2650
Connection ~ 2700 2650
Wire Wire Line
	2700 2450 2750 2450
Wire Wire Line
	2750 2450 2750 2900
Wire Wire Line
	2750 2900 4200 2900
Connection ~ 2700 2450
Wire Wire Line
	1800 3350 2100 3350
Wire Wire Line
	2100 3350 3300 3350
Connection ~ 2100 3350
Connection ~ 3300 3350
Wire Wire Line
	3300 3350 3300 4700
Wire Wire Line
	5000 1900 5000 1650
Wire Wire Line
	4150 1650 4150 1800
Connection ~ 4150 1800
Wire Wire Line
	4150 1800 3300 1800
$Comp
L Device:L L1
U 1 1 5F695631
P 4550 1650
F 0 "L1" V 4369 1650 50  0000 C CNN
F 1 "L" V 4460 1650 50  0000 C CNN
F 2 "Inductor_THT:L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2" H 4550 1650 50  0001 C CNN
F 3 "~" H 4550 1650 50  0001 C CNN
	1    4550 1650
	0    1    1    0   
$EndComp
Wire Wire Line
	4150 1650 4400 1650
Wire Wire Line
	4700 1650 5000 1650
$Comp
L Device:C C4
U 1 1 5F6975D9
P 4050 3350
F 0 "C4" V 3798 3350 50  0000 C CNN
F 1 "C" V 3889 3350 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4088 3200 50  0001 C CNN
F 3 "~" H 4050 3350 50  0001 C CNN
	1    4050 3350
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 3350 4200 3100
Wire Wire Line
	4200 2200 4200 1750
Connection ~ 4200 2200
$Comp
L Connector:Conn_01x13_Male J2
U 1 1 5F70DBEF
P 7850 2850
F 0 "J2" H 7822 2874 50  0000 R CNN
F 1 "Conn_01x13_Male" H 7822 2783 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x13_P2.54mm_Vertical" H 7850 2850 50  0001 C CNN
F 3 "~" H 7850 2850 50  0001 C CNN
	1    7850 2850
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x13_Male J3
U 1 1 5F711428
P 7850 4200
F 0 "J3" H 7822 4224 50  0000 R CNN
F 1 "Conn_01x13_Male" H 7822 4133 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x13_P2.54mm_Vertical" H 7850 4200 50  0001 C CNN
F 3 "~" H 7850 4200 50  0001 C CNN
	1    7850 4200
	-1   0    0    -1  
$EndComp
Connection ~ 4900 4700
Wire Wire Line
	4900 4700 4900 4900
Wire Wire Line
	4900 4900 7600 4900
Wire Wire Line
	4200 1750 7500 1750
Wire Wire Line
	7500 1750 7500 3600
Wire Wire Line
	7500 3600 7650 3600
Wire Wire Line
	5600 3100 7450 3100
Wire Wire Line
	7450 3100 7450 3700
Wire Wire Line
	7450 3700 7650 3700
Wire Wire Line
	5600 3700 7400 3700
Wire Wire Line
	7400 3700 7400 3800
Wire Wire Line
	7400 3800 7650 3800
Wire Wire Line
	5600 3800 7350 3800
Wire Wire Line
	7350 3800 7350 3900
Wire Wire Line
	7350 3900 7650 3900
Wire Wire Line
	5600 3900 7300 3900
Wire Wire Line
	7300 3900 7300 4000
Wire Wire Line
	7300 4000 7650 4000
Wire Wire Line
	5600 4000 7250 4000
Wire Wire Line
	5600 4100 7200 4100
Wire Wire Line
	7200 4100 7200 4400
Wire Wire Line
	7200 4400 7650 4400
Wire Wire Line
	5600 4200 7150 4200
Wire Wire Line
	7150 4200 7150 4500
Wire Wire Line
	7150 4500 7650 4500
Wire Wire Line
	5600 4300 7100 4300
Wire Wire Line
	7100 4300 7100 4600
Wire Wire Line
	7100 4600 7650 4600
Wire Wire Line
	5600 4400 7050 4400
Wire Wire Line
	7050 4400 7050 4700
Wire Wire Line
	7050 4700 7650 4700
Wire Wire Line
	5600 2200 7000 2200
Wire Wire Line
	7000 2200 7000 4800
Wire Wire Line
	7000 4800 7650 4800
Wire Wire Line
	7550 1800 7550 2850
Wire Wire Line
	7650 2950 7600 2950
Wire Wire Line
	7650 2850 7550 2850
Connection ~ 7550 2850
Wire Wire Line
	5600 2300 7650 2300
Wire Wire Line
	7650 2300 7650 2250
Wire Wire Line
	5600 2400 7650 2400
Wire Wire Line
	7650 2400 7650 2350
Wire Wire Line
	5600 2500 7650 2500
Wire Wire Line
	7650 2500 7650 2450
Wire Wire Line
	5600 2600 7650 2600
Wire Wire Line
	7650 2600 7650 2550
Wire Wire Line
	5600 2700 7650 2700
Wire Wire Line
	7650 2700 7650 2650
Wire Wire Line
	5600 2800 7650 2800
Wire Wire Line
	7650 2800 7650 2750
Wire Wire Line
	5600 2900 7450 2900
Wire Wire Line
	7450 2900 7450 3050
Wire Wire Line
	7450 3050 7650 3050
Wire Wire Line
	5600 3500 7400 3500
Wire Wire Line
	7400 3500 7400 3150
Wire Wire Line
	7400 3150 7650 3150
Wire Wire Line
	5600 3400 7350 3400
Wire Wire Line
	7350 3400 7350 3250
Wire Wire Line
	7350 3250 7650 3250
Wire Wire Line
	5600 3300 7300 3300
Wire Wire Line
	7300 3300 7300 3350
Wire Wire Line
	7300 3350 7650 3350
Wire Wire Line
	5600 3200 7250 3200
Wire Wire Line
	7250 3200 7250 3450
Wire Wire Line
	7250 3450 7650 3450
$Comp
L Device:C C1
U 1 1 5F7569C2
P 3700 2350
F 0 "C1" V 3448 2350 50  0000 C CNN
F 1 "C" V 3539 2350 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm" H 3738 2200 50  0001 C CNN
F 3 "~" H 3700 2350 50  0001 C CNN
	1    3700 2350
	0    1    1    0   
$EndComp
$Comp
L Device:C C2
U 1 1 5F757627
P 3700 2650
F 0 "C2" V 3448 2650 50  0000 C CNN
F 1 "C" V 3539 2650 50  0000 C CNN
F 2 "Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm" H 3738 2500 50  0001 C CNN
F 3 "~" H 3700 2650 50  0001 C CNN
	1    3700 2650
	0    1    1    0   
$EndComp
Wire Wire Line
	3850 2350 4050 2350
Connection ~ 4050 2350
Wire Wire Line
	3850 2650 4050 2650
Connection ~ 4050 2650
Wire Wire Line
	3550 2350 3550 2650
Wire Wire Line
	3550 2650 3550 3350
Connection ~ 3550 2650
Connection ~ 3550 3350
Wire Wire Line
	3550 3350 3900 3350
Connection ~ 3300 2200
Wire Wire Line
	3300 2200 3300 2350
Wire Wire Line
	3300 2750 3300 3350
$Comp
L Switch:SW_Push_Open_Dual SW1
U 1 1 5F79B235
P 3100 2550
F 0 "SW1" V 3054 2263 50  0000 R CNN
F 1 "SW_Push_Open_Dual" V 3145 2263 50  0000 R CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 3100 2750 50  0001 C CNN
F 3 "~" H 3100 2750 50  0001 C CNN
	1    3100 2550
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3300 2350 3100 2350
Connection ~ 3300 2350
Wire Wire Line
	3100 2750 3300 2750
Connection ~ 3300 2750
Wire Wire Line
	4150 1800 4800 1800
Wire Wire Line
	4800 1850 4800 1800
Connection ~ 4800 1850
Connection ~ 4800 1800
Wire Wire Line
	4800 1800 7550 1800
Wire Wire Line
	7650 4100 7550 4100
Wire Wire Line
	7550 4100 7550 2850
Wire Wire Line
	7600 4900 7600 4200
Wire Wire Line
	7650 4200 7600 4200
Connection ~ 7600 4200
Wire Wire Line
	7600 4200 7600 2950
Wire Wire Line
	7250 4300 7650 4300
Wire Wire Line
	7250 4000 7250 4300
Wire Wire Line
	3300 3350 3550 3350
$Comp
L power:GND #PWR?
U 1 1 5F80F56B
P 3300 4700
F 0 "#PWR?" H 3300 4450 50  0001 C CNN
F 1 "GND" H 3305 4527 50  0000 C CNN
F 2 "" H 3300 4700 50  0001 C CNN
F 3 "" H 3300 4700 50  0001 C CNN
	1    3300 4700
	1    0    0    -1  
$EndComp
Connection ~ 3300 4700
$EndSCHEMATC
