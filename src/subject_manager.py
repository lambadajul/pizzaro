from config import SUBJECTS_FILE
from repository import load

def subjects():
    return load(SUBJECTS_FILE)
