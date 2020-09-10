import math

class Convert():
	"""docstring for Convert"""
	def __init__(self):
		super(Convert, self).__init__()
		self.B_TO_HEX = {"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8",
		"1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
		self.HEX_TO_B = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000",
		"9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
		

		self.choice = input("""
		Please make your choice

		1 - From Binary to Decimal and hexa
		2 - From Decimal to binary and hexa	
		3 - From hexa to decimal and binary

		""")

		if(self.choice == "1"):
			self.fromBinary()
		elif(self.choice == "2"):
			self.fromDecimal()
		elif(self.choice == "3"):
			self.fromHexa()

	def fromBinary(self):
		binaryInput = int(input("\n\nPlease enter your binary : "))
		bOld = binaryInput

		#if the lenght can't be divided by 4, we fill with zeros
		if(len(str(binaryInput))%4 != 0):
			nextFactor = 0
			for i in range(1,4):
				if((len(str(binaryInput)) + i)%4 == 0):
					nextFactor = len(str(binaryInput)) + i
					#print("Il faut rajouter " + str(i) + " zéros")
					#print(str(binaryInput).zfill(nextFactor))
					binaryInput = str(binaryInput).zfill(nextFactor)
					break

			

		reverseBinary = ""

		# let's start with the decimal conversion
		decimalSum = 0

		for i in range(1, len(str(binaryInput)) + 1):
			#print(str(binaryInput)[ len(str(binaryInput)) - i ] + " : rang " + str(i-1))
			if( int(str(binaryInput)[ len(str(binaryInput)) - i ]) == 1):
				decimalSum += math.pow(2, i-1 )

		#Now for the hexadecimal form
		nibbleArray = []
		hexArray = []

		#we reverse the binary, and in this way it will be easier
		for y in range(0, len(str(binaryInput))):
			#print( str(binaryInput)[ len(str(binaryInput)) - 1 - y  ] )
			reverseBinary += str(binaryInput)[ len(str(binaryInput)) - 1 - y  ]
		
		
		
				
		for z in range(1,len(reverseBinary) + 1):

			if(z%4 == 0):
				#print(reverseBinary[z-1])
				nibble = ""
				for k in range(z-4,z):
					#print(reverseBinary[k])
					nibble += reverseBinary[k]

				#we had the nibble
				nibbleArray.insert(0,nibble[::-1])
			#print(" ")

		
		for x in range(0,len(nibbleArray)):
			hexArray.append(self.B_TO_HEX[nibbleArray[x]])

		hexForm = ""

		for y in range(0,len(hexArray)):
			hexForm += hexArray[y]


		print(f'''
		Results for {bOld} :

		Decimal form : {decimalSum}
		Hexadecimal form : 0x{hexForm}

			''')


		

	def fromDecimal(self):
		decimalInput = int(input("\n\nPlease enter your decimal : "))

		remainderArray = []

		dividende = decimalInput

		while(math.floor(dividende/2) != 0):
			#print(f"{dividende}/2")
			remainderArray.append(dividende%2)
			if(math.floor(dividende/2) != 1):
				dividende = math.floor(dividende/2)
			else:
				remainderArray.append(1)
				dividende = math.floor(dividende/2)


		binaryForm = ""

		for g in range(0,len(remainderArray)):
			binaryForm += str(remainderArray[g])


		binaryInput = binaryForm[::-1]
		bOldd = binaryInput

		#if the lenght can't be divided by 4, we fill with zeros
		if(len(str(binaryInput))%4 != 0):
			nextFactor = 0
			for i in range(1,4):
				if((len(str(binaryInput)) + i)%4 == 0):
					nextFactor = len(str(binaryInput)) + i
					#print("Il faut rajouter " + str(i) + " zéros")
					#print(str(binaryInput).zfill(nextFactor))
					binaryInput = str(binaryInput).zfill(nextFactor)
					break

			

		reverseBinary = ""

		#Now for the hexadecimal form
		nibbleArray = []
		hexArray = []

		#we reverse the binary, and in this way it will be easier
		for y in range(0, len(str(binaryInput))):
			#print( str(binaryInput)[ len(str(binaryInput)) - 1 - y  ] )
			reverseBinary += str(binaryInput)[ len(str(binaryInput)) - 1 - y  ]
		
		
		
				
		for z in range(1,len(reverseBinary) + 1):

			if(z%4 == 0):
				#print(reverseBinary[z-1])
				nibble = ""
				for k in range(z-4,z):
					#print(reverseBinary[k])
					nibble += reverseBinary[k]

				#we had the nibble
				nibbleArray.insert(0,nibble[::-1])
			#print(" ")

		
		for x in range(0,len(nibbleArray)):
			hexArray.append(self.B_TO_HEX[nibbleArray[x]])

		hexForm = ""

		for y in range(0,len(hexArray)):
			hexForm += hexArray[y]

		print(f'''
		Results for {decimalInput} :

		Binary form : 0b{bOldd}
		Hexadecimal form : 0x{hexForm}

			''')
		

	def get_key(self,val):

		for key, value in self.B_TO_HEX.items():
                                              if(val == value):
                                                      return key


	def fromHexa(self):
		hexaInput = input("\n\nPlease enter your hexa : ")

		binaryForm = ""

		for i in range(0,len(hexaInput)):
			binaryForm += self.HEX_TO_B[hexaInput[i]]

		# let's start with the decimal conversion
		decimalSum = 0

		for i in range(1, len(str(binaryForm)) + 1):
			#print(str(binaryForm)[ len(str(binaryForm)) - i ] + " : rang " + str(i-1))
			if( int(str(binaryForm)[ len(str(binaryForm)) - i ]) == 1):
				decimalSum += math.pow(2, i-1 )


		print(f'''
		Results for 0x{hexaInput} :

		Decimal form : {decimalSum}
		Binary form : 0b{binaryForm}

			''')


if __name__ == '__main__':
	Convert()
