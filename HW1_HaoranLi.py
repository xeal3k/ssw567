import unittest

def classifyTriangle(a,b,c):
    """
    This will test whether it is a triangle. After that, it will determine which kind of triangle it is.
    """
    if type(a) != int and type(a) != float:
        return 'NotATriangle'
    elif type(b) != int and type(b) != float:
        return 'NotATriangle'
    elif type(c) != int and type(c) != float:
        return 'NotATriangle'

    if a + b <= c or a + c <= b or c + b <= a:
        return 'NotATriangle'
    elif a <= 0 or b <= 0 or c<= 0:
        return 'NotATriangle'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == c**2:
        return 'Right'
    elif a == b and b == c:
        return 'Equilateral'
    elif b == c or a == c or b == c:
        return 'Isoscele'
    return 'RegularTriangle'


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        self.assertNotEqual(classifyTriangle('3',4,5),'Right',"'3',4,5 is a NotATriangle")
        self.assertNotEqual(classifyTriangle(3,-4,5),'Right',"'3',4,5 is a NotATriangle")
        self.assertNotEqual(classifyTriangle(3,10,5),'Right',"'3',4,5 is a NotATriangle")

    def testMyTestSet2(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(10,25,30),'RegularTriangle','Should be RegularTriangle')
        self.assertEqual(classifyTriangle(9,12,15),'Right','Should be Right')


def main():
    a = input("The length of the first lateral is ")
    try:
        a = float(a)
    except ValueError:
        raise ValueError("The length of the first lateral is wrong.")

    b = input("The length of the second lateral is ")
    try:
        b = float(b)
    except ValueError:
        raise ValueError("The length of the second lateral is wrong.")

    c = input("The length of the third lateral is ")
    try:
        c = float(c)
    except ValueError:
        raise ValueError("The length of the third lateral is wrong.")

    print("This triangle is ", classifyTriangle(a,b,c))

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)

    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)

main()
