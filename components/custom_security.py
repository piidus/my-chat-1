from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA private and public keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

def generate_message(input_text):
    # Convert input text to bytes
    message = str(input_text).encode('utf-8')
    # print("Original Message:", message)

    # Load the public key for encryption
    public_key_obj = RSA.import_key(public_key)
    cipher_encrypt = PKCS1_OAEP.new(public_key_obj)
    encrypted_message = cipher_encrypt.encrypt(message)

    # Load the private key for decryption
    private_key_obj = RSA.import_key(private_key)
    cipher_decrypt = PKCS1_OAEP.new(private_key_obj)
    decrypted_message = cipher_decrypt.decrypt(encrypted_message)
    
    return encrypted_message, decrypted_message

if __name__ == '__main__':
    encrypted_message, decrypted_message = generate_message('Hello, World!')

    # Print results
    print("Encrypted Message:\n", encrypted_message)
    print("Decrypted Message:\n", decrypted_message.decode('utf-8'))
