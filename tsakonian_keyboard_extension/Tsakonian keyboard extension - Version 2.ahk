#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force

; Lower letters

:*?:τσσ::τ͡σ
:*?:σ/::σ̌
:*?:ζ/::ζ̌

:*?:τ/::τ̇
:*?:π/::π̇
:*?:κ/::κ̇

:*?:ν/::ν̂
:*?:λ/::λ̣

; Capital letters

:*?:Τσσ::Τ͡σ
:*?:Σ/::Σ̌
:*?:Ζ/::Ζ̌

:*?:Τ/::Τ̇
:*?:Π/::Π̇
:*?:Κ/::Κ̇

:*?:Ν/::Ν̂
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

