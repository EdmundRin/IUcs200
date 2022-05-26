################################
# PROBLEM 1
################################
# In this starter code (different from the pdf), we have also
# added a blank `get` function but you are free to remove it or name it
# differently (but appropriately) to implement the functionality.
# A `get` function is used to obtain the value for objects of a given class.
# For example, in this case since it's Fractions so if I call get on an object of this class
# then the get function should retiurn the reduced representation for that Fraction.
# This could come handy for implementing other related functions in this class.
class Fraction:
    def __init__(self, numerator, denominator):
        from math import gcd
        self.numerator = numerator
        # check if the denominator is zero
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        else:
            self.denominator = denominator
        # check if the denominator is negative
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        # reduce the fraction
        gcd1 = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd1
        self.denominator = self.denominator // gcd1

    def get(self):
        # I'm still very confused about this get function
        from math import gcd
        gcd1 = gcd(self.numerator, self.denominator)
        # The comment means that the fraction should be returned in the following way
        return Fraction(self.numerator // gcd1, self.denominator // gcd1)
        # But shouldn't this step already be implemented in __init__?
        # Or am I wrong in thinking that this function returns a human-readable string?

    def __add__(self,other):
        new_nume = self.numerator * other.denominator + self.denominator * other.numerator
        new_deno = self.denominator * other.denominator
        return Fraction(new_nume, new_deno)
    
    def __mul__(self,other):
        new_nume = self.numerator * other.numerator
        new_deno = self.denominator * other.denominator
        return Fraction(new_nume, new_deno)

    def __repr__(self):
        if self.numerator < self.denominator:
            return "Frac(" + str(self.numerator) + "/" + str(self.denominator) + ")"
        else:
            return "Frac(" + str(self.numerator // self.denominator)\
                 + "," + str(self.numerator % self.denominator)\
                 + "/" + str(self.denominator) + ")"

    def __eq__(self,other):
        return self.numerator == other.numerator and self.denominator == other.denominator


################################
# PROBLEM 2
# You likely will need some additional functions
################################

#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    # confused about the modulus:
    # alphabet = "abcdefghijklmnopqrstuvwxyz{"
    # for i in range(27):
        # if letter == alphabet[i]:
            # return alphabet[(i + n) % 27]
    new = chr(ord(letter) + n)
    if new > "z":
       return chr(ord(letter) + n - 27)
    else:
        return new

#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    old = chr(ord(letter) - n)
    if old < "a":
        return chr(ord(letter) - n + 27)
    else:
        return old

#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    new = ""
    _sentence = sentence.replace(" ", "{")
    for i in range(len(_sentence)):
        new += encrypt(_sentence[i], shift)
    return new

#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    old = ""
    for i in range(len(sentence)):
        old += decrypt(sentence[i], shift)
    return old.replace("{", " ")


################################
# PROBLEM 3
################################

#the dictionary for the transation
aa_d = {}
#the FASTA file
DNA_d = []

#the translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"


# INPUT path and file name of amino acid file
# RETURN a dictionary 
# Key is a tuple (c0, c1, ... , cn) where ci are codons
# Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(path,name):
    with open (path + "/" + name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip("\n")
            line = line.split(", ")
            aa_d[tuple(line[2:])] = [line[0], line[1]]
    return aa_d

# INPUT path and file name of amino acid file
# RETURN a list [header, DNA]
# header is first line in the file
# DNA is a string of letters from remainder of file
# no whitespace
def get_DNA(path,name):
    with open (path + "/" + name, "r") as f:
        lines = f.readlines()
        header = lines[0].rstrip("\n")
        DNA = ""
        for line in lines[1:]:
            line = line.strip()
            DNA += line
    return [header, DNA]


#INPUT FAST file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    protein = ""
    for i in range(0, len(DNA_d[1]), 3):
        codon = DNA_d[1][i:i+3]
        for key in aa_d:
            if codon in key:
                protein += aa_d[key][1]
    return protein

# Here is how we set the path and file name as function arguments
# This is done assuming that you run the code from within Assignment7 directory.
# Based on differences in our paths (could be differet based on how VSC is configured on your system), y
# you may or may not need to modify the path i.e. 'Assignment7'. We suggest that you try this asap and
# if file could not be found then, you revise the File IO concepts from lectures/labs
# to properly set the path in these functions.
aa_d = get_amino_acids("Assignment7", "amino_acids.txt")
DNA_d = get_DNA("Assignment7", "DNA.txt")
protein = translate(DNA_d)



################################
# PROBLEM 4
################################
# In this problem we will build a class that allows us to capture a single variable function of x
# and evaluation of the function for a given input (i.e. the value of x), the derivative at an input,
# and integral over an interval.

# The class constructor takes a Python expression of x as a string and evaluates it.
class Function:
    def __init__(self,expression):
        self.expression = expression

    def point(self,x):
        return eval("lambda x: " + self.expression)(x)
        

    def integral(self,x,y):
        h = (y - x) / 4
        d = [x, x + h, x + 2*h, x + 3*h, x + 4*h]
        return (h/3)*(self.point(d[0]) + self.point(d[4]) + \
               4*(self.point(d[1]) + self.point(d[3])) + \
               2*self.point(d[2]))
    
    def derivative_at_point(self,x):
        h = 0.000005
        return (self.point(x+h)-self.point(x-h))/(2*h)

    def __repr__(self):
        return self.expression




if __name__ == "__main__":
    
    #PROBLEM 1
    x = 2*3*5
    y = 2*3*7
    a = Fraction(x,y)
    print(a)
    b = Fraction(1,2)
    c = Fraction(4,5)
    d = b + c
    e = b*c
    print(f"{b} + {c} = {d}")
    print(f"{b} * {c} = {e}")
    print(Fraction(6,2))
    zz = Fraction(2,4)
    print(zz,b)
    print(zz == b)
    print(b + b == b)


    #PROBLEM 2
    sentence = "this is a secret message about the class"
    shift = 5
    secret = encrypt_sentence(sentence, shift)
    decode_secret = decrypt_sentence(secret, shift)
    
    print(f"original: {sentence}")
    print(f"encrypted: {secret}")
    print(f"decrypted: {decode_secret}")

    #PROBLEM 3
    print("Dictionary")
    print(aa_d)
    print("FASTA file")
    print(DNA_d)
    print("Translations match:", str(protein == actual))

    # # should return "PLHS"    
    print(translate(["nothing", "CCACTGCACTCA"]))

    # # should returns "D-"
    print(translate(["nothing", "GACTAA"]))

    #PROBLEM 4
    
    f0 = Function("1/x")
    f1 = Function("x**2 - x")
    f2 = Function("x**2")

    print(f0)
    print(f1)
    print(f2)

    print(f0.point(10))
    print(f1.point(2))
    print(f2.point(3))

    print(f0.derivative_at_point(10))
    print(f1.derivative_at_point(2))
    print(f2.derivative_at_point(3))

    print(f0.integral(1,2))
    print(f1.integral(1,4))
    print(f2.integral(0,3))