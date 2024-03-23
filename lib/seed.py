from models import Auditions, Role, engine
from sqlalchemy.orm import sessionmaker

# creating a session
Session = sessionmaker(bind=engine)
session = Session()

audition1 = Auditions(location='first l', phone='first p', hired=True)
audition2 = Auditions(location='second l', phone='second p', hired=False)

role1 = Role(character_name='char 1')
role2 = Role(character_name='char 2')

audition1.role = role1
audition2.role = role2

session.add(audition1)
session.add(audition2)
session.add(role1)
session.add(role2)

session.commit()

print(audition1.location)
print(audition2.location)