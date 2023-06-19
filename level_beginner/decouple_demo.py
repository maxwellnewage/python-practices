"""
Decouple implementado sobre un directorio
custom para leer variables de configuración.
"""
from decouple import Config, RepositoryEnv
import os

if __name__ == '__main__':
    # busco el path absoluto de este archivo
    dirname = os.path.dirname(os.path.realpath(__file__))
    # lo fusiono con config/.env
    env_path = os.path.join(dirname, 'config', '.env')
    # armo una custom config basada en ese path
    env_config = Config(RepositoryEnv(env_path))

    # me traigo las variables de configuración
    print(f"username: {env_config.get('USERNAME', '')}")
    print(f"password: {env_config.get('PASSWORD', '')}")
