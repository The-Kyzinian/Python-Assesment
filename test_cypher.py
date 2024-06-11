import unittest
import cypher_helper

class TestEncryptDecrypt(unittest.TestCase):

    def test_encrypt(self):
        input = "bcd"
        expected = 'cde'
        r = cypher_helper.encrypt(input,1)
        self.assertEqual(r,expected)
    
    def test_decrypt(self):
        input = "cde"
        expected = 'bcd'
        r = cypher_helper.decrypt(input,1)
        self.assertEqual(r,expected)
        
    def test_encrypt_therinas(self):
        input = "THERINAStherinas"
        expected = 'HTRENISAhtrenisa'
        r = cypher_helper.encrypt(input,0)
        self.assertEqual(r,expected)

    def test_decrypt_therinas(self):
        input = "HTRENISAhtrenisa"
        expected = 'THERINAStherinas'
        r = cypher_helper.decrypt(input,0)
        self.assertEqual(r,expected)
    
    def test_encrypt_decrypt_num(self):
        input = "1234567890"
        expected = '1234567890'
        rencrypt = cypher_helper.encrypt(input,1)
        rdecrypt = cypher_helper.decrypt(input,1)
        self.assertEqual(rencrypt,expected)
        self.assertEqual(rdecrypt,expected)

    def test_encrypt_decrypt_sym(self):
        input = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
        expected = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
        rencrypt = cypher_helper.encrypt(input,1)
        rdecrypt = cypher_helper.decrypt(input,1)
        self.assertEqual(rencrypt,expected)
        self.assertEqual(rdecrypt,expected)
    
    def test_encrypt_decrypt_quotes(self):
        input = '""'
        expected = '""'
        rencrypt = cypher_helper.encrypt(input,1)
        rdecrypt = cypher_helper.decrypt(input,1)
        self.assertEqual(rencrypt,expected)
        self.assertEqual(rdecrypt,expected)
        
    def test_encrypt_decrypt_space(self):
        input = ' '
        expected = ' '
        rencrypt = cypher_helper.encrypt(input,1)
        rdecrypt = cypher_helper.decrypt(input,1)
        self.assertEqual(rencrypt,expected)
        self.assertEqual(rdecrypt,expected)
    
    def test_encrypt_therinas_shifted(self):
        input = "THERINAStherinas"
        expected = 'IUSFOJTBiusfojtb'
        r = cypher_helper.encrypt(input,1)
        self.assertEqual(r,expected)

    def test_decrypt_therinas_shifted(self):
        input = "IUSFOJTBiusfojtb"
        expected = 'THERINAStherinas'
        r = cypher_helper.decrypt(input,1)
        self.assertEqual(r,expected)
    
    def test_encrypt_capitals(self):
        input = "BCD"
        expected = 'CDE'
        r = cypher_helper.encrypt(input,1)
        self.assertEqual(r,expected)
    
    def test_decrypt_capitals(self):
        input = "CDE"
        expected = 'BCD'
        r = cypher_helper.decrypt(input,1)
        self.assertEqual(r,expected)
if __name__ == '__main__':
    unittest.main()
