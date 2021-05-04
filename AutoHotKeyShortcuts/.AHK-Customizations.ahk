#singleinstance force

I_Icon = RGBAHK.ico
ICON [I_Icon]                        ;Changes a compiled script's icon (.exe)
if I_Icon <>
IfExist, %I_Icon%
	Menu, Tray, Icon, %I_Icon%   ;Changes menu tray icon 
	
#include alwaysOnTop.ahk
#include DrawShortcuts.ahk
#include ECENChars.ahk
#include ECENFormulas.ahk
#include GameCuts.ahk
#include GreekChars.ahk
#include MathChars.ahk
#include MiscChars.ahk
#include SpanishChars.ahk
#include swap@.ahk