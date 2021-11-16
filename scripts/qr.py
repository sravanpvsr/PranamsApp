import os
from PranamsApp.models import Maid
from pathlib import Path
import pyqrcode
import png
from pyqrcode import QRCode

def run():
    
    sat=Maid.objects.filter(Status='Y')
    m_name=[]
    m_id=[]
    m_s_id=[]
    
    for s in sat:            
        m_name=str.upper(s.Maid_Name)
        m_id=s.Maid_ID
        m_night_duty=str.upper(s.NightDuty_Permitted)
        m_photo=str(s.Photo_File_Name)
        m_s_id=s.id   

        os.chdir(os.getcwd()+"\media\qr")
        qrCode = pyqrcode.create(m_id)
        
    
# Create and save the png file naming "myqr.png"
        qrCode.png(str(f"{m_id}")+str('.png'), scale = 6)    
        os.chdir('..')
        os.chdir('..')
        print(m_id)
        print(os.getcwd())
    return m_id