import unittest

class PTBSL(unittest.TestCase):
	def test_xor_1bytes(self):
		import ptbsl.bsl

		self.assertEqual(ptbsl.bsl.xor(b'\x80'), b'\x80'[0])
	
	def test_xor_2bytes(self):
		import ptbsl.bsl

		self.assertEqual(ptbsl.bsl.xor(b'\x80\x04'), b'\x84'[0])
		self.assertEqual(ptbsl.bsl.xor((1, 2)), 3)
	
	def test_xor_3bytes(self):
		import ptbsl.bsl

		self.assertEqual(ptbsl.bsl.xor(b'\x80\x00\x00'), b'\x80'[0])
	
	def test_xor_4bytes(self):
		import ptbsl.bsl

		self.assertEqual(ptbsl.bsl.xor(b'\x80\x00\x00\x00'), b'\x80'[0])

	def test_neg_xor_4bytes(self):
		import ptbsl.bsl

		self.assertEqual(~ptbsl.bsl.xor(b'\x80\x00\x00\x00') & 0xFF, 0X7F)

	def test_hexstr_to_bytes(self):
		import ptbsl.bsl
		self.assertEqual(ptbsl.bsl.hexstr_to_bytes('80 14 04 04 00 0F 0E 00'), b'\x80\x14\x04\x04\x00\x0F\x0E\x00')

	def test_checksum(self):
		import ptbsl.bsl

		self.assertEqual(ptbsl.bsl.checksum(b'\x80\x14\x04\x04\x00\x0F\x0E\x00'), (0X75, 0XE0))
		self.assertEqual(ptbsl.bsl.checksum(ptbsl.bsl.hexstr_to_bytes('80 00 0E 0E F2 13 40 40 00 00 00 00 00 00 02 01 01 01')), (0xC0, 0XA2))
