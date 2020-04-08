MESSAGES = {
    'weather_for_location_retrieval_failed': 'Не получилось узнать погоду в этой локации 😞,' + \
         'предлагаем посмотреть, какая погода за окном. \n\n /help - инструкция по использованию бота.',

    'general_failure': 'Я такое не умею 😞.\n\n /help - инструкция по использованию бота.',

    'weather_in_city_message': 'Погода в городе {}:\n {}.',

    'weather_in_location_message': 'Погода в указанной локации {}:\n {}.'
}

def get_message(message_key: str):
    return MESSAGES[message_key]
