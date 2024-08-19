@echo off
pytest --alluredir=allure-results
if %errorlevel% equ 0 (
    allure serve allure-results
) else (
    echo Tests failed. Report not generated.
)
