from airflow.providers.telegram.hooks.telegram import TelegramHook # импортируем хук телеграма

def send_telegram_success_message(context): # на вход принимаем словарь со контекстными переменными
    hook = TelegramHook(telegram_conn_id='test',
                        token='{7018455315:AAE9nYzvnnXv2CEVBMP5bNmm9WEt2dXJNT0}',
                        chat_id='{-1002066440377}')
    dag = context['ti'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '{-1002066440377}',
        'text': message
    }) # отправление сообщения 
    
def send_telegram_failure_message(context):
    hook = TelegramHook(telegram_conn_id='test',
                        token='{7018455315:AAE9nYzvnnXv2CEVBMP5bNmm9WEt2dXJNT0}',
                        chat_id='{-1002066440377}')
    dag = context['task_instance_key_str']
    run_id = context['run_id']
    
    
    message = f'Исполнение DAG {dag} с id={run_id} не прошло!' # определение текста сообщения
    hook.send_message({
        'chat_id': '{-4118735826}',
        'text': message
    }) # отправление сообщения 