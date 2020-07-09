@echo off

setlocal EnableDelayedExpansion

set filename=

for %%i in (*.lnk) do (
set filename=%%i
set purefilename=!filename: - ¿ì½Ý·½Ê½=!
set purefilename=!purefilename:.exe=!
echo !filename! !purefilename!
ren "!filename!" "!purefilename!"
)

pause