import time
from tqdm.auto import tqdm

text=input("Enter the text to encrypt : ")
rot=int(input("Enter the number of shift : "))

text=text.upper()
letters='ABCEDFGHIJKLMNOPQRSTUVWXYZ'
ciphertext=''

bar=tqdm(total=len(text),position=0,leave=False)
for c in text:
	
	bar.set_description('Encrypting {}'.format(c))
	bar.update()

	time.sleep(1)

	if(c==' '):
		ciphertext+=' '
	else:
		shift=letters.find(c)+ rot
		if(shift>25):
			shift=shift%25
		ciphertext+=letters[shift]
#bar.close()
print('\nROT ',(rot),' CipherText : ',ciphertext)