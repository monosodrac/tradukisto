@echo off
echo -------------------------------------
echo   INICIANDO AMBIENTE DE TRADUCAO
echo -------------------------------------

REM Verifica se a venv existe
if not exist ".env\Scripts\activate.bat" (
    echo ERRO: A pasta .env NAO foi encontrada!
    echo Crie com: python -m venv .env
    pause
    exit /b
)

echo Ativando ambiente virtual...
call .env\Scripts\activate

echo Executando o script Python...
python main.py
if errorlevel 1 (
    echo Houve um erro ao executar main.py
)

echo Desativando ambiente virtual...
call deactivate

echo -------------------------------------
echo   PROCESSO FINALIZADO
echo -------------------------------------
pause
