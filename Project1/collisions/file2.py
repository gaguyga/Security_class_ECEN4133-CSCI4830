#!/usr/bin/python3
# coding: latin-1
blob = """
                U��l�<`+Z����
�x[�x.g�J����v�/�S���6By���U���&��q=uK6����P�ǀ�}�����#p�!�+�W�_��˳6���U�
�3�g�/�	�1��_`'q'�8"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())
