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
L power:GND #PWR03
U 1 1 5F6551BE
P 4800 3850
F 0 "#PWR03" H 4800 3600 50  0001 C CNN
F 1 "GND" H 4805 3677 50  0000 C CNN
F 2 "" H 4800 3850 50  0001 C CNN
F 3 "" H 4800 3850 50  0001 C CNN
	1    4800 3850
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR02
U 1 1 5F655E30
P 4800 2550
F 0 "#PWR02" H 4800 2400 50  0001 C CNN
F 1 "+5V" H 4815 2723 50  0000 C CNN
F 2 "" H 4800 2550 50  0001 C CNN
F 3 "" H 4800 2550 50  0001 C CNN
	1    4800 2550
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_CBE Q2
U 1 1 5F65994B
P 7000 4000
F 0 "Q2" H 7191 4046 50  0000 L CNN
F 1 "Q_NPN_CBE" H 7191 3955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 7200 4100 50  0001 C CNN
F 3 "~" H 7000 4000 50  0001 C CNN
	1    7000 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_CBE Q4
U 1 1 5F65FBE6
P 9100 4000
F 0 "Q4" H 9291 4046 50  0000 L CNN
F 1 "Q_NPN_CBE" H 9291 3955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 9300 4100 50  0001 C CNN
F 3 "~" H 9100 4000 50  0001 C CNN
	1    9100 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_RCGB D2
U 1 1 5F661409
P 7100 3300
F 0 "D2" V 7146 2970 50  0000 R CNN
F 1 "LED_RCGB" V 7055 2970 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 7100 3250 50  0001 C CNN
F 3 "~" H 7100 3250 50  0001 C CNN
	1    7100 3300
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED_RCGB D3
U 1 1 5F661D2B
P 8150 3300
F 0 "D3" V 8196 2970 50  0000 R CNN
F 1 "LED_RCGB" V 8105 2970 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 8150 3250 50  0001 C CNN
F 3 "~" H 8150 3250 50  0001 C CNN
	1    8150 3300
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED_RCGB D4
U 1 1 5F662529
P 9200 3300
F 0 "D4" V 9246 2970 50  0000 R CNN
F 1 "LED_RCGB" V 9155 2970 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 9200 3250 50  0001 C CNN
F 3 "~" H 9200 3250 50  0001 C CNN
	1    9200 3300
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED_RCGB D5
U 1 1 5F663766
P 10250 3300
F 0 "D5" V 10296 2970 50  0000 R CNN
F 1 "LED_RCGB" V 10205 2970 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 10250 3250 50  0001 C CNN
F 3 "~" H 10250 3250 50  0001 C CNN
	1    10250 3300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6050 4200 7100 4200
Wire Wire Line
	7100 4200 8150 4200
Connection ~ 7100 4200
Connection ~ 8150 4200
Wire Wire Line
	9200 4200 10250 4200
Connection ~ 9200 4200
$Comp
L power:GND #PWR04
U 1 1 5F6724E6
P 8150 4200
F 0 "#PWR04" H 8150 3950 50  0001 C CNN
F 1 "GND" H 8155 4027 50  0000 C CNN
F 2 "" H 8150 4200 50  0001 C CNN
F 3 "" H 8150 4200 50  0001 C CNN
	1    8150 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	8150 4200 9200 4200
Wire Wire Line
	5850 2850 5850 3100
Wire Wire Line
	5850 2850 6900 2850
Wire Wire Line
	6900 2850 6900 3100
Wire Wire Line
	6900 2850 7950 2850
Wire Wire Line
	7950 2850 7950 3100
Connection ~ 6900 2850
Wire Wire Line
	7950 2850 9000 2850
Wire Wire Line
	9000 2850 9000 3100
Connection ~ 7950 2850
Wire Wire Line
	9000 2850 10050 2850
Wire Wire Line
	10050 2850 10050 3100
Connection ~ 9000 2850
Wire Wire Line
	6050 2950 6050 3100
Wire Wire Line
	6050 2950 7100 2950
Wire Wire Line
	7100 2950 7100 3100
Wire Wire Line
	7100 2950 8150 2950
Wire Wire Line
	8150 2950 8150 3100
Connection ~ 7100 2950
Wire Wire Line
	8150 2950 9200 2950
Wire Wire Line
	9200 2950 9200 3100
Connection ~ 8150 2950
Wire Wire Line
	9200 2950 10250 2950
Wire Wire Line
	10250 2950 10250 3100
Connection ~ 9200 2950
Wire Wire Line
	6250 3050 6250 3100
Wire Wire Line
	6250 3050 7300 3050
Wire Wire Line
	7300 3050 7300 3100
Wire Wire Line
	7300 3050 8350 3050
Wire Wire Line
	8350 3050 8350 3100
Connection ~ 7300 3050
Wire Wire Line
	8350 3050 9400 3050
Wire Wire Line
	9400 3050 9400 3100
Connection ~ 8350 3050
Wire Wire Line
	9400 3050 10450 3050
Wire Wire Line
	10450 3050 10450 3100
Connection ~ 9400 3050
Wire Wire Line
	5200 3150 5650 3150
Wire Wire Line
	5200 3250 5600 3250
Wire Wire Line
	6750 4000 6800 4000
Wire Wire Line
	7800 4000 7850 4000
Wire Wire Line
	5200 3350 5550 3350
Wire Wire Line
	8850 4000 8900 4000
Wire Wire Line
	5200 3450 5500 3450
Wire Wire Line
	9900 4000 9950 4000
Wire Wire Line
	4400 3050 4300 3050
Wire Wire Line
	4300 3850 4800 3850
Wire Wire Line
	4300 3050 4300 3850
Wire Wire Line
	4400 3350 4350 3350
Wire Wire Line
	4350 3350 4350 2550
$Comp
L Connector:Conn_01x05_Female J1
U 1 1 5F6A976F
P 3650 3050
F 0 "J1" H 3542 3435 50  0000 C CNN
F 1 "Conn_01x05_Female" H 3542 3344 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x05_P2.54mm_Vertical" H 3650 3050 50  0001 C CNN
F 3 "~" H 3650 3050 50  0001 C CNN
	1    3650 3050
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR01
U 1 1 5F6D4773
P 4000 3050
F 0 "#PWR01" H 4000 2900 50  0001 C CNN
F 1 "+5V" H 4015 3223 50  0000 C CNN
F 2 "" H 4000 3050 50  0001 C CNN
F 3 "" H 4000 3050 50  0001 C CNN
	1    4000 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 3250 3850 3250
Wire Wire Line
	4400 2950 4050 2950
Wire Wire Line
	4050 2950 4050 3150
Wire Wire Line
	4050 3150 3850 3150
Wire Wire Line
	3950 2750 3950 2950
Wire Wire Line
	3950 2950 3850 2950
$Comp
L Device:LED_RCGB D1
U 1 1 5F65B230
P 6050 3300
F 0 "D1" V 6096 2970 50  0000 R CNN
F 1 "LED_RCGB" V 6005 2970 50  0000 R CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 6050 3250 50  0001 C CNN
F 3 "~" H 6050 3250 50  0001 C CNN
	1    6050 3300
	0    -1   -1   0   
$EndComp
$Comp
L Device:Q_NPN_CBE Q5
U 1 1 5F65FBEC
P 10150 4000
F 0 "Q5" H 10341 4046 50  0000 L CNN
F 1 "Q_NPN_CBE" H 10341 3955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 10350 4100 50  0001 C CNN
F 3 "~" H 10150 4000 50  0001 C CNN
	1    10150 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_CBE Q3
U 1 1 5F65A346
P 8050 4000
F 0 "Q3" H 8241 4046 50  0000 L CNN
F 1 "Q_NPN_CBE" H 8241 3955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 8250 4100 50  0001 C CNN
F 3 "~" H 8050 4000 50  0001 C CNN
	1    8050 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 3350 5550 3650
Wire Wire Line
	5600 3250 5600 3600
$Comp
L Device:Q_NPN_CBE Q1
U 1 1 5F65887B
P 5950 4000
F 0 "Q1" H 6141 4046 50  0000 L CNN
F 1 "Q_NPN_CBE" H 6141 3955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92L_Inline" H 6150 4100 50  0001 C CNN
F 3 "~" H 5950 4000 50  0001 C CNN
	1    5950 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 3150 5650 3550
Wire Wire Line
	5650 3550 6750 3550
Wire Wire Line
	6750 3550 6750 4000
Wire Wire Line
	5600 3600 7800 3600
Wire Wire Line
	7800 3600 7800 4000
Wire Wire Line
	8850 4000 8850 3650
Wire Wire Line
	8850 3650 5550 3650
Wire Wire Line
	5500 3700 9900 3700
Wire Wire Line
	9900 3700 9900 4000
Wire Wire Line
	5500 3450 5500 3700
Wire Wire Line
	5450 3050 5450 4000
Wire Wire Line
	5200 3050 5450 3050
Wire Wire Line
	5450 4000 5750 4000
Wire Wire Line
	5850 2750 5850 2850
Connection ~ 5850 2850
Wire Wire Line
	5750 3050 6250 3050
Connection ~ 6250 3050
Wire Wire Line
	5200 2750 5850 2750
$Comp
L Device:R_US R5
U 1 1 5F7CF5DA
P 10250 3650
F 0 "R5" H 10318 3696 50  0000 L CNN
F 1 "R_US" H 10318 3605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 10290 3640 50  0001 C CNN
F 3 "~" H 10250 3650 50  0001 C CNN
	1    10250 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R4
U 1 1 5F7D083D
P 9200 3650
F 0 "R4" H 9268 3696 50  0000 L CNN
F 1 "R_US" H 9268 3605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 9240 3640 50  0001 C CNN
F 3 "~" H 9200 3650 50  0001 C CNN
	1    9200 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R3
U 1 1 5F7D286D
P 8150 3650
F 0 "R3" H 8218 3696 50  0000 L CNN
F 1 "R_US" H 8218 3605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 8190 3640 50  0001 C CNN
F 3 "~" H 8150 3650 50  0001 C CNN
	1    8150 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R2
U 1 1 5F7D47E9
P 7100 3650
F 0 "R2" H 7168 3696 50  0000 L CNN
F 1 "R_US" H 7168 3605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 7140 3640 50  0001 C CNN
F 3 "~" H 7100 3650 50  0001 C CNN
	1    7100 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R1
U 1 1 5F7D68B9
P 6050 3650
F 0 "R1" H 6118 3696 50  0000 L CNN
F 1 "R_US" H 6118 3605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 6090 3640 50  0001 C CNN
F 3 "~" H 6050 3650 50  0001 C CNN
	1    6050 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5200 2850 5800 2850
Wire Wire Line
	5800 2850 5800 2950
Wire Wire Line
	5800 2950 6050 2950
Connection ~ 6050 2950
Wire Wire Line
	5200 2950 5750 2950
Wire Wire Line
	5750 2950 5750 3050
Connection ~ 4800 2550
Connection ~ 4800 3850
$Comp
L Device:R_US R6
U 1 1 5F7FD3C6
P 4250 2750
F 0 "R6" V 4045 2750 50  0000 C CNN
F 1 "R_US" V 4136 2750 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 4290 2740 50  0001 C CNN
F 3 "~" H 4250 2750 50  0001 C CNN
	1    4250 2750
	0    1    1    0   
$EndComp
$Comp
L 74xx:74HC595 U1
U 1 1 5F654232
P 4800 3150
F 0 "U1" H 4800 3931 50  0000 C CNN
F 1 "74HC595" H 4800 3840 50  0000 C CNN
F 2 "Package_DIP:DIP-16_W7.62mm_LongPads" H 4800 3150 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74hc595.pdf" H 4800 3150 50  0001 C CNN
	1    4800 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 2750 3950 2750
Wire Wire Line
	4350 2550 4800 2550
Wire Wire Line
	4000 3050 3850 3050
Wire Wire Line
	3850 2850 4300 2850
Wire Wire Line
	4300 2850 4300 3050
Connection ~ 4300 3050
$EndSCHEMATC
