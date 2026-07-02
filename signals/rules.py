from signals.base_signal import Signal


class Rules:

    @staticmethod
    def aviator(stats):

        if not stats:
            return None

        if stats["average"] >= 5:

            return Signal(

                title="Aviator",

                message="Média histórica acima do limite configurado.",

                level="INFO"

            )

        return None

    @staticmethod
    def mines(stats):

        if not stats:
            return None

        if stats["total"] >= 100:

            return Signal(

                title="Mines",

                message="Quantidade mínima de histórico atingida.",

                level="INFO"

            )

        return None