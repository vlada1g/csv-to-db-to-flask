from datetime import datetime
from api import db


class Advertisement(db.Model):
    # __tablename__= 'advertisement'
    id = db.Column(db.Integer, primary_key=True)# int,19
    logtype = db.Column(db.Integer)# int,1
    wp_type = db.Column(db.Integer)# int,1
    campaign_id = db.Column(db.Integer)# int,7
    banner_id = db.Column(db.Integer)# int,7
    werbeplatz_id = db.Column(db.Integer)# int,7
    peer_ip = db.Column(db.Integer)# int,10
    userid = db.Column(db.Integer)# int,19
    timestamp = db.Column(db.Integer)# int,10
    proxy_ip = db.Column(db.Integer)# int,1
    time = db.Column(db.DateTime)# datetime,22
    network = db.Column(db.Integer)# int,3
    browser = db.Column(db.Integer)# int,2
    os = db.Column(db.Integer)# int,2
    screen_res = db.Column(db.Integer)# int,3
    country = db.Column(db.Integer)# int,3
    state = db.Column(db.Integer)# int,4
    delivered_as = db.Column(db.Integer)# int,1
    city = db.Column(db.Integer)# int,6
    connection = db.Column(db.Integer)# int,1
    fvers = db.Column(db.Integer)# int,2
    gk = db.Column(db.Integer)# int,1
    mdev = db.Column(db.Integer)# int,1
    subreq = db.Column(db.Integer)# int,1
    server_id = db.Column(db.Integer)# int,3
    svz_id = db.Column(db.String(20))# object,14 (int + str; str = '\N')
    fraud_action = db.Column(db.Integer)# int,1
    fraud_detection_results = db.Column(db.Integer)# int,1
    used_batch_media = db.Column(db.Integer)# int,1