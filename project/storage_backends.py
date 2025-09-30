from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'          # Nome do subdiretório para arquivos de mídia
    file_overwrite = False      # Impede que arquivos com o mesmo nome sejam sobrescritos