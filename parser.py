Pieces = {}
def Register(Piece):
    Pieces[Piece.__name__] = Piece
    return Piece

class StrongholdPiece:
    def __init__(self, RawParts, Index):
        self.PieceName = RawParts[0]
        self.Index = Index
        try:
            self.ChildrenIndices = list(map(int, RawParts[1:]))
        except:
            self.ChildrenIndices = [-1]

@Register
class PortalRoom(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ExitIndex, = [-1]
@Register
class Library(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ExitIndex, = [-1]

@Register
class SmallCorridor(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ExitIndex, = [-1]

@Register
class LeftTurn(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class RightTurn(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class PrisonHall(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class SpiralStaircase(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class Start(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class Stairs(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices

@Register
class ChestCorridor(StrongholdPiece):
    def __init__(self, RawPiece, Index):   
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, = self.ChildrenIndices  

@Register
class Corridor(StrongholdPiece):
    def __init__(self, RawPiece, Index):   
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, self.LeftExitIndex, self.RightExitIndex = self.ChildrenIndices  

@Register
class SquareRoom(StrongholdPiece):
    def __init__(self, RawPiece, Index):   
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, self.RightExitIndex, self.LeftExitIndex = self.ChildrenIndices  

@Register
class FiveWayCrossing(StrongholdPiece):
    def __init__(self, RawPiece, Index):
        super().__init__(RawPiece, Index)
        self.ForwardExitIndex, self.BottomRightExitIndex, self.TopRightExitIndex, self.BottomLeftExitIndex, self.TopLeftExitIndex = self.ChildrenIndices

class DeadendPiece:
    def __init__(self):
        self.PieceName = "Deadend"

Deadend = DeadendPiece()
StructuredPieceList = list()

RawPieceList = open("./sample_layout.txt", "r").read().split("\n")[2:-2]
TotalRooms = len(RawPieceList)

for Index in range(TotalRooms):
    RawParts = RawPieceList[Index].split()
    PieceName = RawParts[0]
    StructuredPieceList.append(Pieces[PieceName](RawParts, Index))
StructuredPieceList.append(Deadend)

#AdjacencyLists = list((StructuredPieceList[Index], list(StructuredPieceList[ChildIndex] for ChildIndex in StructuredPieceList[Index].ChildrenIndices)) for Index in range(TotalRooms))

print(*reversed(list((str(Index)+". "+StructuredPieceList[Index].PieceName, list(str(ChildIndex)+". "+StructuredPieceList[ChildIndex].PieceName for ChildIndex in StructuredPieceList[Index].ChildrenIndices)) for Index in range(TotalRooms))), sep='\n')