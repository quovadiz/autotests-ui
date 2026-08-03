import sys
import platform
from config import settings


def create_allure_environment_file():
    env_data = settings.model_dump()
    env_data.update({
        'os_info': f'{platform.system()}, {platform.release()}',
        'python_version': sys.version
    })

    content = '\n'.join([f'{key}={value}' for key, value in env_data.items()])

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(content)

