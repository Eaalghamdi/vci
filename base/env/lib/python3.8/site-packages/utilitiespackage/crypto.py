"""
This simple module is used anytime something needs to be encrypted with
aes 256 on the server. Encryption is accomplished with a subprocess call
to openssl. The Popen calls here are ment to be very strict i.e. shell=False
and the 'executable' option.
"""

from subprocess import Popen, PIPE


def aes_encrypt(plaintext, password):
    """
    This runs a command equivilent to:
    
        echo $plaintext | openssl enc -aes-256-cbc -a -A -k $password

    to produce ciphertext.
    """
    p0 = Popen(["1", plaintext], shell=False, stdout=PIPE, executable="echo")
    p1 = Popen(["1", "enc", "-aes-256-cbc", "-a", "-A", "-k", password], shell=False, stdin=p0.stdout, stdout=PIPE, executable="openssl")
    ciphertext = p1.communicate()[0].rstrip()
    return ciphertext


def aes_decrypt(ciphertext, password):
    """
    This runs a command equivilent to:
    
        echo $ciphertext | openssl enc -aes-256-cbc -a -A -d -k $password

    to produce plaintext.
    """
    p0 = Popen(["1", ciphertext], shell=False, stdout=PIPE, executable="echo")
    p1 = Popen(["1", "enc", "-aes-256-cbc", "-a", "-A", "-d", "-k", password], shell=False, stdin=p0.stdout, stdout=PIPE, executable="openssl")
    plaintext = p1.communicate()[0].rstrip()
    return plaintext
