from analyzer.base_analyzer import BaseAnalyzer


class AviatorAnalyzer(BaseAnalyzer):

    def analyze(self, limit=100):

        rows = self.repository.get_last_aviator(limit)

        if not rows:

            return None

        multipliers = [
            row.multiplier
            for row in rows
        ]

        total = len(multipliers)

        average = sum(multipliers) / total

        highest = max(multipliers)

        lowest = min(multipliers)

        above_2 = (
            sum(
                1
                for value in multipliers
                if value >= 2
            ) / total
        ) * 100

        above_5 = (
            sum(
                1
                for value in multipliers
                if value >= 5
            ) / total
        ) * 100

        above_10 = (
            sum(
                1
                for value in multipliers
                if value >= 10
            ) / total
        ) * 100

        return {

            "total": total,

            "average": round(average, 2),

            "highest": highest,

            "lowest": lowest,

            "above_2": round(above_2, 2),

            "above_5": round(above_5, 2),

            "above_10": round(above_10, 2)

        }