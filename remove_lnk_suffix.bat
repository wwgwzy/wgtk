@echo off

setlocal EnableDelayedExpansion

set filename=

for %%i in (*.lnk) do (
set filename=%%i
set purefilename=!filename: - ��ݷ�ʽ=!
set purefilename=!purefilename:.exe=!
echo !filename! !purefilename!
ren "!filename!" "!purefilename!"
)

pause