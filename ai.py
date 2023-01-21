import copy
import math
import random
import evalute


class AI_Module():

    def __init__(self,board,level,player):
        self.board = board
        self.level = level
        self.player = player


    def rnd(self,mainboard):
        empty_sqrs = evalute.get_empty_sqrs(mainboard)
        idx = random.randrange(0,len(empty_sqrs))
        return empty_sqrs[idx]

    #minimax
    def minimax(self,board,maximizing):
        case = evalute.checkWin(board)
        if case == 1:
            return 1,None
        
        elif case == 2:
            return -1,None
        
        elif evalute.is_full(board):
            return 0,None

        if maximizing:
            max_eval = -100
            bestmove = None
            empty_sqrs = evalute.get_empty_sqrs(board)
            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                evalute.mark_sqr(temp_board,row,col,1)
                eval = self.minimax(temp_board,False)[0]
                if eval>max_eval:
                    max_eval = eval
                    bestmove = (row,col)
            return max_eval,bestmove

        elif not maximizing:
            min_eval = 100
            bestmove = None
            empty_sqrs = evalute.get_empty_sqrs(board)
            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                evalute.mark_sqr(temp_board,row,col,2)
                eval =self.minimax(temp_board,True)[0]
                if eval<min_eval:
                    min_eval = eval
                    bestmove = (row,col)
            return min_eval,bestmove

    def eval(self):
        board = self.board
        level = self.level
        if level == 0:
            eval ="random"
            move = self.rnd(board)

        elif level == 1 :
            Maximizing_or_not = True if self.player == 1 else False 
                 
            eval,move = self.minimax(board,Maximizing_or_not)
            print(f"Ai has chose to mark the sqaure in pos {move} with an eval of :{eval} ")    
        return move
