from signals.rules import Rules


class SignalEngine:

    def generate(self, aviator_stats, mines_stats):

        signals = []

        signal = Rules.aviator(aviator_stats)

        if signal:

            signals.append(signal)

        signal = Rules.mines(mines_stats)

        if signal:

            signals.append(signal)

        return signals