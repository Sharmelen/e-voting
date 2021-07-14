from xpxchain import models
from xpxchain import client

public_key = "fa56e8d029fafe8a2d94195ecef9a89fa6757e83bb5b315fab89cbee524b5ace"
ENDPOINT = "https://bctestnet1.brimstone.xpxsirius.io"
account = models.PublicAccount.create_from_public_key(public_key, models.NetworkType.TEST_NET)
tx_list = []

f = open("vote_receipt.txt","w")

with client.AccountHTTP(ENDPOINT) as http:


	decor1 = "######################################################\n"					
	title = "This is a list of all transaction that has occured\n"					
	decor2 = "######################################################\n\n"
	f.write(decor1+title+decor2)
	
	txns = http.transactions(account)
	for x in range (len(txns)):
		
		first_strip = str(txns[x]).strip("',")
		transaction_array = first_strip.split("=")
		transaction_hash = transaction_array[17].strip("', merkle_component_hash")
		sender_signature = transaction_array[7].strip("', signer")
		sender_address = transaction_array[10].strip("', network_type")
		
		if str(transaction_array[1]) == "<TransactionType.TRANSFER: 16724>, network_type":
		
			try:
				payload = transaction_array[28].strip("')b'")
				
			except:
				print("This is a contract transactions")
				
				
			datetime_raw = transaction_array[5].strip("datetime. max_fee ( )),")
			datetime_array = datetime_raw.split(",")
			date = datetime_array[2]+"/"+datetime_array[1].strip(" ")+"/"+datetime_array[0].strip(" ")
			time = datetime_array[3]+":"+datetime_array[4].strip(" ")
			receipient_address = transaction_array[20].strip("', network_type")
			block_number = transaction_array[14].strip(", index")
			
			tx_date = "Transaction Date: "+date
			split_time = str(time).split(":")
			
			if len(str(split_time[1])) < 2:
				time = str(time)+"0"
				final_time = "\nTransaction Time: "+time +"\n"
				
			else:
				final_time = "\nTransaction Time: "+time +"\n"
				
				
			
			
			block_num = "Block Number: "+block_number+"\n"
			
			content = "Message Content: "+payload+"\n"
			
			tx_hash = "Transaction Hash: "+transaction_hash+"\n"
		
			
			sender_sign = "Sender Signature: "+sender_signature+"\n"
			
			sender_addr = "Sender Address: "+sender_address+"\n"
			
			
			recv_addr = "Receipient Address: "+receipient_address+"\n"
			
			
			decor = '***************************************************\n'
											
			append_tnxs = tx_date + final_time + sender_addr + recv_addr + content + tx_hash + sender_sign + block_num + decor
			f.write(append_tnxs)
			
			#print("Please check file named 'vote_receipt.txt' ")
		
