import os,sys
from PranamsApp.models import Maid, maid_renewal
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pathlib import Path

def run():
    sat=Maid.objects.filter(Status='Y')

    m_name=[]
    m_id=[]
    m_night_duty=[]
    m_photo=[]
    m_validity=[]
    
    for s in sat:            
        m_name=str.upper(s.Maid_Name)
        m_id=s.Maid_ID
        m_night_duty=str.upper(s.NightDuty_Permitted)
        m_photo=str(s.Photo_File_Name)
        m_qr=str(s.QR_Code)

        sat2=maid_renewal.objects.filter(Maid_ID=m_id,Status='Y')

        for s2 in sat2:
            original_date = datetime.strptime(str(s2.Validity), '%Y-%m-%d')
            formatted_date = original_date.strftime("%d-%m-%Y")    
            m_validity=formatted_date 
        
        font = ImageFont.truetype("CORBEL.TTF", size=20)
        font2= ImageFont.truetype("CORBEL.TTF", size=24)
        template = Image.open("Template.png")
        os.chdir(os.getcwd()+"\media")
        file=Path(f"{m_photo}")
        qr=Path(f"{m_qr}")
        
        if os.path.isfile(file):
            pic = Image.open(f"{m_photo}").resize((150, 150), Image.ANTIALIAS)
            template.paste(pic, (360, 120, 510, 270))
       
        os.chdir(os.getcwd()+"\qr")
        pic2 = Image.open(f"{m_qr}").resize((85, 85), Image.ANTIALIAS)
        template.paste(pic2, (425, 10, 510, 95))
        draw = ImageDraw.Draw(template)  

        os.chdir('..')
        
        draw.text((150, 130), m_name, fill='black',font=font)
        draw.text((150, 165), str(m_id), fill='black',font=font2)
        draw.text((150, 200), m_night_duty, fill='black',font=font)
        draw.text((150, 235), m_validity, fill='black',font=font2)
        template.save(f'maidIDs/{str(m_id)}.jpg')
        os.chdir('..')
    return template