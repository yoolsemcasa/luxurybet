from database.database import SessionLocal

from database.models import (
    AviatorHistory,
    MinesHistory
)


class Repository:

    def __init__(self):

        self.db = SessionLocal()

    # ===========================
    # AVIATOR
    # ===========================

    def save_aviator(self, multiplier):

        row = AviatorHistory(
            multiplier=multiplier
        )

        self.db.add(row)

        self.db.commit()

    # ===========================
    # MINES
    # ===========================

    def save_mines(self, mines, board):

        row = MinesHistory(

            mines=mines,

            board=str(board)

        )

        self.db.add(row)

        self.db.commit()