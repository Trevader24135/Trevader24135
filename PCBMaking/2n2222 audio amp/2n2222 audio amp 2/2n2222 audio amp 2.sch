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
L Device:Q_NPN_EBC Q1
U 1 1 5F690F33
P 5850 2950
F 0 "Q1" H 6041 2996 50  0000 L CNN
F 1 "Q_NPN_EBC" H 6041 2905 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 6050 3050 50  0001 C CNN
F 3 "~" H 5850 2950 50  0001 C CNN
	1    5850 2950
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Male J1
U 1 1 5F697520
P 4950 2950
F 0 "J1" H 5058 3231 50  0000 C CNN
F 1 "Conn_01x03_Male" H 5058 3140 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x03_P2.54mm_Vertical" H 4950 2950 50  0001 C CNN
F 3 "~" H 4950 2950 50  0001 C CNN
	1    4950 2950
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R1
U 1 1 5F69918D
P 5650 2800
F 0 "R1" H 5582 2754 50  0000 R CNN
F 1 "R_US" H 5582 2845 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5690 2790 50  0001 C CNN
F 3 "~" H 5650 2800 50  0001 C CNN
	1    5650 2800
	1    0    0    1   
$EndComp
$Comp
L Device:R_US R2
U 1 1 5F69A7D1
P 5650 3100
F 0 "R2" H 5582 3054 50  0000 R CNN
F 1 "R_US" H 5582 3145 50  0000 R CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5690 3090 50  0001 C CNN
F 3 "~" H 5650 3100 50  0001 C CNN
	1    5650 3100
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x02_Female J2
U 1 1 5F69A8FB
P 6150 2650
F 0 "J2" H 6178 2626 50  0000 L CNN
F 1 "Conn_01x02_Female" H 6178 2535 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x02_P2.54mm_Vertical" H 6150 2650 50  0001 C CNN
F 3 "~" H 6150 2650 50  0001 C CNN
	1    6150 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 2650 5950 2650
Wire Wire Line
	5650 2650 5350 2650
Wire Wire Line
	5350 2650 5350 2850
Wire Wire Line
	5350 2850 5150 2850
Connection ~ 5650 2650
Wire Wire Line
	5150 2950 5650 2950
Connection ~ 5650 2950
Wire Wire Line
	5150 3050 5150 3250
Wire Wire Line
	5150 3250 5650 3250
Wire Wire Line
	5650 3250 5950 3250
Wire Wire Line
	5950 3250 5950 3150
Connection ~ 5650 3250
$Comp
L power:GND #PWR?
U 1 1 5F69D4EF
P 5650 3250
F 0 "#PWR?" H 5650 3000 50  0001 C CNN
F 1 "GND" H 5655 3077 50  0000 C CNN
F 2 "" H 5650 3250 50  0001 C CNN
F 3 "" H 5650 3250 50  0001 C CNN
	1    5650 3250
	1    0    0    -1  
$EndComp
$EndSCHEMATC
