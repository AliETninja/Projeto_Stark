import starkbank
import os

current_dir = os.getcwd()
private_key, public_key = starkbank.key.create(current_dir)

print(private_key)
print(public_key)