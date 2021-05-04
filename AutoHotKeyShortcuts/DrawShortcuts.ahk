#singleinstance force


:?c*:%testpos::
MouseGetPos, X, Y
MsgBox, X: %X%, Y: %Y%
return

:?c*:%3dbox::
BoxScale:= 100
OneNoteDrawX:= 716
OneNoteDrawY:= 94

MouseGetPos, MX, MY

WinGetActiveTitle, Window
;MsgBox, %Window%
if( InStr(Window, "OneNote") != 0) {
	Click, %OneNoteDrawX%, %OneNoteDrawY%
}

for key, Yoff in [0, BoxScale] {
	MouseClickDrag, L, MX, MY + Yoff, MX + BoxScale, MY + (BoxScale / 2) + Yoff
	MouseClickDrag, L, MX + BoxScale, MY + BoxScale / 2 + Yoff, MX + BoxScale * 2, MY + Yoff
	MouseClickDrag, L, MX + BoxScale * 2, MY + Yoff, MX + BoxScale, MY - BoxScale / 2 + Yoff
	MouseClickDrag, L, MX + BoxScale, MY - BoxScale / 2 + Yoff, MX, MY + Yoff
}
MouseClickDrag, L, MX, MY, MX, MY + BoxScale
MouseClickDrag, L, MX + BoxScale, MY + BoxScale / 2, MX + BoxScale, MY + BoxScale / 2 + BoxScale
MouseClickDrag, L, MX + BoxScale * 2, MY, MX + BoxScale * 2, MY + BoxScale
MouseClickDrag, L, MX + BoxScale, MY - BoxScale / 2, MX + BoxScale, MY - BoxScale / 2 + BoxScale
return