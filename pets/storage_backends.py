from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    """
    Classe personalizada para garantir que os arquivos sejam públicos.
    """
    location = ''  # define a pasta onde os arquivos serão armazenados
    default_acl = 'public-read'  # torna os arquivos públicos assim que são carregados
    file_overwrite = False