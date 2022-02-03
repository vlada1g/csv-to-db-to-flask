from api.models import Advertisement
from flask import Flask
from api import app,db
from flask import abort
from sqlalchemy import exc

@app.route('/user/<user_id>', methods=['GET'])
def advert_seen(user_id):
    
    advert = db.session.query(Advertisement).filter(
    Advertisement.userid == user_id).all()
 
    return {"advertisements": len(advert)}