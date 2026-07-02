import ast

from analyzer.base_analyzer import BaseAnalyzer


class MinesAnalyzer(BaseAnalyzer):

    def analyze(self, limit=100):

        rows = self.repository.get_last_mines(limit)

        if not rows:
            return None

        total = len(rows)

        board_frequency = [0] * 25

        mines_frequency = {}

        for row in rows:

            mines_frequency[row.mines] = (
                mines_frequency.get(row.mines, 0) + 1
            )

            board = ast.literal_eval(row.board)

            for index, value in enumerate(board):

                if value == 1:
                    board_frequency[index] += 1

        percentages = [
            round((value / total) * 100, 2)
            for value in board_frequency
        ]

        safest = sorted(
            enumerate(percentages),
            key=lambda x: x[1]
        )[:5]

        riskiest = sorted(
            enumerate(percentages),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        return {

            "total": total,

            "board": percentages,

            "mines": mines_frequency,

            "safest": safest,

            "riskiest": riskiest

        }