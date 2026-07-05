import type { PredictionOutput } from "../utils/types";

type Props = {
  result: PredictionOutput | null;
};

export default function Result({ result }: Props) {
  if (!result) return null;

  const homePercent = Math.round(result.home_win * 100);
  const drawPercent = Math.round(result.draw * 100);
  const awayPercent = Math.round(result.away_win * 100);

  return (
    <div className="bg-white/5 border border-white/10 rounded-3xl p-8">
      <div className="flex items-center justify-between mb-8">
        <h2 className="text-3xl font-black tracking-tighter">
          MATCH PREDICTION
        </h2>
        <div className="text-xs uppercase tracking-widest bg-yellow-400/10 text-yellow-400 px-4 py-1.5 rounded-full border border-yellow-400/30">
          HIGH CONFIDENCE
        </div>
      </div>

      <div className="space-y-7">
        {/* Home Win */}
        <div>
          <div className="flex justify-between text-sm mb-2 font-medium">
            <div className="flex items-center gap-2">
              <span className="text-emerald-400">HOME WIN</span>
            </div>
            <span className="tabular-nums font-mono">{homePercent}%</span>
          </div>
          <div className="h-4 bg-white/10 rounded-full overflow-hidden">
            <div
              className="h-full bg-linear-to-r from-emerald-400 to-teal-400 transition-all duration-700"
              style={{ width: `${homePercent}%` }}
            />
          </div>
        </div>

        {/* Draw */}
        <div>
          <div className="flex justify-between text-sm mb-2 font-medium">
            <div className="flex items-center gap-2">
              <span className="text-amber-400">DRAW</span>
            </div>
            <span className="tabular-nums font-mono">{drawPercent}%</span>
          </div>
          <div className="h-4 bg-white/10 rounded-full overflow-hidden">
            <div
              className="h-full bg-linear-to-r from-amber-400 to-yellow-400 transition-all duration-700"
              style={{ width: `${drawPercent}%` }}
            />
          </div>
        </div>

        {/* Away Win */}
        <div>
          <div className="flex justify-between text-sm mb-2 font-medium">
            <div className="flex items-center gap-2">
              <span className="text-rose-400">AWAY WIN</span>
            </div>
            <span className="tabular-nums font-mono">{awayPercent}%</span>
          </div>
          <div className="h-4 bg-white/10 rounded-full overflow-hidden">
            <div
              className="h-full bg-linear-to-r from-rose-400 to-red-500 transition-all duration-700"
              style={{ width: `${awayPercent}%` }}
            />
          </div>
        </div>
      </div>

      <div className="mt-10 pt-6 border-t border-white/10 text-center text-xs text-emerald-400/70">
        Probabilities based on historical data, form, and venue
      </div>
    </div>
  );
}
