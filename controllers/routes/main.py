from .atri import Atri
from fastapi import Request, Response
from atri_utils import *


def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.Flex38.onClick:
        if at.Div71.styles.left == '':
            x=0
        else:
            x=float(at.Div71.styles.left.strip('px'))
            if x<-1447.95:
                x=482.65    
        # print(x)
        x-=482.65
        at.Div71.styles.left= f"{x}px"

    if at.Flex39.onClick:
        if at.Div71.styles.left == '':
            x=0
        else:
            x=float(at.Div71.styles.left.strip('px'))
        x+=482.65
        if x>1:
            x=-1930.6            
        at.Div71.styles.left= f"{x}px"