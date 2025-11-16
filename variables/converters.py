
def cm_to_inches(cm):
    """Funkcja konwertuje centymetry na cale"""
    return cm / 2.54

def ft_inch_to_cm(feet, inches):
    """Funkcja konwertuje stopy i cale na centymetry"""
    total_inches = (feet * 12) + inches  
    return total_inches * 2.54 
