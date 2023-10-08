import boto3
from django.conf import settings


class Bicker:
    def __init__(self) -> None:
        session = boto3.Session()
        self.conn = session.client(
            service_name=settings
        )
