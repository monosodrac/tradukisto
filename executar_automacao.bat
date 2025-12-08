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

REM Perguntar ao usuário se ele deseja atualizar a tradução para uma nova ambientação
set /p resposta="Gostaria de atualizar a traducao para uma nova ambientacao para algum pais ou regiao? (s/n): "

REM Verificar a resposta do usuário
if /i "%resposta%"=="s" (
    echo Ativando ambiente virtual...
    call .env\Scripts\activate

    echo Executando o script Python...
    python traduzir_c_regiao.py
    if errorlevel 1 (
        echo Houve um erro ao executar traduzir_c_regiao.py
    )
) else (
    echo Ativando ambiente virtual...
    call .env\Scripts\activate

    echo Executando o script Python...
    python traduzir.py
    if errorlevel 1 (
        echo Houve um erro ao executar traduzir.py
    )
)

echo Desativando ambiente virtual...
call deactivate

echo -------------------------------------
echo   PROCESSO FINALIZADO
echo -------------------------------------
pause
