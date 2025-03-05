
from random import randint
from time import sleep
from projects.project2.kbhit import KBHit


class GameController:
    
    def __init__(self) -> None:
        """
        Initializes the GameController. Sets sim mode to manual or automatic
        """
        self.past_boards = []
        self.mode = input("Do you want to simulate in Manual or Automatic mode?").strip().lower()
        if self.mode not in ['a', 'auto', 'automatic', 'm', 'manual']:
            raise ValueError("Must input a valid mode type")
    

    def check_boards(self, curr_grid) -> bool:
        """
        Checks if the simulation has stabilized (no board changes or repeating patterns)
        """
        boardeq = 0
        for board in self.past_boards[::-1]:
            if board == curr_grid:
                boardeq += 1
            else:
                break
        if boardeq >= 3:
            return True
        if len(self.past_boards) >= 5:
            return all(board == curr_grid for board in self.past_boards[-1::-2])


    def run(self, curr_grid) -> None:
        """
        Main running of the simulation
        """
        kb = KBHit()
        gen = 1
        finished = False
        while not finished:
            print(f"Generation {gen}:")
            for element in curr_grid:
                print(*element)
            print(" ")
            if self.mode in ["manual", "m"]:
                while True:
                    if kb.kbhit():
                        kg = kb.getch()
                        if kg == "s":
                            break
                        elif kg == "a":
                            self.mode = "a"
                            print("Mode switched to 'automatic'")
                            sleep(1)
                            break
                        elif kg == "q":
                            print("Simulation quit")
                            exit()
            elif self.mode in ["automatic", "a", "auto"]:
                while True:
                    sleep(1)
                    if kb.kbhit():
                        kg = kb.getch()
                        if kg == "m":
                            self.mode = "m"
                            print("Mode switched to 'manual'")
                            sleep(1)
                            break
                        elif kg == "q":
                            print("Simulation quit")
                            exit()
                        else:
                            break
                    else:
                        break

            self.past_boards.append(curr_grid.copy())
            if len(self.past_boards) > 5:
                self.past_boards.pop(0)
            
            finished = self.check_boards(curr_grid)
            
            for row in range(len(curr_grid)):
                for col in range(len(curr_grid[0])):
                    curr_grid[row][col].next_life(curr_grid.check3x3(row, col))

            for row in range(len(curr_grid)):
                for col in range(len(curr_grid[0])):
                    if curr_grid[row][col].alive_next:
                        curr_grid[row][col].live()
                    else:
                        curr_grid[row][col].kill()

            gen += 1

            
        print("Simulation Stabilized")