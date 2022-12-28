from .atri import Atri
from fastapi import Request, Response
from atri_utils import *
import time


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
    pass
def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.Flex38.onClick:
        if at.Div71.styles.left == '':
            x=0
        elif at.Div71.styles.left[6]=='4':
            x=-1
        else:
            x=int(at.Div71.styles.left[6])
        x+=1
        at.Div71.styles.left= f"calc(-{x} * (40% + 24px))"


    if at.Flex39.onClick:
        if at.Div71.styles.left == '':
            x=5
        elif at.Div71.styles.left[6]=='0':
            x=5
        else:
            x=int(at.Div71.styles.left[6])
        x-=1
        at.Div71.styles.left= f"calc(-{x} * (40% + 24px))"

    if at.Flex111.onClick:
        if at.Flex114.styles.opacity=='' or at.Flex114.styles.opacity== '100%':
            at.Div181.styles.left='50%'
            at.Flex114.styles.opacity= '0'
            at.Flex116.styles.opacity= '100%'
            at.Div181.styles.left='0%'
        
        else:
            at.Div177.styles.left='50%'
            at.Flex116.styles.opacity= '0'
            at.Flex114.styles.opacity= '100%'
            at.Div177.styles.left='0%'
