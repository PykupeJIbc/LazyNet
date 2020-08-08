from . import db

class Clients(db.Model):
    __tablename__ = 'CLIENTS'
    id = db.Column('CLIENT_ID', db.Integer, primary_key=True)
    name = db.Column('CLIENT_NAME', db.Unicode, unique=True)
    reg_date = db.Column('CLIENT_REG_DATE', db.DateTime)
    description = db.Column('CLIENT_DESCRIPTION', db.Unicode)
    speed = db.Column('CLIENT_SPEED', db.Integer)
    email = db.Column('ALERT_MAIL', db.Unicode)

    def __repr__(self):
        return '<Clients {}>'.format(self.id)


class Routers(db.Model):
    __tablename__ = 'ROUTERS'
    id = db.Column('ROUTER_ID', db.Integer, primary_key=True)
    ip = db.Column('ROUTER_IP', db.Integer)
    name = db.Column('ROUTER_NAME', db.Unicode)
    loc = db.Column('ROUTER_LOC', db.Unicode)
    description = db.Column('ROUTER_DESCRIPTION', db.Unicode)

    def __repr__(self):
        return '<Routers {}>'.format(self.id)


class Interfaces(db.Model):
    __tablename__ = 'ROUTERIFMAP'
    id = db.Column('IF_ID', db.Integer, primary_key=True)
    r_id = db.Column('ROUTER_ID', db.Integer)
    name = db.Column('IF_NAME', db.Unicode)
    index = db.Column('IF_INDEX', db.Integer)
    speed = db.Column('IF_SPEED', db.Integer)
    description = db.Column('IF_DESCRIPTION', db.Unicode)

    def __repr__(self):
        return '<Interfaces {}>'.format(self.id)


class Maps(db.Model):
    __tablename__ = 'CLIENTMAP'
    client_id = db.Column('CLIENT_ID', db.Integer)
    router_id = db.Column('ROUTER_ID', db.Integer)
    if_id = db.Column('IF_ID', db.Integer)
    client_ip = db.Column('CLIENT_IP', db.Integer, primary_key=True)

    def __repr__(self):
        return '<Maps {}>'.format(self.id)