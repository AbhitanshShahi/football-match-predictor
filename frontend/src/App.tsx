import { useState } from "react";
import TeamSelector from "./components/TeamSelector";
import Result from "./components/Result";
import Loader from "./components/Loader";
import { predictMatch } from "./utils/api";
import type { PredictionOutput } from "./utils/types";
import { Trophy, MapPin } from "lucide-react";

export default function App() {
  const [home, setHome] = useState("");
  const [away, setAway] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionOutput | null>(null);
  const [neutral, setNeutral] = useState(false);

  async function handlePredict() {
    if (!home || !away) return;
    setLoading(true);
    setResult(null);
    try {
      const res = await predictMatch({
        home_team: home,
        away_team: away,
        neutral: neutral ? 1 : 0,
      });
      console.log(res);
      setResult(res.prediction);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-linear-to-br from-emerald-950 via-green-900 to-teal-950 text-white overflow-hidden relative">
      {/* Background Pattern */}
      <div className="absolute inset-0 bg-[radial-gradient(#ffffff10_1px,transparent_1px)] bg-size-[40px_40px] opacity-30"></div>

      {/* Header */}
      <div className="relative pt-8 pb-6 text-center">
        <div className="flex items-center justify-center gap-4 mb-3">
          <div className="p-3 bg-yellow-400 text-emerald-950 rounded-2xl shadow-xl">
            <Trophy className="w-10 h-10" />
          </div>
          <h1 className="text-5xl font-black tracking-tighter bg-clip-text text-transparent bg-linear-to-r from-white via-yellow-200 to-white">
            WORLD CUP
          </h1>
          <div className="p-3 bg-yellow-400 text-emerald-950 rounded-2xl shadow-xl">
            <Trophy className="w-10 h-10" />
          </div>
        </div>
        <p className="text-emerald-300 text-xl font-medium tracking-wide">
          MATCH PREDICTOR
        </p>
        <div className="mt-2 text-emerald-400/70 text-sm flex items-center justify-center gap-1.5">
          <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
          FIFA OFFICIAL SIMULATION
        </div>
      </div>

      <div className="max-w-3xl mx-auto px-6 pb-12">
        <div className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl shadow-2xl overflow-hidden">
          {/* Stadium Top Bar */}
          <div className="h-2 bg-linear-to-r from-yellow-400 via-emerald-400 to-yellow-400"></div>

          <div className="p-8">
            {/* Team Selector */}
            <TeamSelector
              home={home}
              away={away}
              setHome={setHome}
              setAway={setAway}
            />

            {/* Neutral Venue */}
            <div className="flex items-center justify-center gap-3 mt-8 bg-white/5 border border-white/10 rounded-2xl p-4">
              <MapPin className="w-5 h-5 text-emerald-400" />
              <label className="flex items-center gap-3 cursor-pointer group">
                <input
                  type="checkbox"
                  checked={neutral}
                  onChange={(e) => setNeutral(e.target.checked)}
                  className="w-5 h-5 accent-yellow-400 bg-white/10 border-white/30 rounded focus:ring-yellow-400"
                />
                <span className="text-emerald-200 group-hover:text-white transition-colors">
                  Neutral Ground
                </span>
              </label>
            </div>

            {/* Predict Button */}
            <button
              onClick={handlePredict}
              disabled={!home || !away}
              className="mt-8 w-full bg-linear-to-r from-yellow-400 to-amber-400 hover:from-yellow-300 hover:to-amber-300 disabled:from-gray-600 disabled:to-gray-500 text-emerald-950 font-black text-2xl py-6 rounded-2xl transition-all duration-300 active:scale-[0.985] shadow-xl flex items-center justify-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span>KICK OFF</span>
              <span className="text-3xl">⚽</span>
            </button>

            {loading && <Loader />}

            {/* Result Area */}
            <div className="mt-8">
              <Result result={result} />
            </div>
          </div>

          {/* Footer Accent */}
          <div className="h-1.5 bg-linear-to-r from-yellow-400 via-emerald-400 to-yellow-400"></div>
        </div>

        {/* Decorative Elements */}
        <div className="flex justify-between text-[120px] opacity-10 pointer-events-none mt-6">
          <div>⚽</div>
          <div>🏆</div>
        </div>
      </div>
    </div>
  );
}
