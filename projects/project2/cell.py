



class Cell:

    def __init__(self, alive: bool) -> None:
        """
        Initializes the cell based on whether the input bool is True or False (Alive or Dead)
        """        
        self.__alive = alive
    
    def isAlive(self) -> bool:
        """
        Returns whether the cell is alive or dead as a bool
        """
        return self.__alive
    
    def kill(self) -> None:
        """
        Sets the cell to be dead
        """
        self.__alive = False

    def live(self) -> None:
        """
        Sets the cell to be alive
        """
        self.__alive = True

    def next_life(self, neighbors) -> bool:
        """
        Evaluates and saves whether the cell should be alive or dead in the next round
        """
        alive = 0
        for list in neighbors:
            for neighbor in list:
                if neighbor.isAlive():
                    alive+=1
        match alive:
            case 0 | 1:
                self.alive_next = False
            case 2:
                self.alive_next = self.__alive
            case 3:
                self.alive_next = True
            case _ if alive >= 4:
                self.alive_next = False
                

    def __repr__(self):
        """
        Living cell = 'X'
        Dead cell = '—'
        """
        if self.__alive:
            return "X"
        else:
            return "—"
        
    def __eq__(self, object) -> bool:
        """
        Equality for cells.
        Has to be a cell with the same isAlive status.
        """
        if isinstance(object, Cell):
            if self.__alive == object.isAlive():
                return True
            else:
                return False      
        else:
            return False
        