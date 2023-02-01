import TOKENS
from YA_API import YA
from VK_API import VK

access_token_ya = TOKENS.token_disk
user_id = input('Введите токен вашего яндекс диска: ')
owner_id = input('Введите ID пользователя фотографии которого хотите сохранить: ')
vk = VK(TOKENS.token_vk, TOKENS.id)
res = vk.users_foto(owner_id)
YA(access_token_ya).create_folder(owner_id)
YA(access_token_ya).upload_foto(owner_id, res)
