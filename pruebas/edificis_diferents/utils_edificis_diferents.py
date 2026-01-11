import numpy as np

def gradable(func):
    def cc_vv(row):
        c_i = 0
        counter = 0
        for i in row:
            if i == 0:
                break
            if i > c_i:
                counter += 1
                c_i = i
        return counter
    


    def receiver(*args, **kwargs):
        top = args[0]
        bottom = args[1]
        left = args[2]
        right = args[3]
        if "grading" in kwargs:
            kwargs.pop("grading")

            solution = func(*args, **kwargs)
            if not solution:
                return False
            solution = np.array(solution)

            for i in range(len(solution[0])):
                if top[i] != 0 and top[i] != cc_vv(solution[:,i]):
                    return False

            for i in range(len(solution[0])):
                if bottom[i] != 0 and bottom[i] != cc_vv(solution[::-1,i]):
                    return False

            for i in range(len(solution)):
                if left[i] != 0 and left[i] != cc_vv(solution[i,:]):
                    return False
            
            for i in range(len(solution)):
                if right[i] != 0 and right[i] != cc_vv(solution[i,::-1]):
                    return False
            
            return True
        else:
            solution = func(*args, **kwargs)
            if solution:
                print(format_sky(np.array(solution), top, bottom, left, right))
            else:
                print('No solution found')
    return receiver


def format_sky(board, top, bottom, left, right):
    """
    Funció auxiliar per mostrar la matriu del Problema 1 en forma de graella.
    """
    _str = ""
    
    # Files
    for v in top:
        _str+="   "+str(v)
    _str = "  " + _str + "\n"

    for idx, i in enumerate(board):
        _str+= "   +"+ ("-"*((board.shape[1]*4)-1)) +"+\n"
        _str+= f" {left[idx]} | "
        
        # Columnes
        for j in i:   
            if j!=0:
                _str+= str(j)+" | "
            else:
                 _str+= "  | "
            
        _str+= f"{right[idx]} \n"
    _str+= "   +"+ ("-"*((board.shape[1]*4)-1))+"+\n"
    
    _bot = ""
    for v in bottom:
        _bot+="   "+str(v)
    _str += "  " + _bot
    
    return _str.replace('0',' ')