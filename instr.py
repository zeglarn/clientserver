class Instr:
    """
    Instructions sent over tcp.
    """

    def __init__(self):
        self.fwd = False
        self.bkwd = False
        self.left = False
        self.right = False
        self.start = False
        self.stop = False
        self.quit = False

    def printSelf(self):
        print("Forward:\t", self.fwd)
        print("Backward:\t", self.bkwd)
        print("Left:\t\t", self.left)
        print("Right:\t\t", self.right)
        print("Start:\t\t", self.start)
        print("Stop:\t\t", self.stop)
        print("Quit:\t\t", self.quit)

    def forward(self, fwd):
        self.fwd = fwd

    def backward(self, bkwd):
        self.bkwd = bkwd

    def turnLeft(self, left):
        self.left = left

    def turnRight(self, right):
        self.right = right

    def doStart(self, start):
        self.start = start

    def doStop(self, stop):
        self.stop = stop

    def disconnect(self, quit):
        self.quit = quit
