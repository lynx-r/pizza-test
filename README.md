# pizza-test
Тестовое задание

При создании заказа отправляется почта. Чтобы ее удалось отправить нужно запустить SMTP сервер:

```python
python -m smtpd -n -c DebuggingServer localhost:1025
```