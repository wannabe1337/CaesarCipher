import time
from tqdm.auto import tqdm

ciphertext=input("Enter the Cipher Text to Decrypt : ")
rot=int(input("Enter the number of shift : "))
ciphertext=ciphertext.upper()

letters='ABCEDFGHIJKLMNOPQRSTUVWXYZ'
plaintext=''

bar=tqdm(total=len(ciphertext),position=0,leave=False)
for c in ciphertext:
	
	bar.set_description('Decrypting {}'.format(c))
	bar.update()
	time.sleep(0.05)

	if(c==' '):
		plaintext+=' '
	else:
		shift=letters.find(c)
		if(shift<rot):
			shift=shift+25-rot
		else:
			shift=shift-rot
		plaintext+=letters[shift]
#bar.close()
print('\nROT ',(rot),' Decrypted PlainText : ',plaintext)