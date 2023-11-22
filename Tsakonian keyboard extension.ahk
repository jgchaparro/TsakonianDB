#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force

; Lower letters

:*?:τσσ::τσ̇
:*?:σ/::σ̌
:*?:ζ/::ζ̌

:*?:τ/::τ̇
:*?:π/::π̇
:*?:κ/::κ̇

:*?:μ/::μ̇
:*?:ν/::ν̇
:*?:λ/::λ̣

; Capital letters

:*?:Σ/::Σ̌
:*?:Ζ/::Ζ̌

:*?:Τ/::Τ̇
:*?:Π/::Π̇
:*?:Κ/::Κ̇

:*?:Μ/::Μ̇
:*?:Ν/::Ν̇
:*?:Λ/::Λ̣

; Word workarounds

:*?:τς::
Clipboard := "τσ̇"
Send ^v
return

:*?:ς/::
Clipboard := "σ̌"
Send ^v
return

