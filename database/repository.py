from datetime import datetime, timedelta

from database.database import SessionLocal

from database.models import (
    AviatorHistory,
    MinesHistory
)


class Repository:

    # ===========================
    # AVIATOR
    # ===========================

    def save_aviator(self, multiplier):

        db = SessionLocal()

        try:

            row = AviatorHistory(
                multiplier=multiplier
            )

            db.add(row)

            db.commit()

        finally:

            db.close()

    def get_last_aviator(self, limit=100):

        db = SessionLocal()

        try:

            return (
                db.query(AviatorHistory)
                .order_by(AviatorHistory.id.desc())
                .limit(limit)
                .all()
            )

        finally:

            db.close()

    # ===========================
    # MINES
    # ===========================

    def save_mines(self, mines, board):

        db = SessionLocal()

        try:

            row = MinesHistory(
                mines=mines,
                board=str(board)
            )

            db.add(row)

            db.commit()

        finally:

            db.close()

    def get_last_mines(self, limit=100):

        db = SessionLocal()

        try:

            return (
                db.query(MinesHistory)
                .order_by(MinesHistory.id.desc())
                .limit(limit)
                .all()
            )

        finally:

            db.close()

    # ===========================
    # CONSULTAS GERAIS
    # ===========================

    def get_aviator_today(self):

        db = SessionLocal()

        try:

            today = datetime.now().date()

            return (
                db.query(AviatorHistory)
                .filter(
                    AviatorHistory.created_at >= today
                )
                .all()
            )

        finally:

            db.close()

    def get_mines_today(self):

        db = SessionLocal()

        try:

            today = datetime.now().date()

            return (
                db.query(MinesHistory)
                .filter(
                    MinesHistory.created_at >= today
                )
                .all()
            )

        finally:

            db.close()

    def get_aviator_last_hour(self):

        db = SessionLocal()

        try:

            hour = datetime.now() - timedelta(hours=1)

            return (
                db.query(AviatorHistory)
                .filter(
                    AviatorHistory.created_at >= hour
                )
                .all()
            )

        finally:

            db.close()

    def get_mines_last_hour(self):

        db = SessionLocal()

        try:

            hour = datetime.now() - timedelta(hours=1)

            return (
                db.query(MinesHistory)
                .filter(
                    MinesHistory.created_at >= hour
                )
                .all()
            )

        finally:

            db.close()