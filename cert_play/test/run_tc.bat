@echo off
echo Iteration 2
@echo on
@echo off
echo Time Stamp is: %DATE% %TIME%
echo %USERNAME%
echo %USERDOMAIN%
ver
@echo on
@echo off
pushd %~dp0
echo.
echo.
echo.
echo.
echo "cli_--help"

cd ..
cd ..
if not exist "cert_play/test/logs/" MD "cert_play/test/logs/"
cd scripts
call activate_vir_env.bat
cd ..
python -m cert_play.main.certplay --help > cert_play\test\logs\cli_--help.log
cd scripts
call deactivate_vir_env.bat
cd ..
echo.
echo.
echo.
echo.
echo "Batch Execution Done"

@echo on