from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import unittest
from tevai_vaikai_m2m import *


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n=== Paruosiam testavimo klase ===")

    @classmethod
    def tearDownClass(cls):
        engine = create_engine("sqlite:///projektai/tevai_vaikai_m2m.db")
        session = sessionmaker(bind=engine)()
        tevai = session.query(Tevas).all()
        vaikai = session.query(Vaikas).all()
        for tevas in tevai:
            session.delete(tevas)
        for vaikas in vaikai:
            session.delete(vaikas)
        session.commit()
        print("\n=== Valytuvai veikia ===")
        return super().tearDownClass()

    def setUp(self):
        self.engine = create_engine("sqlite:///projektai/tevai_vaikai_m2m.db")
        self.session = sessionmaker(bind=self.engine)()
        print("\n=== Paruosiam nauja testavimo metoda ===")

    def test_000_insert_tevas(self):
        lukestis_tetis = Tevas(vardas="Tetux", pavarde="Vardelis")
        lukestis_mama = Tevas(vardas="Mamike", pavarde="Vardeliene")
        self.session.add(lukestis_tetis)
        self.session.add(lukestis_mama)
        self.session.commit()
        rezultatas_tetis = session.query(Tevas).filter_by(vardas=lukestis_tetis.vardas, pavarde=lukestis_tetis.pavarde).one()
        rezultatas_mama = session.query(Tevas).filter_by(vardas=lukestis_mama.vardas, pavarde=lukestis_mama.pavarde).one()
        self.assertEqual(lukestis_tetis.id, rezultatas_tetis.id)
        self.assertEqual(lukestis_mama.id, rezultatas_mama.id)

    # def test_001_insert_vaikas(self):
    #     pirmas = Vaikas(vardas="Geras", pavarde="Vardelis")
    #     antra = Vaikas(vardas="Smagi", pavarde="Vardelyte")
    #     self.session.add(pirmas)
    #     self.session.add(antra)
    #     self.session.commit()


if __name__ == "__main__":
    unittest.main()
