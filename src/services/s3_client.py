from typing import Final

import boto3

bucket_name_pari_proofs: Final[str] = 'pari-proofs'


class ProofManager:
    def __init__(self):
        self.__s3 = boto3.client(
            service_name='s3',
            aws_access_key_id='test',
            aws_secret_access_key='test',
            endpoint_url='http://localhost:4566',
        )
        self.__s3.create_bucket(Bucket=bucket_name_pari_proofs)
        super().__init__()

    def put_proof_to_s3(self, proof_id: int, proof_file: bytes):
        self.__s3.put_object(Bucket=bucket_name_pari_proofs, Key=str(proof_id), Body=proof_file)

    def get_proof_from_s3(self, proof_id: int):
        self.__s3.get_object(Bucket=bucket_name_pari_proofs, Key=str(proof_id))
