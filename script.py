
Copy
import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from requests_html import HTMLSession

# Настройте параметры Telegram API
api_id = 123456
api_hash = 'abcdefg'
phone_number = '+1234567890'
channel_username = 'mychannel'

# Настройте параметры форума phpBB
forum_url = 'https://example.com/forum'
forum_username = 'myusername'
forum_password = 'mypassword'

# Войдите в Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

# Получите историю сообщений из канала Telegram
channel_entity = client.get_entity(channel_username)
messages = client(GetHistoryRequest(
    peer=PeerChannel(channel_entity.id),
    limit=100
))

# Войдите на форум phpBB
session = HTMLSession()
r = session.post(f'{forum_url}/ucp.php?mode=login', data={
    'username': forum_username,
    'password': forum_password
})

# Создайте тему на форуме
topic_title = 'Экспорт постов из Telegram канала'
topic_content = ''
for message in messages:
    topic_content += f'<p>{message.message}</p>'
topic_data = {
    'subject': topic_title,
    'message': topic_content,
    'forum': 1,
    'topictype': 'normal',
    'notify_watch': '1'
}
r = session.post(f'{forum_url}/posting.php?mode=post&f=1', data=topic_data)

# Выйдите из Telegram и phpBB
client.disconnect()
session.close()